import requests
import base64
import json

# Spotify app 資訊
client_id = "25f580a36fda4419beee7500dd05fa02"
client_secret = "08d5978f2c744956955fed6ed238ba53"  # <== 記得改這裡！
redirect_uri = "https://petermaverick-ndhu.github.io/ESP32-Project/"

# 你剛剛提供的 code
code = "AQCZK3EGkWEI5LszzWzJ6GJUmZujcQunycpdLciV3FFIfNspXTXqSD_ntdRa665S5haxgG4M1Xl6PIHpzqzwF1rcVgzQAdqTIzd0Be121HggAbCB9IdTjVS8saTRdeh5rmK2cdblPcCdoWyu5joKw49C1trfY7wv3bTGlcYaxR2J3TKcKl8xiLiJMZMkTOJQ4ymkPwkNQgLdN2cZmVJtzopAyrWDp30xCfs0CKHdN8q91zRAiKM6g9OkF_DzC0qs-6sM9vg_xXwsl42JVA"

# 編碼 client_id:client_secret 成 base64
auth_string = f"{client_id}:{client_secret}"
b64_auth = base64.b64encode(auth_string.encode()).decode()

# 設定 headers
headers = {
    "Authorization": f"Basic {b64_auth}",
    "Content-Type": "application/x-www-form-urlencoded"
}

# 設定資料
data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": redirect_uri
}

# 發送請求
response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

# 解析結果
if response.status_code == 200:
    token_info = response.json()
    access_token = token_info["access_token"]
    refresh_token = token_info["refresh_token"]

    print(f"Access Token: {access_token}")
    print(f"Refresh Token: {refresh_token}")

    # 把 token 存到檔案，之後自動 refresh 用
    with open("token.json", "w") as f:
        json.dump(token_info, f, indent=4)

    print("Token 已儲存到 token.json，之後可以自動 refresh！")
else:
    print(f"Error: {response.status_code} {response.text}")
