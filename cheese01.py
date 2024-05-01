import pygame

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
PINK = (255, 192, 203)

# 棋盘设置
board_size = 8
square_size = 800 // board_size
piece_size = square_size // 2  # 棋子大小
# 挡板大小
barrier_width = square_size * 2
barrier_height = square_size // 2

# 棋子和挡板的初始位置
pieces = {'blue': (0, 0), 'red': (7, 7)}
barriers = []

# 可移动位置标记
movable_positions = []

# 按钮设置
button_font = pygame.font.SysFont('Arial', 24)
move_button = pygame.Rect(100, height - 100, 200, 50)
barrier_button = pygame.Rect(500, height - 100, 200, 50)

# 回合设置
current_player = 'blue'  # 当前回合的玩家
player_turn_rect = pygame.Rect(300, height - 100, 200, 50)

# 游戏主循环
running = True
placing_barrier = False
barrier_orientation = 'horizontal'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # 检查是否点击了“放置挡板”按钮
            if barrier_button.collidepoint(mouse_pos):
                placing_barrier = not placing_barrier  # 切换放置挡板模式
                barrier_orientation = 'horizontal' if barrier_orientation == 'vertical' else 'vertical'
            # 如果正在放置挡板
            if placing_barrier:
                # 计算挡板位置
                col = mouse_pos[0] // square_size
                row = mouse_pos[1] // square_size
                barrier_rect = pygame.Rect(col * square_size, row * square_size, barrier_width
                if barrier_orientation == 'horizontal' else square_size, barrier_height if barrier_orientation == 'vertical' else square_size)
                # 检查挡板位置是否有效
                if (not any(barrier_rect.colliderect(pygame.Rect(b[0], b[1], barrier_width
                if b[2] == 'horizontal' else square_size, barrier_height if b[2] == 'vertical' else square_size))
                           for b in barriers) and not barrier_rect.colliderect(pygame.Rect(pieces['blue'][1] * square_size, pieces['blue'][0] * square_size, square_size, square_size))
                        and not barrier_rect.colliderect(pygame.Rect(pieces['red'][1] * square_size, pieces['red'][0] * square_size, square_size, square_size))):
                    barriers.append((barrier_rect.x, barrier_rect.y, barrier_orientation))
                    placing_barrier = False  # 停止放置挡板

            # 检查是否点击了“移动棋子”按钮
            if move_button.collidepoint(mouse_pos):
                print("移动棋子按钮被点击")
                # 获取当前玩家的棋子位置
                piece_pos = pieces[current_player]
                # 标记可移动位置

                movable_positions = [(piece_pos[0] + dx, piece_pos[1])
                                     for dx in (-1, 1) if 0 <= piece_pos[0] + dx < board_size] + \
                                    [(piece_pos[0], piece_pos[1] + dy)
                                     for dy in (-1, 1) if 0 <= piece_pos[1] + dy < board_size]

            # 检查是否点击了可移动位置
            for pos in movable_positions:
                if pygame.Rect(pos[1] * square_size, pos[0] * square_size, square_size, square_size).collidepoint(mouse_pos):
                    # 移动棋子到新位置
                    pieces[current_player] = pos
                    # 清除可移动位置标记
                    movable_positions = []
                    # 切换玩家回合
                    current_player = 'red' if current_player == 'blue' else 'blue'
                    break

    # 绘制棋盘
    screen.fill(BLACK)
    for row in range(board_size):
        for col in range(row % 2, board_size, 2):
            rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
            pygame.draw.rect(screen, RED if (row, col) in pieces.values() else WHITE, rect)
            # 如果是可移动位置，则绘制绿色
            if (row, col) in movable_positions:
                pygame.draw.rect(screen, GREEN, rect)

    # 在这里绘制绿色的可移动位置
    for pos in movable_positions:
        rect = pygame.Rect(pos[1] * square_size, pos[0] * square_size, square_size, square_size)
        pygame.draw.rect(screen, GREEN, rect)

    # 绘制棋子
    for color, position in pieces.items():
        pygame.draw.circle(screen, RED if color == 'red' else BLUE,
                           (position[1] * square_size + piece_size, position[0] * square_size + piece_size), piece_size)

    # 绘制挡板
    for barrier in barriers:
        pygame.draw.rect(screen, GREEN, barrier)

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
