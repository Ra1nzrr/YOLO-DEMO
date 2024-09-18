# YOLO DEMO

下方将会提供三种不同的的调用YOLO V8官方的模型yolov8s.pt

## 1. 处理视频

### 运行前提:
a. 请完成ppt已描述过的步骤
b. 需要你将项目文件夹内添加一个任意的视屏 并改名为"test.mp4"

### Code:
```python
import cv2
import os
from ultralytics import YOLO

# 加载 YOLOv8 模型
model = YOLO('yolov8s.pt')

# 视频文件路径
video_path = 'test.mp4'
output_folder = 'frames_output'

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 打开视频文件
cap = cv2.VideoCapture(video_path)

frame_count = 0

# 循环处理每一帧
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 使用 YOLOv8 模型进行目标检测
    results = model(frame)

    # 获取检测结果并在帧上绘制边框
    annotated_frame = results[0].plot()

    # 保存带有边框的帧
    frame_output_path = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_output_path, annotated_frame)

    frame_count += 1

# 释放视频对象
cap.release()

print(f"视频帧处理完成，共处理了 {frame_count} 帧。")
```
## 2. 处理照片

运行前提:

a. 请完成ppt已描述过的步骤
b. 需要你将项目文件夹内添加一个任意的图片文件 并改名为"test.png"
