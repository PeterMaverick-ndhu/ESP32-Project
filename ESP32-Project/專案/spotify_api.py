import requests
import base64

# 👉 請填入你的 Client ID 和 Secret
client_id = "25f580a36fda4419beee7500dd05fa02"
client_secret = "08d5978f2c744956955fed6ed238ba53"

# 👉 你剛剛設定的 redirect URI
redirect_uri = "https://petermaverick-ndhu.github.io/ESP32-Project/"

# 👉 剛剛從網址取得的授權碼
code = "AQCI7_qw1nd0HE_Wz6CWytoDoIaFyammr3jdaUhkhvy5KPJ6OsafDyLJzW316GnlrPe-faVFSQNp_E-m7HkRLyyMdc1Peb0U9DWuuIEoWCz3_1o2Gd8ZklU7CEX7UWiqLm21x6ti8BHgJId96D3YrNC6gPXyZ3ggaLouNfAFa9uRGXXE3tAXKvapw-ksvDYVbOiSsD2Mp5rWE__TPuVAYw_3Oh0EvaWNXApWIxMfR78stAt4RPoMDFkGjMfw0iZgKVFfGoLXrN1vjZ06Og"

# 編碼 client_id 和 client_secret 為 Base64 字串
auth_string = f"{client_id}:{client_secret}"
b64_auth = base64.b64encode(auth_string.encode()).decode()

# 設定 headers 與表單資料
headers = {
    "Authorization": f"Basic {b64_auth}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": redirect_uri
}

# 發送請求
response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

# 顯示結果
print(response.status_code)
print(response.json())
