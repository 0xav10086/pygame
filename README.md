# pygame
# just a life game 
# o.0
在这段代码中，有以下定义：
1.life_game(board, steps):包含了两个参数，board为一个二维数组，表示游戏开始时的初始状态；steps为要模拟的步数
2.get_neighbors(r, c):包含了两个参数，r 和 c，分别表示要计算其周围存活细胞数量的单元格的行和列
3.generate_random_board(rows, cols, steps):接受三个参数：rows, cols, 和 steps。它的目的是生成一个随机的初始网格，该网格在指定步数内不会全部死亡
4.dr和dc分别表示行和列的偏移量，用于遍历给定单元格周围的八个单元格
这段代码分为两个部分，一为根据当前状态计算下一步的状态，二为生成一个非死环境
