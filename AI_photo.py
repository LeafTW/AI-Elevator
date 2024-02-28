import torch
import cv2
import numpy as np
import random
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# model.conf = 0.5
# print(model)

personPicture=["1.png","2.png","3.jpg","4.png","5.jpg","6.png","7.jpg","8.png","9.png","10.jpg",]
pictureAddress="/Users/zi-wei/PycharmProjects/yolococo/personPhoto/"


def star():
  dataIn = pictureAddress + personPicture[random.randrange(10)]
  img=cv2.imread(dataIn)
  results = model(img)

  # results.print()
  # print(results.pred)

  ans=results.pred
  peopleTotle=0
  for i in range(len(ans[0])):
    stans=str(ans[0][i][5])
    if stans[7] == "0":
      peopleTotle=peopleTotle+1
  # print(peopleTotle,"persons")

  cv2.imshow('YOLO COCO', np.squeeze(results.render()))

  img=cv2.imread(dataIn)
  # cv2.imshow("Output", img)
  # cv2.waitKey(0)
  return peopleTotle


