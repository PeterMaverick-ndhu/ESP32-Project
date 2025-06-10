# ESP32-Project

此檔案為 "創客入門" 課程之檔案，資料內容如下：

## 專案結構

ESP32-Project/  
├── README.md # 這份說明檔  
├── callback.html # 處理 Spotify OAuth 授權回調的 HTML 頁面  
└── ESP32-Project/ # 主要專案資料夾  
    ├── pycache/ # 儲存編譯後的 .pyc 檔案  
    │ └── spotify_token_helper.cpython-311.pyc # 用來處理 Spotify token  
    ├── Hide_the_block.py # 小遊戲 - 躲避掉落方塊  
    ├── Spotify_play.py # 播放 Spotify 音樂  
    ├── autoassign.py # 自動從 Spotify 獲取新 token  
    ├── dinosaur.py # 小遊戲 - 恐龍跳方塊  
    ├── main.py # 主程式 - 整合各部分程式  
    ├── menu.py # OLED 顯示螢幕的選單  
    ├── mp3_player.py # 播放 Spotify 音樂（需結合手機及 Spotify Premium）  
    ├── spotify_api.py # 用來呼叫 Spotify API 的程式  
    ├── spotify_api.txt # 存放 Spotify 授權碼的暫存檔案（已過期）  
    ├── spotify_token_helper.py # 用來處理 Spotify token 的腳本  
    ├── ssd1306.py # OLED 顯示用程式  
    ├── token.json # Spotify token（已過期）  


## 使用說明

### 步驟 1: Spotify 授權

1. 設定 **`spotify_token_helper.py`** 中的 `client_id` 和 `client_secret`。
2. 運行 **`autoassign.py`** 來獲取授權碼（authorization code）。
3. 使用授權碼，通過 **`spotify_token_helper.py`** 來獲得 `access_token` 和 `refresh_token`。

### 步驟 2: 播放 Spotify 音樂

1. 在 **`mp3_player.py`** 中使用已獲得的 `access_token` 控制 Spotify 播放音樂。
2. 音樂播放功能需要 **Spotify Premium** 帳號。

### 步驟 3: 玩遊戲

1. 使用 **`Hide_the_block.py`** 和 **`dinosaur.py`** 來玩遊戲，這些遊戲會顯示在 OLED 屏幕上。

### 步驟 4: 回到主選單

1. 按下返回鍵即可回到主選單。

## 注意事項

- 你需要 **Spotify Premium** 才能使用 **`mp3_player.py`** 播放音樂。
- **`token.json`** 會儲存從 Spotify 獲得的 token，記得定期刷新 token。
- 如果 **`token.json`** 過期，請運行 **`autoassign.py`** 來獲取新的 token。

## 其他

- **`callback.html`** 用來處理 Spotify 的授權回調並顯示授權碼，請確認在 Spotify 授權後，回到此頁面來捕捉授權碼。

