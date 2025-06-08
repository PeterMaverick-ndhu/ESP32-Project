import requests
from spotify_token_helper import get_access_token

access_token = get_access_token()

headers = {
    "Authorization": f"Bearer {access_token}"
}

# 播放
response = requests.put("https://api.spotify.com/v1/me/player/play", headers=headers)
print(f"Play: {response.status_code}")

# 暫停
# response = requests.put("https://api.spotify.com/v1/me/player/pause", headers=headers)
# print(f"Pause: {response.status_code}")

# 下一首
# response = requests.post("https://api.spotify.com/v1/me/player/next", headers=headers)
# print(f"Next: {response.status_code}")
