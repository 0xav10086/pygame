import torch
from PIL import Image
import torchvision.transforms as transforms
import torchvision
import cv2
import numpy as np

# 加载模型
model = torchvision.models.regnet.regnet_x_400mf()
model.load_state_dict(torch.load('MNIST_5_acc_0.9717.pth'))
model.eval()  # 设置为评估模式

# 图像预处理
def preprocess_image(image):
    transformation = transforms.Compose([
        transforms.Resize(size=(32, 32)),
        transforms.Grayscale(num_output_channels=3),
        transforms.ToTensor()
    ])
    return transformation(image).unsqueeze(0)  # 添加批次维度

# 预测函数
def predict(model, image_tensor):
    outputs = model(image_tensor)
    _, predicted = torch.max(outputs.data, 1)
    return predicted.item()

# 检查图像明度变化的函数
def check_brightness_variation(image, threshold=0.1):
    # 检查图像通道数
    if len(part_array.shape) == 2:  # 灰度图将只有两个维度
        # 将灰度图转换回BGR
        part_array_bgr = cv2.cvtColor(part_array, cv2.COLOR_GRAY2BGR)
        hsv_image = cv2.cvtColor(part_array_bgr, cv2.COLOR_BGR2HSV)
    else:
        # 如果图像已经是BGR，直接转换到HSV
        hsv_image = cv2.cvtColor(part_array, cv2.COLOR_BGR2HSV)
    v_channel = hsv_image[:, :, 2]
    return np.var(v_channel) > threshold

# 导入图像
image = cv2.imread('./img/test.png')
height, width = image.shape[:2]

# 裁剪图像
x = int(round(1150/2560 * width))
y = int(round(1180/1600 * height))
w = int(round(220/2560 * width))
h = int(round(105/1600 * height))
cropped_image = image[y:y+h, x:x+w]

# 灰度处理
gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

# 应用阈值处理
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# 再分割
re_height, re_width = thresh.shape[:2]
width_third = re_width // 3

# 分割图片
left_part = thresh[:, :width_third]
middle_part = thresh[:, width_third:2*width_third]
right_part = thresh[:, 2*width_third:]

# 将分割后的图像转换为PIL Image
left_image = Image.fromarray(left_part)
middle_image = Image.fromarray(middle_part)
right_image = Image.fromarray(right_part)


# 使用cv2.imshow显示三张图片
cv2.imshow('Left Part', left_part)
cv2.imshow('Middle Part', middle_part)
cv2.imshow('Right Part', right_part)

# 等待按键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()


# 初始化预测结果字符串
predicted_numbers = ''

# 对每个分割后的图像部分进行明度变化检查和预测
for part, image in zip(['left', 'middle', 'right'], [left_image, middle_image, right_image]):
    part_array = np.array(image)
    if check_brightness_variation(part_array):
        prediction = predict(model, preprocess_image(image))
        predicted_numbers += str(prediction)
    else:
        print(f"{part} part of the image has no brightness variation and will be discarded.")

print(f'合并后识别出的数字是：{predicted_numbers}')