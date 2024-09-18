# YOLO DEMO

下方将会提供三种不同的的调用YOLO V8官方的模型yolov8s.pt

## 1. 处理视频

运行前提:
a. 请完成ppt已描述过的步骤
b. 需要你将项目文件夹内添加一个任意的视屏 并改名为"test.mp4"

### Code:
```python
import cv2
import os
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO('yolov8s.pt')

# Video file path
video_path = 'test.mp4'
output_folder = 'frames_output'

# Create output folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open video file
cap = cv2.VideoCapture(video_path)

frame_count = 0

# Process each frame in the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection using YOLOv8
    results = model(frame)

    # Draw bounding boxes on the frame
    annotated_frame = results[0].plot()

    # Save the processed frame
    frame_output_path = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_output_path, annotated_frame)

    frame_count += 1

# Release video object
cap.release()

print(f"Video frames processed, total {frame_count} frames.")
```
2. 处理照片

运行前提:

a. 请完成ppt已描述过的步骤
b. 需要你将项目文件夹内添加一个任意的图片文件 并改名为"test.png"
