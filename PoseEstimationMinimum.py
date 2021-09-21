import cv2
import mediapipe as mp
import time


def rescale_frame(frame, percent=75):
	width = int(frame.shape[1] * percent/ 100)
	height = int(frame.shape[0] * percent/ 100)
	dim = (width, height)
	return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)


mpPose = mp.solutions.pose #create object to detect pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils


cap = cv2.VideoCapture('Media/video (1).mp4')

pTime = 0

while True:

	success , img = cap.read()

	imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	results = pose.process(imgRGB)

	print(results.pose_landmarks) # this would have an x , y , z and visibility 

	if results.pose_landmarks:
		mpDraw.draw_landmarks( img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
	


	cTime = time.time()

	fps = 1/(cTime - pTime)

	pTime = cTime

	cv2.putText(img, str(int(fps)),(70,50), cv2.FONT_HERSHEY_PLAIN,3, (255,0,0),3)

	frame75 = rescale_frame(img , percent=50)

	cv2.imshow("Image" , frame75)

	cv2.waitKey(1)

