import torch
import numpy as np
import cv2
import time
import pafy
prev_time = 0

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
url = "https://www.youtube.com/watch?v=z_mlibCfgFI&ab_channel=%E6%A1%83%E5%9C%92%E6%99%BA%E6%85%A7%E6%97%85%E9%81%8A%E9%9B%B2TaoyuanTravel"
# url = "https://www.youtube.com/watch?v=F37nhO8fJds"

live = pafy.new(url)
stream = live.getbest(preftype="mp4")
cap = cv2.VideoCapture(stream.url)
while cap.isOpened():
    success, frame = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue
    frame = cv2.resize(frame,(960,540))
    results = model(frame)
    output_image = np.squeeze(results.render())
    cv2.putText(output_image, f'FPS: {int(1 / (time.time() - prev_time))}',
                (3, 40), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
    prev_time = time.time()
    cv2.imshow('YOLO COCO', output_image)

    ans = results.pred
    k = 0
    for i in range(len(ans[0])):
        stans = str(ans[0][i][5])
        if stans[7] == "0":
            k = k + 1
    print(k, "persons")

    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()