import cv2
from ultralytics import YOLO

model = YOLO('yolov8s.pt')
cap = cv2.VideoCapture('test.mp4')
out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), cap.get(cv2.CAP_PROP_FPS),
                      (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    results = model(frame)
    out.write(results[0].plot())

cap.release()
out.release()
