"""
Implementation of Steam client based on ``gevent``

.. warning::
    ``steam.client`` no longer patches stdlib to make it gevent cooperative.
    This provides flexibility if you want to use :class:`.SteamClient` with async or other modules.
    If you want to monkey patch anyway use :meth:`steam.monkey.patch_minimal()`

.. note::
    Additional features are located in separate submodules. All functionality from :mod:`.builtins` is inherited by default.

.. note::
    Optional features are available as :mod:`.mixins`. This allows the client to remain light yet flexible.

"""
import os
import json
from random import random
from time import time
from io import open
from getpass import getpass
import logging
import six

from eventemitter import EventEmitter
from steam.enums import EResult, EOSType, EPersonaState
from steam.enums.emsg import EMsg
from steam.core.cm import CMClient
from steam.core.msg import MsgProto
from steam.core.crypto import sha1_hash
from steam.steamid import SteamID
from steam.exceptions import SteamError
from steam.client.builtins import BuiltinBase
from steam.utils import ip4_from_int, ip4_to_int
from steam.utils.proto import proto_fill_from_dict


# TODO: remove py2 support.
if six.PY2:
    _cli_input = raw_input
else:
    _cli_input = input


class SteamClient(CMClient, BuiltinBase):
    EVENT_LOGGED_ON = 'logged_on'
    """After successful login"""

    _LOG = logging.getLogger("SteamClient")
    _reconnect_backoff_c = 0
    current_jobid = 0
    username = None                    #: username when logged on
    chat_mode = 2                      #: chat mode (0=old chat, 2=new chat)

    def __init__(self):
        CMClient.__init__(self)

        # register listners
        self.on(self.EVENT_DISCONNECTED, self._handle_disconnect)
        self.on(self.EVENT_RECONNECT, self._handle_disconnect)

        #: indicates logged on status. Listen to ``logged_on`` when change to ``True``
        self.logged_on = False

        BuiltinBase.__init__(self)

    def __repr__(self):
        return "<%s(%s) %s>" % (self.__class__.__name__,
                              repr(self.current_server_addr),
                              'online' if self.connected else 'offline',
                              )

    def connect(self, *args, **kwargs):
        """Attempt to establish connection, see :meth:`.CMClient.connect`"""
        return CMClient.connect(self, *args, **kwargs)

    def disconnect(self, *args, **kwargs):
        """Close connection, see :meth:`.CMClient.disconnect`"""
        self.logged_on = False
        CMClient.disconnect(self, *args, **kwargs)

    def _parse_message(self, message):
        result = CMClient._parse_message(self, message)

        if result is None:
            return

        emsg, msg = result

        # emit job events
        if msg.proto:
            jobid = msg.header.jobid_target
        else:
            jobid = msg.header.targetJobID

        if jobid not in (-1, 18446744073709551615):
            jobid = "job_%d" % jobid
            if msg.body is None and self.count_listeners(jobid):
                msg.parse()
            self.emit(jobid, msg)

        # emit UMs
        if emsg in (EMsg.ServiceMethod, EMsg.ServiceMethodResponse, EMsg.ServiceMethodSendToClient):
            if msg.body is None and self.count_listeners(msg.header.target_job_name):
                msg.parse()
            self.emit(msg.header.target_job_name, msg)

    def _handle_cm_list(self, msg):
        if (self.cm_servers.last_updated + 3600*24 > time()
           and self.cm_servers.cell_id != 0):
            return
        CMClient._handle_cm_list(self, msg)  # clear and merge

    def _handle_disconnect(self, *args):
        self.logged_on = False
        self.current_jobid = 0

    def _handle_logon(self, msg):
        CMClient._handle_logon(self, msg)

        result = EResult(msg.body.eresult)

        if result == EResult.OK:
            self._reconnect_backoff_c = 0
            self.logged_on = True
            self.emit(self.EVENT_LOGGED_ON)
            return

        # CM kills the connection on error anyway
        self.disconnect()

    def reconnect(self, maxdelay=30, retry=0):
        """Implements explonential backoff delay before attempting to connect.
        It is otherwise identical to calling :meth:`.CMClient.connect`.
        The delay is reset upon a successful login.

        :param maxdelay: maximum delay in seconds before connect (0-120s)
        :type maxdelay: :class:`int`
        :param retry: see :meth:`.CMClient.connect`
        :type retry: :class:`int`
        :return: successful connection
        :rtype: :class:`bool`
        """
        delay_seconds = 2**self._reconnect_backoff_c - 1

        if delay_seconds < maxdelay:
            self._reconnect_backoff_c = min(7, self._reconnect_backoff_c + 1)

        delay_seconds = int(delay_seconds * 0.5 + delay_seconds * 0.5 * random())

        return self.connect(delay=delay_seconds, retry=retry)

    def wait_msg(self, event, timeout=None, raises=None):
        """Wait for a message, similiar to :meth:`.wait_event`

        :param event: event id
        :type  event: :class:`.EMsg` or :class:`str`
        :param timeout: seconds to wait before timeout
        :type  timeout: :class:`int`
        :param raises: On timeout when ``False`` returns :class:`None`, else raise :class:`gevent.Timeout`
        :type  raises: :class:`bool`
        :return: returns a message or :class:`None`
        :rtype: :class:`None`, or `proto message`
        :raises: :class:`gevent.Timeout`
        """
        resp = self.wait_event(event, timeout, raises)

        if resp is not None:
            return resp[0]

    def send(self, message, body_params=None):
        """Send a message to CM

        :param message: a message instance
        :type message: :class:`.Msg`, :class:`.MsgProto`
        :param body_params: a dict with params to the body (only :class:`.MsgProto`)
        :type body_params: dict
        """
        if not self.connected:
            self._LOG.debug("Trying to send message when not connected. (discarded)")
        else:
            if body_params and isinstance(message, MsgProto):
                proto_fill_from_dict(message.body, body_params)

            CMClient.send(self, message)

    def send_job(self, message, body_params=None):
        """Send a message as a job

        .. note::
            Not all messages are jobs, you'll have to find out which are which

        :param message: a message instance
        :type message: :class:`.Msg`, :class:`.MsgProto`
        :param body_params: a dict with params to the body (only :class:`.MsgProto`)
        :type body_params: dict
        :return: ``jobid`` event identifier
        :rtype: :class:`str`

        To catch the response just listen for the ``jobid`` event.

        .. code:: python

            jobid = steamclient.send_job(my_message)

            resp = steamclient.wait_event(jobid, timeout=15)
            if resp:
                (message,) = resp

        """
        jobid = self.current_jobid = ((self.current_jobid + 1) % 10000) or 1
        self.remove_all_listeners('job_%d' % jobid)

        if message.proto:
            message.header.jobid_source = jobid
        else:
            message.header.sourceJobID = jobid

        self.send(message, body_params)

        return "job_%d" % jobid

    def send_job_and_wait(self, message, body_params=None, timeout=None, raises=False):
        """Send a message as a job and wait for the response.

        .. note::
            Not all messages are jobs, you'll have to find out which are which

        :param message: a message instance
        :type  message: :class:`.Msg`, :class:`.MsgProto`
        :param body_params: a dict with params to the body (only :class:`.MsgProto`)
        :type  body_params: dict
        :param timeout: (optional) seconds to wait
        :type  timeout: :class:`int`
        :param raises: (optional) On timeout if ``False`` return ``None``, else raise :class:`gevent.Timeout`
        :type  raises: :class:`bool`
        :return: response proto message
        :rtype: :class:`.Msg`, :class:`.MsgProto`
        :raises: :class:`gevent.Timeout`
        """
        job_id = self.send_job(message, body_params)
        response = self.wait_event(job_id, timeout, raises=raises)
        if response is None:
            return None
        return response[0].body

    def send_message_and_wait(self, message, response_emsg, body_params=None, timeout=None, raises=False):
        """Send a message to CM and wait for a defined answer.

        :param message: a message instance
        :type  message: :class:`.Msg`, :class:`.MsgProto`
        :param response_emsg: emsg to wait for
        :type  response_emsg: :class:`.EMsg`,:class:`int`
        :param body_params: a dict with params to the body (only :class:`.MsgProto`)
        :type  body_params: dict
        :param timeout: (optional) seconds to wait
        :type  timeout: :class:`int`
        :param raises: (optional) On timeout if ``False`` return ``None``, else raise :class:`gevent.Timeout`
        :type  raises: :class:`bool`
        :return: response proto message
        :rtype: :class:`.Msg`, :class:`.MsgProto`
        :raises: :class:`gevent.Timeout`
        """
        self.send(message, body_params)
        response = self.wait_event(response_emsg, timeout, raises=raises)
        if response is None:
            return None
        return response[0].body

    def _pre_login(self):
        if self.logged_on:
            self._LOG.debug("Trying to login while logged on???")
            raise RuntimeError("Already logged on")

        if not self.connected and not self._connecting:
            if not self.connect():
                return EResult.Fail

        if not self.channel_secured:
            resp = self.wait_event(self.EVENT_CHANNEL_SECURED, timeout=10)

            # some CMs will not send hello
            if resp is None:
                if self.connected:
                    self.wait_event(self.EVENT_DISCONNECTED)
                return EResult.TryAnotherCM

        return EResult.OK

    def login(self, username, password='', access_token='', login_id=None):
        """Login as a specific user.

        :param username: optionally provide username
        :type  username: :class:`str`
        :param password: optionally provide password
        :type  password: :class:`str`
        :param access_token: optionally, provide access token
        :type  access_token: :class:`str`
        :return: logon result, see `CMsgClientLogonResponse.eresult`
        :rtype: :class:`.EResult`

        .. note::
            Failure to login will result in the server dropping the connection, ``error`` event is fired

        If you have 2FA/SteamGuard, login first with :class:`WebAuth` then pass
        the WebAuth `refresh_token` as Client `access_token`.
        You can save the `username` and `refresh_token` somewhere for automatic
        login at a later time.

        Example:

        .. code:: python
            In [1]: import steam.client, steam.webauth
            In [2]: webauth = steam.webauth.WebAuth()
            In [3]: _ = webauth.cli_login('username')
            Enter password for 'username':
            Enter your Steam Guard code (or simply press Enter if approved via app):
            In [4]: client = steam.client.SteamClient()
            In [5]: client.login(webauth.username, access_token=webauth.refresh_token)
            Out[5]: <EResult.OK: 1>
        """
        self._LOG.debug("Attempting steam client login from webauth")
        if not password and not access_token:
            raise RuntimeError("Must provide either password or access token")

        eresult = self._pre_login()
        if eresult != EResult.OK:
            return eresult

        self.username = username

        message = MsgProto(EMsg.ClientLogon)
        message.header.steamid = SteamID(type='Individual', universe='Public')
        message.body.protocol_version = 65580
        message.body.client_os_type = EOSType.Windows10
        message.body.client_language = "english"
        message.body.should_remember_password = True
        message.body.supports_rate_limit_response = True
        message.body.chat_mode = self.chat_mode

        if login_id is None:
            message.body.obfuscated_private_ip.v4 = ip4_to_int(self.connection.local_address) ^ 0xBAADF00D
        else:
            message.body.obfuscated_private_ip.v4 = login_id

        message.body.account_name = username

        if access_token:
            message.body.access_token = access_token
        else:
            message.body.password = password

        self.send(message)

        resp = self.wait_msg(EMsg.ClientLogOnResponse, timeout=30)

        if resp and resp.body.eresult == EResult.OK:
            self.sleep(0.5)

        return EResult(resp.body.eresult) if resp else EResult.Fail

    def anonymous_login(self):
        """Login as anonymous user

        :return: logon result, see `CMsgClientLogonResponse.eresult <https://github.com/ValvePython/steam/blob/513c68ca081dc9409df932ad86c66100164380a6/protobufs/steammessages_clientserver.proto#L95-L118>`_
        :rtype: :class:`.EResult`
        """
        self._LOG.debug("Attempting Anonymous login")

        eresult = self._pre_login()

        if eresult != EResult.OK:
            return eresult

        self.username = None
        self.login_key = None

        message = MsgProto(EMsg.ClientLogon)
        message.header.steamid = SteamID(type='AnonUser', universe='Public')
        message.body.client_package_version = 1561159470
        message.body.protocol_version = 65580
        self.send(message)

        resp = self.wait_msg(EMsg.ClientLogOnResponse, timeout=30)
        return EResult(resp.body.eresult) if resp else EResult.Fail

    def logout(self):
        """
        Logout from steam. Doesn't nothing if not logged on.

        .. note::
            The server will drop the connection immediatelly upon logout.
        """
        if self.logged_on:
            self.logged_on = False
            self.send(MsgProto(EMsg.ClientLogOff))
            try:
                self.wait_event(self.EVENT_DISCONNECTED, timeout=5, raises=True)
            except:
                self.disconnect()
            self.idle()

    def run_forever(self):
        """
        Transfer control the gevent event loop

        This is useful when the application is setup and ment to run for a long time
        """
        while True:
            self.sleep(300)
