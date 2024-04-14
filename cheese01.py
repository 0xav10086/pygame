import turtle #引入turtle库
n = 60  # 方块大小
x = -300   #  x初始值，可以根据自己需要进行设置
y = -300   #  y初始值
turtle.speed(5)#绘制速度
turtle.pensize(2)#画笔宽度

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


