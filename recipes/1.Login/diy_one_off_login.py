from getpass import getpass
from steam.client import SteamClient
import steam.webauth as wa

print("One-off login recipe")
print("-"*20)

LOGON_DETAILS = {
    'username': input("Steam user: "),
    'password': getpass("Password: "),
}

webauth = wa.WebAuth()

try:
    webauth.login(**LOGON_DETAILS)
except wa.TwoFactorCodeRequired:
    webauth.login(code=input("Enter SteamGuard Code: "))
except wa.EmailCodeRequired:
    webauth.login(code=input("Enter Email Code: "))

client = SteamClient()

@client.on('error')
def error(result):
    print("Logon result:", repr(result))

try:
    client.login(webauth.username, access_token=webauth.refresh_token)
except:
    raise SystemExit

print("-"*20)
print("Logged on as:", client.user.name)
print("Community profile:", client.steam_id.community_url)
print("Last logon:", client.user.last_logon)
print("Last logoff:", client.user.last_logoff)

client.logout()
