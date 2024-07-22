from steam.client import SteamClient
from steam.enums import EResult
from steam.webauth import WebAuth

print("One-off login recipe")
print("-"*20)

webauth = WebAuth()
webauth.cli_login(input("Steam user: "))
client = SteamClient()
result = client.login(webauth.username, access_token=webauth.refresh_token)

if result != EResult.OK:
    print("Failed to login: %s" % repr(result))
    raise SystemExit

print("-"*20)
print("Logged on as:", client.user.name)
print("Community profile:", client.steam_id.community_url)
print("Last logon:", client.user.last_logon)
print("Last logoff:", client.user.last_logoff)

client.logout()
