

import requests

user = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
users = user.json()
for i in range(len(users)):
    print(users[i]["user"]["login"])