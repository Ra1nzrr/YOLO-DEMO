import cv2
from ultralytics import YOLO

# 加载 YOLOv8 模型
model = YOLO('yolov8s.pt')

# 打开系统摄像头（0 表示默认摄像头）
cap = cv2.VideoCapture(0)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # 从摄像头读取一帧
    ret, frame = cap.read()

    if not ret:
        print("无法读取摄像头画面")
        break

    # 使用 YOLOv8 进行目标检测
    results = model(frame)

    # 获取检测结果并在帧上绘制边框
    annotated_frame = results[0].plot()

    # 显示处理后的帧
    cv2.imshow('YOLOv8 Detection', annotated_frame)

    # 按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源并关闭窗口
cap.release()
cv2.destroyAllWindows()
