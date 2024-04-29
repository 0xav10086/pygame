import pyautogui
import time

# 启动游戏

# 获取游戏图标位置
try:
    location = pyautogui.locateCenterOnScreen('/home/oxav10086/PycharmProjects/pygame/1999/img/softwareCharts.png',
                                              confidence=0.90)
    # 模拟鼠标打开程序
    pyautogui.moveTo(location)
    pyautogui.doubleClick()
except pyautogui.ImageNotFoundException:
    print('游戏图标未找到，请检查图片路径是否正确。')


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
            break  # 如果图片未找到，跳出循环
        except Exception as e:  # 捕获其他所有异常
            print(f'第{i+1}次尝试未检测到图片，等待3秒后重试。错误信息: {e}')
        time.sleep(3)
    else:
        print("深蓝没有你我怎么活啊！？")


full_screen(r'/home/oxav10086/PycharmProjects/pygame/1999/img/bluePoch.png')


# 检测当前界面是否有start按钮
def check_and_click(start_image1, start_image2):
    for i in range(5):  # 设置循环次数为5
        try:
            main1 = pyautogui.locateCenterOnScreen(start_image1, confidence=0.7)
            main2 = pyautogui.locateCenterOnScreen(start_image2, confidence=0.7)
            if main1 and main2:
                x, y = 1920 / 2, 1080 / 2  # 使用locateCenterOnScreen返回的坐标
                pyautogui.click(x, y)
                print('游戏开始，程序启动！')
                print(main1, main2)
                break  # 如果找到图片，点击后退出循环
        except pyautogui.ImageNotFoundException:
            print(f'第{i+1}次未检测到图片，等待3秒后重试。')
        time.sleep(3)  # 每次循环结束后等待3秒
    else:
        print('耶？我开始键呢？')  # 循环5次后如果仍未检测到图片，打印提示


check_and_click('/home/oxav10086/PycharmProjects/pygame/1999/img/12.png',
                '/home/oxav10086/PycharmProjects/pygame/1999/img/log_out.png')

# 签到以及生日
for i in range(3):
    pyautogui.moveTo(1260, 550)
    pyautogui.click()
    time.sleep(2)
