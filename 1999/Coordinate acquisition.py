import pyautogui
import time
import sys
import mss
import mss.tools


def getWildegness(image1, image2, image3):
    max_attempts = 10  # 增加尝试次数
    for i in range(max_attempts):
        try:
            img1 = pyautogui.locateCenterOnScreen(image1, confidence=0.6)  # 减少置信度
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
