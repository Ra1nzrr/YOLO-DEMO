# YOLOv8 Model Usage

This document describes three different ways to call the YOLOv8 model (`yolov8s.pt`): processing video, processing images, and processing live webcam input for face detection.

## Prerequisites

Before running any of the examples, make sure you have completed the steps mentioned in the provided PowerPoint presentation. Additionally, ensure the required media files are present in the project folder.

## 1. Process Video

### Requirements:
- Complete the steps described in the PowerPoint.
- Add a video file to the project folder and rename it as `test.mp4`.

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
