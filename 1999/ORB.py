import cv2
import numpy as np

img1 = cv2.imread('./img/test_5.png')
img2 = cv2.imread('./img/number1.png', 0)  # 数据库中的图像

# 初始化ORB检测器
orb = cv2.ORB_create()

# 找到关键点和描述符
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# 创建BFMatcher对象
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# 进行匹配
matches = bf.match(des1, des2)

# 根据距离排序
matches = sorted(matches, key=lambda x: x.distance)

# 假设我们有一个字典来映射匹配点到相应的数字
number_map = {0: '区域1', 1: '区域2', 2: '区域3', 3: '区域4', 4: '区域5', 5: '区域6', 6: '区域7', 7: '区域8', 8: '区域9', 9: '区域10',  44: '区域X'}

# 初始化匹配的数字变量
matched_number = None
def parse_number_from_region(region_name):
    # 假设区域名称的格式是 "区域X"，其中X是数字
    return int(region_name[-1])  # 提取并返回区域名称的最后一个字符作为数字

# 找到最佳匹配的数字
if matches[0].trainIdx in number_map:
    best_match_region = number_map[matches[0].trainIdx]
    # 这里需要一个方法来从区域名称解析出实际的数字
    matched_number = parse_number_from_region(best_match_region)

# 检查匹配的数字是否已经被定义
if matched_number is not None:
    print(f'匹配的数字是: {matched_number}')
else:
    print('没有找到匹配的数字')
