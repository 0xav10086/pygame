from ultralytics import YOLO

# 加载预训练模型，在该模型基础上，训练目标检测的模型
model = YOLO('yolov8n.pt')

# 训练自定义数据集，数据配置保存在data.yaml中
model.train(
    data='main.yaml',
    epochs=50,
    batch=2,
    workers=0
)

# 使用验证集验证效果
model.val()
