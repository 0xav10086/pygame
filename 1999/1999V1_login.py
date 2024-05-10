import pyautogui
import time

def set(setImg):
    pyautogui.locateCenterOnScreen(setImg, confidence=0.8)
    x, y = 1920//2, 1080//2
    pyautogui.moveTo(x, y)
    pyautogui.click()


# 签到以及生日
