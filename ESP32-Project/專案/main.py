from machine import Pin, I2C
import ssd1306
import time
import menu  # 引入選單模組
import Hide_the_block  # 引入躲方塊遊戲模組
import dionsaur  # 引入 Dino Game 模組

# OLED 初始化
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# 按鈕
btn_left = Pin(36, Pin.IN, Pin.PULL_UP)
btn_right = Pin(5, Pin.IN, Pin.PULL_UP)
btn_confirm = Pin(5, Pin.IN, Pin.PULL_UP)  # 用來返回選單的按鈕

# LED 初始化
led_red = Pin(16, Pin.OUT)
led_yellow = Pin(12, Pin.OUT)
led_green = Pin(13, Pin.OUT)

# 蜂鳴器
buzzer = Pin(14, Pin.OUT)

# --- 統一執行模式框架 ---
def run_mode(title, function_to_run):
    # 顯示模式名稱
    oled.fill(0)
    oled.text(title, 0, 0)
    oled.text("Starting...", 0, 20)
    oled.show()
    time.sleep(1)

    # 執行該模式
    function_to_run()

    # 回主選單動畫
    oled.fill(0)
    oled.text(title, 0, 0)
    oled.text("Returning...", 0, 20)
    oled.show()
    time.sleep(1)

# --- 顯示選單並進行選擇 ---
def start_game():
    while True:  # 改成 while True → 回選單後可以繼續再選
        mode_index = None
        while mode_index is None:
            menu.display_menu(oled)  # 顯示選單
            mode_index = menu.change_mode()  # 監測選擇

        # 根據選擇的模式啟動遊戲
        if mode_index == 0:
            run_mode("Hide the block", lambda: Hide_the_block.start_dodge_game(
                oled, btn_left, btn_right, led_red, led_yellow, led_green, buzzer, btn_confirm))
        elif mode_index == 1:
            run_mode("MP3 Player", start_mp3_player)
        elif mode_index == 2:
            run_mode("Dinosaur", start_new_game)

# --- MP3 撥放器 ---
def start_mp3_player():
    oled.fill(0)
    oled.text("MP3 Player", 0, 0)
    oled.text("Function closed", 0, 20)
    oled.text("Please return to menu", 0, 40)
    oled.text("menu", 0, 50)
    oled.show()

    # 等待確認鍵按下
    while btn_confirm.value():  # 按下才結束
        time.sleep(0.1)

# --- 待開發遊戲 ---
def start_new_game():
    dionsaur.start_dino_game()


    # 等待確認鍵按下
    while btn_confirm.value():
        time.sleep(0.1)

# --- 主程式 ---
start_game()  # 啟動選單系統並根據選擇啟動遊戲
