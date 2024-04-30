import pyautogui
import time
import sys
import subprocess

# 启动游戏

# 获取游戏图标位置,确保游戏图标在可见的位置
try:
    location = pyautogui.locateCenterOnScreen('./img/softwareCharts.png', confidence=0.6)
    # 模拟鼠标打开程序
    pyautogui.moveTo(location)
    pyautogui.doubleClick()
except pyautogui.ImageNotFoundException:
    print('游戏图标未找到，请检查图片路径是否正确。')
    sys.exit()  # 遇到错误时退出程序


# 全屏
def full_screen(shenlan_image):
    for i in range(4):
        try:
            main = pyautogui.locateCenterOnScreen(shenlan_image, confidence=0.7)
            if main:
                pyautogui.press('F7')
                print('已全屏！')
                break
        except OSError:  # 捕获OSError异常
            print('因为图片未找到，所以深蓝离开了你。')
            sys.exit()  # 遇到错误时退出程序
        except Exception as e:  # 捕获其他所有异常
            print(f'第{i+1}次尝试未检测到图片，等待3秒后重试。错误信息: {e}')
            sys.exit()  # 遇到错误时退出程序
        time.sleep(3)
    else:
        print("深蓝没有你我怎么活啊！？")
        sys.exit()  # 循环结束后如果未成功全屏，退出程序


full_screen(r'./img/bluePoch.png')


# 检测当前界面是否有start按钮
def check_and_click(start_image1, start_image2):
    for i in range(5):  # 设置循环次数为5
        try:
            main1 = pyautogui.locateCenterOnScreen(start_image1, confidence=0.7)
            main2 = pyautogui.locateCenterOnScreen(start_image2, confidence=0.7)
            if main1 and main2:
                x, y = 0, 0  # 避免鼠标指针对图像识别造成影响
                pyautogui.click(x, y)
                print('游戏开始，程序启动！')
                print(main1, main2)
                break  # 如果找到图片，点击后退出循环
        except pyautogui.ImageNotFoundException:
            print(f'第{i+1}次未检测到图片，等待3秒后重试。')
            sys.exit()  # 遇到错误时退出程序
        time.sleep(3)  # 每次循环结束后等待3秒
    else:
        print('耶？我开始键呢？')  # 循环5次后如果仍未检测到图片，退出程序
        sys.exit()


check_and_click('./img/12.png', './img/log_out.png')


# 使用subprocess模块运行1999V1.py文件
subprocess.run(['python', '1999V1_check.py'])