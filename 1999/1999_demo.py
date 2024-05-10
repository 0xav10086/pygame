'''
本段代码已经可以成功运行1999并自动获取微尘，
但没有实现结构化，将在V1更新
'''


# 导入相关库
import pyautogui
import time

# 获取游戏图标位置
location = pyautogui.locateCenterOnScreen('/home/oxav10086/PycharmProjects/pygame/1999/dataset/Software _charts.png')

# 模拟鼠标打开程序
pyautogui.moveTo(location)
pyautogui.doubleClick()

# 等待一段时间
time.sleep(10)
pyautogui.press('F7')
print("已模拟按下 F7 键！")

# 进入初始界面
time.sleep(30)
# 判断游戏是否启动
'''
start = pyautogui.locateCenterOnScreen('/home/oxav10086/PycharmProjects/pygame/1999/dataset/start.png')
pyautogui.moveTo(start)
pyautogui.click()
print(start)
'''

pyautogui.moveTo(1920/2, 1080/2)
pyautogui.click()
time.sleep(20)

# 入场
enter = pyautogui.locateCenterOnScreen('/home/oxav10086/PycharmProjects/pygame/1999/dataset/enter.png')
pyautogui.moveTo(enter)
pyautogui.click()
time.sleep(5)
print(enter)

# 进入资源
# resource = pyautogui.locateCenterOnScreen('/home/oxav10086/PycharmProjects/pygame/1999/dataset/enter.png')
# pyautogui.moveTo(resource)
pyautogui.moveTo(700, 960)
pyautogui.click()
time.sleep(5)

# 尘埃运动
'''
dust = pyautogui.locateCenterOnScreen('/home/oxav10086/PycharmProjects/pygame/1999/dataset/dust.png')
pyautogui.moveTo(dust)
pyautogui.click()
time.sleep(5)
dust6 = pyautogui.locateCenterOnScreen('/home/oxav10086/PycharmProjects/pygame/1999/dataset/Dust_movement.png')
pyautogui.moveTo(dust6)
pyautogui.click()
'''
# 进入尘埃运动
time.sleep(6)
pyautogui.moveTo(1325,575)
pyautogui.click()

# 点击尘埃运动6
time.sleep(2)
pyautogui.moveTo(670,900)
pyautogui.click()

# 点击开始游戏
time.sleep(2)
pyautogui.moveTo(1720,920)
pyautogui.click()

# 开始复现
time.sleep(5)
pyautogui.moveTo(1650,1000)
pyautogui.click()