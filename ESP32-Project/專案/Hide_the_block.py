from machine import Pin, I2C
import ssd1306
import time
import random
import sys

# 躲方塊小遊戲的邏輯，將所需的硬體引腳作為參數傳遞進來
def start_dodge_game(oled, btn_left, btn_right, led_red, led_yellow, led_green, buzzer, btn_confirm):
    try:
        # 初始化遊戲變數
        player_x = 2
        player_y = 6
        obstacles = []      # [(x, y), ...]
        score = 0
        hp = 3
        speed = 0.5

        # 更新 LED 顯示
        def update_led():
            if hp >= 3:
                led_green.value(1)
                led_yellow.value(1)
                led_red.value(1)
            elif hp == 2:
                led_green.value(0)
                led_yellow.value(1)
                led_red.value(1)
            elif hp == 1:
                led_green.value(0)
                led_yellow.value(0)
                led_red.value(1)
            else:
                led_green.value(0)
                led_yellow.value(0)
                led_red.value(0)

        # 畫面更新
        def draw():
            oled.fill(0)
            oled.text("Score:{}".format(score), 0, 0)
            oled.text("HP:{}".format('*'*hp), 70, 0)
            oled.fill_rect(player_x*10, player_y*10, 10, 10, 1)  # 玩家
            for ox, oy in obstacles:
                oled.fill_rect(ox*10, oy*10, 10, 10, 1)           # 障礙物
            oled.show()

        # 更新障礙物狀態
        def update_obstacles():
            nonlocal hp
            new_obs = []
            for ox, oy in obstacles:
                oy += 1
                if oy == player_y and ox == player_x:
                    hp -= 1
                    led_red.value(1)
                    buzzer.value(1)
                    time.sleep(0.2)
                    led_red.value(0)
                    buzzer.value(0)
                    update_led()
                elif oy < 7:
                    new_obs.append((ox, oy))
            obstacles.clear()
            obstacles.extend(new_obs)
            if random.random() < 0.3:
                obstacles.append((random.randint(0, 11), 0))

        update_led()
        loop_count = 0
        while True:
            if not btn_left.value() and player_x > 0:
                player_x -= 1
            if not btn_right.value() and player_x < 11:
                player_x += 1

            if loop_count % 5 == 0:
                update_obstacles()
                draw()
                score += 1

            loop_count += 1
            time.sleep(0.02)

            if hp <= 0:
                oled.fill(0)
                oled.text("GAME OVER", 25, 20)
                oled.text("Score:{}".format(score), 25, 40)
                oled.show()
                update_led()

                # 等待 5 秒後自動返回選單
                time.sleep(3)

                # 清空顯示並顯示返回訊息
                oled.fill(0)  # 清空顯示
                oled.text("Returning...", 0, 0)
                oled.show()
                time.sleep(1)

                # 跳回選單
                return  # 直接返回 start_game() 並重新啟動選單

    except Exception as e:
        sys.print_exception(e)
