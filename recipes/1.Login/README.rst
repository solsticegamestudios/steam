one_off_login.py
----------------

Minimal example to login into Steam:
1) webauth login using ``cli_login()``
   supports SteamGuard and Email codes as well as app confirmation
2) steam login using the webauth token
3) print some account info and exit
No information is persisted to disk.

diy_one_off_login.py
--------------------

Same as above, but we make our own prompts instead of using ``cli_login()``.

persistent_login.py
-------------------

In this example, after the login prompt, the client will remain connected until interrupted.
The client will attempt to reconnect after losing network connectivity or when steam is down.
A json file is persisted to disk with the account information: ``credentials.json``.

