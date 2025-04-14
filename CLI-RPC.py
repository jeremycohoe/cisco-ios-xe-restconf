import requests
from requests.auth import HTTPBasicAuth
import urllib3

# Disable SSL warnings for self-signed certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Device info
router_ip = "10.85.134.65"
username = "admin"
password = "password"

# RESTCONF RPC endpoint
url = f"https://{router_ip}/restconf/operations/Cisco-IOS-XE-cli-rpc:config-ios-cli-rpc"

# Headers
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}

# Payload to send "do show run"
payload = {
    "Cisco-IOS-XE-cli-rpc:input": {
        "config-clis": "do show run"
    }
}

# POST the RPC
response = requests.post(
    url,
    auth=HTTPBasicAuth(username, password),
    headers=headers,
    json=payload,
    verify=False
)

if response.status_code == 200:
    print("Success!\n")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
