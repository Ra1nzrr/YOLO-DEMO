from ultralytics import YOLO
import cv2

# 加载 YOLOv8 模型
model = YOLO('yolov8s.pt')

# 读取图片
img = cv2.imread('test.png')

# 使用 YOLOv8 进行目标检测
results = model(img)

# 在图片上绘制边框
annotated_img = results[0].plot()

# 保存带有边框的图片
cv2.imwrite('result.png', annotated_img)

print("处理完成，结果保存在 result.png")