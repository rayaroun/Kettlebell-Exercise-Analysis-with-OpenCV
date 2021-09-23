import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture('Media/video (1).mp4')

img = cv2.imread("Media/kettlebell end position.jpg")

detector = pm.PoseDetector()

while True:

	# success , img = cap.read()

	# img = cv2.resize(img, (1280,720))

	img = detector.findPose(img, False)

	#getting the landmark positions for the points 

	lmlist = detector.findPosition(img, False)

	# print(lmlist)

	if len(lmlist) != 0:
		detector.findAngle(img, 11, 23, 25 )

	# img = cv2.imread('')

	cv2.imshow('Image', img)

	cv2.waitKey(1)

	
# 11 23 25