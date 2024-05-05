import time

import easyocr
import mss
import pyautogui
import cv2
import numpy as np
import mss

def find_and_click(ac_img):
    for i in range(4):
        try:
            main = pyautogui.locateCenterOnScreen(ac_img, confidence=0.8)
            if main:
                pyautogui.moveTo(main)
                pyautogui.click()
                print('正在检查当前活性')
                break
        except Exception as e:
            print('活性检测失败！')
    else:
        with mss.mss() as sct:
            monitor_number = 1  # 屏幕编号，1 代表第1号屏幕
            mon = sct.monitors[monitor_number]  # 获取特定屏幕的信息
            print(f"第{monitor_number}号屏幕分辨率: {mon['width']} x {mon['height']}")
            x_click = 2440/1560 * mon['width']
            y_click = 450/1600 * mon['height']
        pyautogui.moveTo(x_click,y_click)
        pyautogui.click()
        print('尝试强制打开')


find_and_click('./img/activity.png')

time.sleep(3)

def activity(img):
    # 获取图片大小
    height, width = img.shape[:2]

    # 设置裁剪区域
    x = int(round(1150 / 2560 * width))
    y = int(round(1180 / 1600 * height))
    w = int(round(220 / 2560 * width))
    h = int(round(105 / 1600 * height))

    # 裁剪图像
    cropped_image = img[y:y + h, x:x + w]

    # 灰度处理
    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    # 创建一个阅读器实例，指定语言为简体中文和英文
    reader = easyocr.Reader(['ch_sim', 'en'])

    # 使用 readtext 方法读取图像文件中的文字
    results = reader.readtext(gray)

    for (bbox, text, prob) in results:
        # 检查识别到的文本是否为数字
        if text.isdigit():
            print(f'识别到的数字: {text} - 置信度: {prob:.2f}')

    pyautogui.moveTo(w, h)
    pyautogui.click()

with mss.mss() as sct:
    monitor = sct.monitors[1]
    sct_img = sct.grab(monitor)
    img = np.array(sct_img)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    activity(img)

