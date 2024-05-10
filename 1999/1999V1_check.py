import pyautogui
import time
import mss
import mss.tools
import os
import tempfile
import subprocess


class Automation:
    @staticmethod
    def small_back(img):
        # 尝试定位图像
        location = pyautogui.locateCenterOnScreen(img, confidence=0.8)
        if location:
            pyautogui.moveTo(location)
            pyautogui.click()
            print('点了一下返回键')
        else:
            print('未找到返回键的图像')

    @staticmethod
    def big_back(img):
        # 尝试定位图像
        location = pyautogui.locateCenterOnScreen(img, confidence=0.8)
        if location:
            pyautogui.moveTo(location)
            pyautogui.click()
            print('返回主页')
        else:
            print('未找到返回主页键的图像')


# 用于签到
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

# 用于领取生日礼物，如果有的话
def birthday(image):
    found = getThing(image)  # 首先尝试找到生日图片并点击
    if not found:
        # 如果没有找到生日图片，移动鼠标到屏幕底部的10%位置并点击
        with mss.mss() as sct:
            monitor_number = 1
            mon = sct.monitors[monitor_number]
            mon_width = mon["width"]
            mon_height = mon["height"]
            pyautogui.moveTo(mon_height / 2, mon_width - mon_width / 10)
            pyautogui.click()
            time.sleep(2)
            print('今天没有人过生日:(')

# 调用birthday函数
birthday('./dataset/birthday.png')
# 调用getThing函数
getThing('./dataset/obtained.png')


# 用于进入荒原
def capture_screen_area():
    with mss.mss() as sct:
        # 获取第一个显示器的信息
        monitor = sct.monitors[1]

        # 计算捕获区域的像素值
        left = monitor["width"] * 72 // 100
        top = monitor["height"] * 50 // 100
        width = monitor["width"] * 85 // 100 - left
        height = monitor["height"] * 63 // 100 - top

        # 定义捕获区域
        capture_area = {
            "top": top,
            "left": left,
            "width": width,
            "height": height,
            "mon": 1,
        }

        # 捕获指定区域的屏幕
        sct_img = sct.grab(capture_area)

        # 计算捕获图像的中心点
        center_x = left + width // 2
        center_y = top + height // 2

        # 保存捕获的屏幕到临时文件
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=tmpfile.name)
            return tmpfile.name, (left, top, width, height, center_x, center_y)

def wildegness(reward1, reward2):
    # 捕获屏幕区域并获取临时文件路径和捕获区域的左上角坐标以及宽度和高度
    screen_capture, (offset_x, offset_y, width, height,center_x,center_y) = capture_screen_area()

    try:
        for i in range(2):
            # 在捕获的屏幕空间中寻找图像
            img1 = pyautogui.locateCenterOnScreen(screen_capture,
                                                  region=(offset_x, offset_y, width, height))
            img2 = pyautogui.locateCenterOnScreen(screen_capture,
                                                  region=(offset_x, offset_y, width, height))

            # 检查两个图像是否都存在
            if img1 and img2:
                # 移动到中点并点击
                pyautogui.moveTo(center_x, center_y)
                pyautogui.click()
                print('点击了捕获图像的中心')
                print(img1,img2)
                return True
            elif img1:
                # 只有img1存在，点击img1
                pyautogui.moveTo(img1[0], img1[1])
                pyautogui.click()
                print('不休荒原，启动！')
                return True
            elif img2:
                # 只有img2存在，点击img2
                pyautogui.moveTo(img2[0], img2[1])
                pyautogui.click()
                print('不休荒原，启动！')
                return True
    except pyautogui.ImageNotFoundException:
        print('原来已经启动了')
    else:
        return False
    finally:
        # 删除临时文件
        os.remove(screen_capture)

wildegness('./dataset/wildegness1.png','./dataset/wildegness2.png')

# 用于领取荒原奖励
def getWildegness_resource(image1, image2):
    max_attempts = 10  # 增加尝试次数
    for i in range(max_attempts):
        try:
            img1 = pyautogui.locateCenterOnScreen(image1, confidence=0.6)
            img2 = pyautogui.locateCenterOnScreen(image2, confidence=0.6)
            if img1:
                pyautogui.moveTo(img1[0], img1[1])
                pyautogui.click()
                time.sleep(0.5)  # 短暂等待
            if img2:
                pyautogui.moveTo(img2[0], img2[1])
                pyautogui.click()
                time.sleep(0.5)
            return True
        except pyautogui.ImageNotFoundException:
            print(f'第{i + 1}次未检测到图片，等待0.5秒后重试。')
            time.sleep(0.5)  # 等待0.5秒
    else:
        print('看来荒原没有什么要事')
        return False

# 用于与荒原朋友互动
def getWildegness_frends(image):
    if getWildegness_resource('./dataset/weichen.png', './dataset/lici.png'):
        try:
            img = pyautogui.locateCenterOnScreen(image, confidence=0.6)
            if img:
                pyautogui.moveTo(img[0], img[1])
                pyautogui.click()
                print('与荒原的朋友互动了一下')
            else:
                print('未找到朋友的图像')
        except pyautogui.ImageNotFoundException:
            print('未找到朋友的图像')
    else:
        homeImg = './dataset/home.png'
        Automation.big_back(homeImg)  # 使用big_back函数返回主页

# 调用函数
getWildegness_frends('./dataset/friend.png')


# 使用subprocess模块运行1999V1.py文件
subprocess.run(['python', '1999V1_activity.py'])
