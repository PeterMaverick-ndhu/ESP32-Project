from machine import Pin
import time

# 按鈕
btn_up = Pin(36, Pin.IN, Pin.PULL_UP)
btn_confirm = Pin(5, Pin.IN, Pin.PULL_UP)

# 模式列表
modes = ["Hide the block", "MP3 player", "Dinosaur"] 
mode_index = 0  # 初始選擇第一個模式

# 顯示選單
def display_menu(oled):
    oled.fill(0)
    oled.text("Please Select", 0, 0)
    for i, mode in enumerate(modes):
        if i == mode_index:
            oled.text("> " + mode, 0, 16 + i*10)  # 游標指示當前選項
        else:
            oled.text(mode, 0, 16 + i*10)
    oled.show()

# 改變選擇的模式
def change_mode():
    global mode_index
    if not btn_up.value():
        mode_index = (mode_index + 1) % len(modes)  # 向上移動，循環選擇
        time.sleep(0.2)  # 防止按鈕彈跳
    if not btn_confirm.value():
        return mode_index
    return None
