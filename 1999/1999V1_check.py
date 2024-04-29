import pyautogui
import time
import cv2
import pytesseract
from PIL import ImageGrab
import numpy as np

# 屏幕截图
screenshot = ImageGrab.grab()
screenshot.save('screen.png')

# 读取图像
image = cv2.imread('screen.png')

# 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 应用阈值化
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# 寻找数字的轮廓
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    # 计算轮廓的边界框
    x, y, w, h = cv2.boundingRect(cnt)

    # 提取ROI
    roi = thresh[y:y + h, x:x + w]

    # 使用Tesseract识别数字
    text = pytesseract.image_to_string(roi, config='--psm 6 digits')
    print(text)

# 显示结果
cv2.imshow('Image', image)
cv2.imshow('Thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
