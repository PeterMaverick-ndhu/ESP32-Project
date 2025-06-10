from machine import Pin, I2C
import ssd1306
import time
import random

# OLED 初始化
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# 按鈕設定
btn_jump = Pin(36, Pin.IN, Pin.PULL_UP)  # 用來跳躍的按鈕（GPIO36）

# 恐龍位置
dino_x = 10
dino_y = 50
dino_vy = 0  # 垂直速度
gravity = 3  # 重力
jump_strength = -12  # 跳躍時給一個負速度
ground_y = 50  # 地面高度

# 障礙物設定
obstacles = []  # [(x, y), ...]
obstacle_speed = 20  # 障礙物速度
obstacle_cooldown = 0  # 兩個障礙物之間的冷卻時間（frame 數）

# 分數
score = 0

# 畫畫面
def draw():
    oled.fill(0)
    oled.fill_rect(dino_x, int(dino_y), 10, 10, 1)  # 恐龍
    for ox, oy in obstacles:
        oled.fill_rect(ox, oy, 10, 10, 1)  # 障礙物
    oled.text(f"Score: {score}", 0, 0)
    oled.show()

# 更新恐龍狀態
def update_dino():
    global dino_y, dino_vy
    dino_y += dino_vy
    dino_vy += gravity

    # 不要低於地面
    if dino_y > ground_y:
        dino_y = ground_y
        dino_vy = 0

# 移動障礙物
def move_obstacles():
    global obstacles, obstacle_cooldown
    new_obstacles = []
    for ox, oy in obstacles:
        ox -= obstacle_speed
        if ox > -10:  # 還沒超出畫面左邊
            new_obstacles.append((ox, oy))
    obstacles.clear()
    obstacles.extend(new_obstacles)

    # 更新 cooldown
    if obstacle_cooldown > 0:
        obstacle_cooldown -= 1

    # 隨機生成障礙物，需 cooldown 完成才能出新障礙物
    if obstacle_cooldown == 0 and random.random() < 0.05:
        obstacles.append((128, ground_y))
        obstacle_cooldown = random.randint(20, 40)  # 20~40 frame 才能出下一個障礙物

# 檢查碰撞
def check_collision_with_obstacle():
    for ox, oy in obstacles:
        if ox < dino_x + 10 and ox + 10 > dino_x and oy < dino_y + 10 and oy + 10 > dino_y:
            return True
    return False

# 主遊戲循環
def start_dino_game():
    global score, dino_y, dino_vy, obstacles, obstacle_cooldown
    # 初始化
    dino_y = ground_y
    dino_vy = 0
    obstacles = []
    obstacle_cooldown = 0
    score = 0

    oled.fill(0)
    oled.text("Dino Game!", 0, 0)
    oled.text("Press B Jump", 0, 20)
    oled.show()
    time.sleep(1)

    while True:
        # 按下跳躍按鈕
        if not btn_jump.value():
            if dino_y >= ground_y:  # 只能在地面跳
                dino_vy = jump_strength

        # 更新狀態
        update_dino()
        move_obstacles()

        # 檢查碰撞
        if check_collision_with_obstacle():
            oled.fill(0)
            oled.text("GAME OVER", 25, 20)
            oled.text(f"Score: {score}", 25, 40)
            oled.show()
            time.sleep(2)
            break  # 回主選單

        # 畫畫面
        draw()

        # 更新分數
        score += 1
        time.sleep(0.05)  # 控制速度

