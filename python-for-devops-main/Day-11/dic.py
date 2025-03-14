import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
# print(response.json())
output = response.json()

for element in range (len(output)):
    print(output[element]["user"]["login"])

print(response.status_code)