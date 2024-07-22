import json
import logging
import os
from steam.client import SteamClient
from steam.enums import EResult
from steam.webauth import WebAuth

# setup logging
logging.basicConfig(format="%(asctime)s | %(message)s", level=logging.INFO)
LOG = logging.getLogger()

# file to save/load credentials
CREDENTIALS = 'credentials.json'

if os.path.exists(CREDENTIALS):
    with open(CREDENTIALS) as f:
        credentials = json.load(f)
else:
    webauth = WebAuth()
    webauth.cli_login(input("Steam user: "))
    credentials = {
        'username': webauth.username,
        'refresh_token': webauth.refresh_token,
    }
    with open(CREDENTIALS, 'w') as f:
        json.dump(credentials, f, indent=4)

client = SteamClient()

@client.on("error")
def handle_error(result):
    LOG.info("Logon result: %s", repr(result))

@client.on("channel_secured")
def send_login():
    client.login(credentials['username'], access_token=credentials['refresh_token'])

@client.on("connected")
def handle_connected():
    LOG.info("Connected to %s", client.current_server_addr)

@client.on("reconnect")
def handle_reconnect(delay):
    LOG.info("Reconnect in %ds...", delay)

@client.on("disconnected")
def handle_disconnect():
    LOG.info("Disconnected.")
    LOG.info("Reconnecting...")
    client.reconnect(maxdelay=30)

@client.on("logged_on")
def handle_after_logon():
    LOG.info("-"*30)
    LOG.info("Logged on as: %s", client.user.name)
    LOG.info("Community profile: %s", client.steam_id.community_url)
    LOG.info("Last logon: %s", client.user.last_logon)
    LOG.info("Last logoff: %s", client.user.last_logoff)
    LOG.info("-"*30)
    LOG.info("Press ^C to exit")

# main bit
LOG.info("Persistent logon recipe")
LOG.info("-"*30)

result = client.connect()

if result != EResult.OK:
    LOG.info("Failed to login: %s" % repr(result))
    raise SystemExit

try:
    client.run_forever()
except KeyboardInterrupt:
    if client.connected:
        LOG.info("Logout")
        client.logout()
