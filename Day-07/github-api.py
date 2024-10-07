import requests

url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'
response = requests.get(url)

compelete_detail = response.json()

for i in range(len(compelete_detail)):
    print(compelete_detail[i]["user"]["login"])