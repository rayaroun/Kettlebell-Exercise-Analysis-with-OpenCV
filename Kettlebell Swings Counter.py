import cv2
import numpy as np
import time
import PoseModule as pm
import time

cap = cv2.VideoCapture('Media/video (5).mp4')

# img = cv2.imread("Media/kettlebell end position.jpg")

detector = pm.PoseDetector()

count = 0 

dir = 0 # to count one repetition 

while True:

	success , img = cap.read()

	img = cv2.resize(img, (500,889))

	img = detector.findPose(img, False)

	#getting the landmark positions for the points 

	lmlist = detector.findPosition(img, False)

	# print(lmlist)

	#  finding angle between right shoulder hip and knee
	if len(lmlist) != 0:
		angle = detector.findAngle(img, 12, 24, 26 )

		per = np.interp(angle , (90,175),(0,100) )

		# print(angle, per)

		# checking for a complete kettlebell swing

		if per == 0:
			if dir == 0:
				count += 0.5
				dir = 1 
		if per == 100 and count != 0:
			if dir == 1:
				count += 0.5
				dir = 0 
		

		# print(count)

	# displyaing the count on the video


	cv2.putText( img, "Count : " + str(int(count)) , (20,120) , cv2.FONT_HERSHEY_PLAIN , 3, (255 , 153 , 0) , 3 )

	cv2.imshow('Image', img)

	cv2.waitKey(1)


	# time.sleep(60)
	
# 11 23 25