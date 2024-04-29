import pyautogui
import time
import cv2
import numpy as np
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
