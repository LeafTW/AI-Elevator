import torch
import numpy as np
import cv2

class ai_search:
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    cap = cv2.VideoCapture(0)

    # def star(self):
    #     while self.cap.isOpened():
    #         success, frame = self.cap.read()
    #         if not success:
    #           print("Ignoring empty camera frame.")
    #           continue
    #         frame = cv2.resize(frame,(800,480))
    #         results = self.model(frame)
    #
    #         ans = results.pred
    #         k = 0
    #         for i in range(len(ans[0])):
    #             stans = str(ans[0][i][5])
    #             if stans[7] == "0":
    #                 k = k + 1
    #         return k
    #         # print(k, "persons")
    #
    #
    #         print(np.array(results.render()).shape)
    #         cv2.imshow('YOLO COCO 01', np.squeeze(results.render()))
    #         if cv2.waitKey(1) & 0xFF == 27:
    #             break

# 單純開相機
#     while cap.isOpened():
#         success, frame = cap.read()
#         if not success:
#             print("Ignoring empty camera frame.")
#             continue
#         frame = cv2.resize(frame, (800, 480))
#         results = model(frame)
#
#         ans = results.pred
#         k = 0
#         for i in range(len(ans[0])):
#             stans = str(ans[0][i][5])
#             if stans[7] == "0":
#                 k = k + 1
#         # print(k, "persons")
#
#         print(np.array(results.render()).shape)
#         cv2.imshow('YOLO COCO 01', np.squeeze(results.render()))
#         if cv2.waitKey(1) & 0xFF == 27:
#             break
#     cap.release()
#     cv2.destroyAllWindows()

