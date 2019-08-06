
import wave
import requests
import json
import base64
import ffmpeg

# Get Access Token
url = "https://openapi.baidu.com/oauth/2.0/token"
params = {'grant_type': 'client_credentials', 'client_id': 'QdOwB4WRNE0jZDp57hFhBHlZ',
          'client_secret': 'sU0u4I0MDNXLiF5bslR8HknjSFIkCRA0'}
r = requests.get(url, params=params)
jsonObject = json.loads(r.text)
access_token = jsonObject['access_token']

# Send Voice File
url = 'http://vop.baidu.com/server_api '
headers = {'content-type': 'application/json'}
# params = {'dev_pid': 1536, 'cuid': 'baiduyuyin', 'token': access_token}
path = "16k.wav"
with wave.open(path, "rb") as f:
    # read the wave's format infomation,and return a tuple
    params = f.getparams()
    # get the info
    nchannels, sampwidth, framerate, nframes = params[:4]
    # Reads and returns nframes of audio, as a string of bytes.
    str_bytes_data = f.readframes(nframes)
    # close the stream
    f.close()

# convert bytes string to base64 format string
speech = base64.b64encode(str_bytes_data).decode('utf-8')
requestData = {
    "format": "pcm",
    "rate": framerate,
    "dev_pid": 1536,
    "channel": nchannels,
    "token": access_token,
    "cuid": "baidu_workshop",
    "len": len(str_bytes_data),
    "speech": speech
}
response = requests.post(url, json=requestData, headers=headers)
print(response.text)


# 参考链接：https://blog.csdn.net/exmlyshy/article/details/84760845