# ESP32-Project

此檔案為 "創客入門" 課程之檔案，資料內容如下：

## 專案結構

- **_pycache_**: 存放已編譯的 `.pyc` 檔案。
  - `spotify_token_helper.cpython-311.pyc`: 用於 MP3 播放器功能（Spotify），此檔案用來從 Spotify 獲取 token。
  
- **Hide_the_block.py**: 小遊戲 - 躲避掉落方塊。

- **Spotify_play.py**: Spotify 撥放用程式，負責控制音樂播放。

- **autoassign.py**: 用於自動從 Spotify 獲取新 token 的腳本。

- **dinosaur.py**: 小遊戲 - 恐龍跳方塊。

- **main.py**: 主程式 - 整合各部分功能。

- **menu.py**: 選單功能 - 用於在 OLED 顯示螢幕上顯示選單。

- **mp3_player.py**: 小程式 - 用於播放 Spotify 音樂（需結合手機及 Spotify Premium）。

- **spotify_api.py**: 用來呼叫 Spotify API 的程式。

- **spotify_api.txt**: 存放 Spotify 授權碼的暫存檔案（已過期）。

- **spotify_token_helper.py**: 用來處理 Spotify token 的腳本。

- **ssd1306.py**: 用於 OLED 顯示的程式。

- **token.json**: 存放 Spotify token（已過期）。

- **callback.html**: 處理 Spotify OAuth 授權回調（Callback）的 HTML 頁面。

## 使用說明

### 步驟 1: Spotify 授權
1. 設定 `spotify_token_helper.py` 中的 `client_id` 和 `client_secret`，並運行 `autoassign.py` 來獲取授權碼。
2. 使用授權碼透過 `spotify_token_helper.py` 來獲得 `access_token` 和 `refresh_token`。

### 步驟 2: 播放 Spotify 音樂
1. 在 `mp3_player.py` 中使用已獲得的 `access_token` 控制 Spotify 播放音樂。
2. 可以通過按鈕控制播放、暫停、切換歌曲等功能。

### 步驟 3: 玩遊戲
1. 使用 `Hide_the_block.py` 和 `dinosaur.py` 來玩遊戲，這些遊戲會顯示在 OLED 屏幕上。

## 注意事項

- 你需要 **Spotify Premium** 才能使用 `mp3_player.py` 播放音樂。
- `token.json` 會儲存從 Spotify 獲得的 token，記得定期刷新 token。
- 如果 `token.json` 過期，請運行 `autoassign.py` 來獲取新的 token。

## 其他
- 如果想要更深入了解 OAuth 流程，請參考 `callback.html`，它會處理 Spotify 的授權回調並顯示授權碼。
