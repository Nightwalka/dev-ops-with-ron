# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
url = ""
API_TOKEN=""
auth = HTTPBasicAuth("", API_TOKEN)



headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
j=0
for i in range(len(output)):
    j=j+1
    name = output[i]["name"]
    key = output[i]["key"]
    print(f"you have projet: {j} called: {name} with the key: {key}")

print("\n")

for project in output:
    # project is the HOUSE ITSELF (the dictionary)
    name = project["name"]
    key = project["key"]
    print(f"Project Name: {name}, Key: {key}")

for j, project in enumerate(output):
    # j is the HOUSE NUMBER (0, 1, 2, etc.)
    # project is the HOUSE ITSELF (the dictionary)
    name = project["name"]
    key = j
    print(f"Project #{j+1}: Name: {name}, Key: {key}")