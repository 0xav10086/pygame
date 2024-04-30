import pyautogui
import time
import mss
import mss.tools


def getThing(objectImg):
    for i in range(4):
        try:
            image = pyautogui.locateCenterOnScreen(objectImg, confidence=0.8)
            if image:
                pyautogui.moveTo(image[0], image[1])
                pyautogui.click()
                print('已经签到了')
                return True  # 如果找到图片，返回True
        except pyautogui.ImageNotFoundException:
            print(f'第{i + 1}次未检测到图片，等待3秒后重试。')
            time.sleep(3)  # 等待3秒
            continue  # 继续下一次尝试
    else:
        # 如果在尝试后仍未找到图片，则获取主显示器的分辨率并移动鼠标
        with mss.mss() as sct:
            monitor_number = 1
            mon = sct.monitors[monitor_number]
            mon_width = mon["width"]
            mon_height = mon["height"]
            pyautogui.moveTo(mon_width / 2, mon_height / 2)
            pyautogui.click()
            print('已经签到过了呀')
        return False  # 如果没有找到图片，返回False


def birthday(image):
    found = getThing(image)  # 首先尝试找到生日图片并点击
    if not found:
        # 如果没有找到生日图片，移动鼠标到屏幕底部的10%位置并点击
        with mss.mss() as sct:
            monitor_number = 1
            mon = sct.monitors[monitor_number]
            mon_width = mon["width"]
            mon_height = mon["height"]
            pyautogui.moveTo(mon_width / 2, mon_height - mon_height / 10)
            pyautogui.click()
            print('今天没有人过生日:(')

# 调用birthday函数
birthday('./img/birthday.png')
# 调用getThing函数
getThing('./img/obtained.png')


def wildegness(reward):
    for i in range(2):
        try:
            img = pyautogui.locateCenterOnScreen(reward, confidence=0.8)
            if img:
                pyautogui.moveTo(img[0], img[1])
                pyautogui.click()
                print('不休荒原，启动！')
                return True
        except pyautogui.ImageNotFoundException:
            print('原来已经启动了')
    else:
        return False


wildegness('./img/wildegness.png')


def getWildegness(image1, image2, image3):
    max_attempts = 10  # 增加尝试次数
    for i in range(max_attempts):
        try:
            img1 = pyautogui.locateCenterOnScreen(image1, confidence=0.6)
            img2 = pyautogui.locateCenterOnScreen(image2, confidence=0.6)
            img3 = pyautogui.locateCenterOnScreen(image3, confidence=0.6)
            if img1:
                pyautogui.moveTo(img1[0], img1[1])
                pyautogui.click()
                time.sleep(0.5)  # 短暂等待
            if img2:
                pyautogui.moveTo(img2[0], img2[1])
                pyautogui.click()
                time.sleep(0.5)
            if img3:
                pyautogui.moveTo(img3[0], img3[1])
                pyautogui.click()
                time.sleep(0.5)
            return True
        except pyautogui.ImageNotFoundException:
            print(f'第{i + 1}次未检测到图片，等待0.5秒后重试。')
            time.sleep(0.5)  # 等待0.5秒
    else:
        print('看来荒原没有什么要事')
        return False


getWildegness('./img/weichen.png', './img/lici.png', './img/friends.png')