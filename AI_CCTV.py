import torch
import numpy as np
import cv2
import time

prev_time = 0
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
cap = cv2.VideoCapture("https://cctvn.freeway.gov.tw/abs2mjpg/bmjpg?camera=13380")
while cap.isOpened():
    success, frame = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue
    frame = cv2.resize(frame,(960,540))
    results = model(frame)
    results.print()

    # print(results.xyxy)
    output_image = np.squeeze(results.render())
    cv2.putText(output_image, f'FPS: {int(1 / (time.time() - prev_time))}',
    (3, 40), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
    prev_time = time.time()
    cv2.imshow('YOLO COCO 02', output_image)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()