import requests
import re

# Authentication
username = "natas1"
password = "gtVrDuiDfck831PqWsLEZy5gyDz1clto"

# URL
url = f"http://{username}.natas.labs.overthewire.org"

response = requests.get(url, auth=(username, password))
content = response.text

print(re.findall("<!--The password for natas2 is (.*) -->", content)[0])