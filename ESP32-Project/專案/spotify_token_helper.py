# spotify_token_helper.py
import requests
import base64
import json
import time

# Spotify App 設定
client_id = "25f580a36fda4419beee7500dd05fa02"
client_secret = "08d5978f2c744956955fed6ed238ba53"
token_file = "token.json"

# 自動 refresh token 並取得最新 access_token
def refresh_access_token():
    with open(token_file, "r") as f:
        token_data = json.load(f)
    refresh_token = token_data["refresh_token"]

    auth_string = f"{client_id}:{client_secret}"
    b64_auth = base64.b64encode(auth_string.encode()).decode()

    headers = {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }

    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

    if response.status_code == 200:
        new_token_data = response.json()
        access_token = new_token_data["access_token"]

        # 更新 token.json
        token_data["access_token"] = access_token
        if "refresh_token" in new_token_data:
            token_data["refresh_token"] = new_token_data["refresh_token"]

        with open(token_file, "w") as f:
            json.dump(token_data, f, indent=4)

        print("Access token refreshed.")
        print(f"Access token now: {access_token}")

        return access_token
    else:
        print(f"Error refreshing token: {response.status_code} {response.text}")
        return None

# 提供一個簡單函式，讓其他程式可以讀最新的 access_token
def get_saved_access_token():
    with open(token_file, "r") as f:
        token_data = json.load(f)
    return token_data.get("access_token")

def transfer_playback(device_id):
    access_token = get_saved_access_token()

    headers = {
        "Authorization": f"Bearer {access_token.strip()}",
        "Content-Type": "application/json"
    }

    transfer_data = {
        "device_ids": [device_id],
        "play": True
    }

    response = requests.put("https://api.spotify.com/v1/me/player", headers=headers, json=transfer_data)

    print(f"Transfer playback status: {response.status_code}")
    print(response.text)

def play():
    access_token = get_saved_access_token()

    headers = {
        "Authorization": f"Bearer {access_token.strip()}",
        "Content-Type": "application/json"
    }

    response = requests.put("https://api.spotify.com/v1/me/player/play", headers=headers)
    print(f"Play status: {response.status_code}")
    print(response.text)

def pause():
    access_token = get_saved_access_token()

    headers = {
        "Authorization": f"Bearer {access_token.strip()}",
        "Content-Type": "application/json"
    }

    response = requests.put("https://api.spotify.com/v1/me/player/pause", headers=headers)
    print(f"Pause status: {response.status_code}")
    print(response.text)

def next_track():
    access_token = get_saved_access_token()

    headers = {
        "Authorization": f"Bearer {access_token.strip()}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://api.spotify.com/v1/me/player/next", headers=headers)
    print(f"Next track status: {response.status_code}")
    print(response.text)
