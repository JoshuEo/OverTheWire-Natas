import requests
import re

"""
Explanantion:
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
All you have to do is turn the hex to binary, reverse it, and then base64 decode the $encodedSecret and use it to enter into the secret field.
"""

# Authentication
username = "natas8"
password = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"

# URL
url = f"http://{username}.natas.labs.overthewire.org/"

response = requests.post(url, data={"secret":"oubWYf2kBq", "submit":"submit"}, auth=(username, password))
content = response.text

print(re.findall("The password for natas9 is (.*)", content)[0])