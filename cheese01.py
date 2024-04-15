import turtle  # 引入turtle库
import matplotlib.pyplot as plt
import numpy as np
import pygame
'''
n = 60  # 方块大小
x = -300   # x初始值，可以根据自己需要进行设置
y = -300   # y初始值
turtle.speed(0)  # 绘制速度
turtle.pensize(2)  # 画笔宽度

# 画出8行8列的黑白棋盘
for i in range(8):  # 默认从0开始，01234567
    for j in range(1, 9):  # 12345678
        turtle.penup()  # 抬起画笔进行移动
        turtle.goto(x + i * n, y + j * n)
        turtle.pendown()  # 落下画笔开始绘制
        if (i + j) % 2 == 1:  # 绘制白块
            for index in range(4):
                turtle.forward(n)  # 依次绘制方块的四边的长度
                turtle.left(90)  # 逆时针旋转90度
        elif (i + j) % 2 == 0:  # 涂黑绘制黑块
            turtle.begin_fill()  # 开始填充
            turtle.fillcolor('black')
            for index in range(4):
                turtle.forward(n)
                turtle.left(90)
            turtle.end_fill()

turtle.penup()
turtle.goto(-320, -260)  # 回到开始绘制的起点的左下方进行外围框的绘制
turtle.pendown()
# 开始绘制最外面的框
for index in range(4):
    turtle.forward(520)
    turtle.left(90)
# 开始书写左边的数字
for s in range(1, 9):
    turtle.penup()
    turtle.goto(-330, -210 + (s - 1) * 60)  # 固定x轴的位置，y轴的值根据位置变化
    turtle.pendown()
    turtle.write(s)
    turtle.forward(5)
# 开始书写下方的字母
for s in range(8):
    turtle.penup()
    turtle.goto(-270 + s * 60, -260)
    turtle.pendown()
    turtle.write(chr(65 + s))
    turtle.forward(5)
'''
'''
def draw_chessboard():
    chessboard = np.zeros((8, 8))
    chessboard[1::2, ::2] = 1
    chessboard[::2, 1::2] = 1

    plt.imshow(chessboard, cmap='gray')
    plt.show()

draw_chessboard()
'''
# 初始化pygame
pygame.init()

# 设置窗口大小
width, height = 800, 900
screen = pygame.display.set_mode((width, height))

# 定义颜色
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# 棋盘设置
board_size = 8
square_size = 800 // board_size
piece_size = square_size // 2  # 棋子大小
barrier_size = (square_size * 2, square_size)  # 挡板大小

# 棋子和挡板的初始位置
pieces = {'blue': (0, 0), 'red': (7, 7)}
barriers = []

# 按钮设置
button_font = pygame.font.SysFont('Arial', 24)
move_button = pygame.Rect(100, height - 100, 200, 50)
barrier_button = pygame.Rect(500, height - 100, 200, 50)

# 回合设置
current_player = 'blue'  # 当前回合的玩家
player_turn_rect = pygame.Rect(300, height - 100, 200, 50)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # 检查是否点击了“移动棋子”按钮
            if move_button.collidepoint(mouse_pos):
                print("移动棋子按钮被点击")
                # 这里添加移动棋子的代码
                # 切换玩家回合
                current_player = 'red' if current_player == 'blue' else 'blue'
            # 检查是否点击了“放置挡板”按钮
            elif barrier_button.collidepoint(mouse_pos):
                print("放置挡板按钮被点击")
                # 这里添加放置挡板的代码
                # 切换玩家回合
                current_player = 'red' if current_player == 'blue' else 'blue'

    # 绘制棋盘
    screen.fill(BLACK)
    for row in range(board_size):
        for col in range(row % 2, board_size, 2):
            pygame.draw.rect(screen, RED if (row, col) in pieces.values() else WHITE,
                             (col * square_size, row * square_size, square_size, square_size))

    # 绘制棋子
    for color, position in pieces.items():
        pygame.draw.circle(screen, RED if color == 'red' else BLUE,
                           (position[1] * square_size + piece_size, position[0] * square_size + piece_size), piece_size)

    # 绘制挡板
    for barrier in barriers:
        pygame.draw.rect(screen, BLACK, barrier)

    # 绘制按钮
    pygame.draw.rect(screen, WHITE, move_button)
    pygame.draw.rect(screen, WHITE, barrier_button)
    screen.blit(button_font.render('MoveCheese', True, BLACK), (move_button.x + 20, move_button.y + 10))
    screen.blit(button_font.render('PutBarrier', True, BLACK), (barrier_button.x + 20, barrier_button.y + 10))

    # 绘制当前回合
    pygame.draw.rect(screen, BLACK if current_player == 'blue' else WHITE, player_turn_rect)
    turn_text = 'Blue Turn' if current_player == 'blue' else 'Red Turn'
    screen.blit(button_font.render(turn_text, True, WHITE if current_player == 'blue' else BLACK),
                (player_turn_rect.x + 20, player_turn_rect.y + 10))

    # 更新屏幕显示
    pygame.display.flip()

# 退出pygame
pygame.quit()

