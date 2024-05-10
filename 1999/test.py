import time
import easyocr
import mss
import pyautogui
import cv2
import numpy as np
import mss


def cv_show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def activity(img):
    # 获取图片大小
    height, width = img.shape[:2]
    # cv_show('original', dataset)
    # 设置裁剪区域
    x = int(round(60 / 1920 * width))
    y = int(round(55 / 1080 * height))
    w = int(round(260 / 1920 * width))
    h = int(round(35 / 1080 * height))

    # 裁剪图像
    cropped_image = img[y:y + h, x:x + w]
    # cv_show('cropped', cropped_image)

    # 创建一个阅读器实例，指定语言为简体中文和英文
    reader = easyocr.Reader(['ch_sim', 'en'])

    # 使用 readtext 方法读取图像文件中的文字
    results = reader.readtext(cropped_image)

    print(results)


with mss.mss() as sct:
    # 使用第一个显示器
    monitor = sct.monitors[0]
    # 调整捕获区域的大小以匹配1920x1080分辨率
    monitor['width'] = 1920
    monitor['height'] = 1080
    # 确保 'left' 和 'top' 值正确
    monitor['left'] = 885
    monitor['top'] = -1080
    print(monitor)
    # 捕获整个屏幕
    sct_img = sct.grab(monitor)
    # 将截图转换为 NumPy 数组
    img = np.array(sct_img)
    activity(img)
