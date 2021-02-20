import requests
import re

# Authentication
username = "natasx"
password = ""

# URL
url = f"http://{username}.natas.labs.overthewire.org"

response = requests.get(url, auth=(username, password))
content = response.text

print(re.findall("<!--The password for natasx is (.*) -->", content)[0])