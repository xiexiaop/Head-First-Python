
import requests
import json

# Get Access Token
url = "https://openapi.baidu.com/oauth/2.0/token"
params = {'grant_type': 'client_credentials', 'client_id': 'QdOwB4WRNE0jZDp57hFhBHlZ',
          'client_secret': 'sU0u4I0MDNXLiF5bslR8HknjSFIkCRA0'}
r = requests.get(url, params=params)
jsonObject = json.loads(r.text)
access_token = jsonObject['access_token']


# Send Voice File
url = 'http://vop.baidu.com/server_api'
headers = {'content-type': 'application/json', 'rate': '16000'}
params = {'dev_pid': 1536, 'cuid': 'baiduyuyin', 'token': access_token}
requestData = {}

with open('16k.pcm') as todos:
    for chore in todos:
        print(chore)

# response = requests.post(url, json=requestData, headers=headers)
# print(response.text)
