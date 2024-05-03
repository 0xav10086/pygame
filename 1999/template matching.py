# 存在未知错误，导致的数字识别出错
# 尝试使用ORB算法


import cv2 as cv
import numpy as np
import matplotlib
import myutils


# 图片展示
def cv_show(name, img):
    cv.imshow(name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

# 读入模板图
img = cv.imread('./img/number1.png')

# 模板预处理
ref = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ref = cv.threshold(ref, 10, 255, cv.THRESH_BINARY_INV)[1]

# 轮廓检测
refCnts, hierarchy = cv.findContours(ref.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(img, refCnts, -1, (0, 0, 255), 2)

# 轮廓排序
refCnts = myutils.sort_contours(refCnts)[0]
digits = {}

# 单个轮廓提取到字典中
for (i, c) in enumerate(refCnts):
    (x, y, w, h) = cv.boundingRect(c)
    roi = ref[y:y + h, x:x + w]
    roi = cv.resize(roi, (57, 88))
    digits[i] = roi

# 读取图像
image = cv.imread('./img/test.png')
height, width = image.shape[:2]

# 设置裁剪区域的坐标和大小
x = int(round(1150/2560 * width))
y = int(round(1180/1600 * height))
w = int(round(220/2560 * width))
h = int(round(105/1600 * height))

# 裁剪图像
cropped_image = image[y:y+h, x:x+w]

# 灰度处理
gray = cv.cvtColor(cropped_image, cv.COLOR_BGR2GRAY)

# 应用阈值处理
thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

# 轮廓检测
cnts, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# 将二值化图像转换为RGB格式
thresh_rgb = cv.cvtColor(thresh, cv.COLOR_GRAY2RGB)

# 设置面积阈值
min_area_threshold = 50  # 最小面积阈值
max_area_threshold = 8000  # 最大面积阈值

# 过滤轮廓
filtered_cnts = [cnt for cnt in cnts if min_area_threshold < cv.contourArea(cnt) < max_area_threshold]

# 在RGB图像上绘制红色轮廓
for cnt in cnts:
    area = cv.contourArea(cnt)
    if max_area_threshold > area > min_area_threshold:
        cv.drawContours(thresh_rgb, [cnt], -1, (0, 0, 255), 2)

cv_show('Contours in Red', thresh_rgb)

recognized_digits = []

# 将检测到的数字轮廓调整为与模板相同的大小
for c in filtered_cnts:
    (x, y, w, h) = cv.boundingRect(c)
    roi = thresh[y:y + h, x:x + w]
    roi_resized = cv.resize(roi, (57, 88))

    scores = []
    for digit, template in digits.items():
        result = cv.matchTemplate(roi_resized, template, cv.TM_SQDIFF)
        (_, score, _, _) = cv.minMaxLoc(result)
        scores.append(score)

    # 选择得分最高的数字
    recognized_digit = str(np.argmax(scores))
    recognized_digits.append(recognized_digit)
    recognized_digits.reverse()

# 输出识别结果
print("识别出的数字序列:", ''.join(recognized_digits))