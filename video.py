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