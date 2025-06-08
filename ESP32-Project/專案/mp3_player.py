import requests
import json
from spotify_token_helper import refresh_access_token, get_saved_access_token, transfer_playback, play, pause, next_track

# 先 refresh 一次 token
refresh_access_token()

# 讀最新 access_token
access_token = get_saved_access_token()

headers = {
    "Authorization": f"Bearer {access_token.strip()}",
    "Content-Type": "application/json"
}

# 查詢 devices
response = requests.get("https://api.spotify.com/v1/me/player/devices", headers=headers)

print(response.status_code)
devices_data = response.json()
print(json.dumps(devices_data, indent=4))

# 自動挑選你手機那台 device_id
device_id = None
for device in devices_data.get("devices", []):
    if device.get("name") == "慈中小猴子":  # 這裡改成你手機 device 名稱
        device_id = device.get("id")
        break

if device_id:
    print(f"\nFound device '{device.get('name')}', device_id = {device_id}")
    
    # Transfer playback 到手機
    transfer_playback(device_id)
    
    # 播放
    play()
    
    # 暫停（你可以註解 / 取消註解）
    pause()
    
    # 下一首
    next_track()

else:
    print("\nNo matching device found.")
