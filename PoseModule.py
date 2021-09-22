import cv2
import mediapipe as mp
import time





class PoseDetector():

	def __init__(self, mode = False, model_complexity=1, smooth_landmarks = True, enable_segmentation=False, smooth_segmentation=True, detectionCon = 0.5 , trackCon = 0.5 ):

		# parameters from the Pose library 

		# static_image_mode=False,
		# model_complexity=1,
		# smooth_landmarks=True,
		# enable_segmentation=False,
		# smooth_segmentation=True,
		# min_detection_confidence=0.5,
		# min_tracking_confidence=0.5


		self.mode = mode
		self.model_complexity = model_complexity
		self.smooth_landmarks = smooth_landmarks
		self.enable_segmentation = enable_segmentation
		self.smooth_segmentation = smooth_segmentation
		self.detectionCon = detectionCon
		self.trackCon = trackCon






		self.mpPose = mp.solutions.pose #create object to detect pose
		self.pose = self.mpPose.Pose(self.mode, self.model_complexity, self.smooth_landmarks, self.enable_segmentation, self.smooth_segmentation, self.detectionCon, self.trackCon)
		self.mpDraw = mp.solutions.drawing_utils



	def rescale_frame(self, frame, percent):
		width = int(frame.shape[1] * percent/ 100)
		height = int(frame.shape[0] * percent/ 100)
		dim = (width, height)
		return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)


	def findPose(self, img, draw = True):


		imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

		self.results = self.pose.process(imgRGB)


		if self.results.pose_landmarks:
			if draw:
				self.mpDraw.draw_landmarks( img,self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

		percent = 50

		frame75 = self.rescale_frame(img , percent)
		
		return frame75


	def findPosition(self, img, draw=True):

		lmList = []

		if self.results.pose_landmarks:
		
			for id, lm in enumerate(self.results.pose_landmarks.landmark):
				h , w , c = img.shape

				cx , cy = int(lm.x*w), int(lm.y*h) 

				lmList.append([id,cx,cy])

				if draw:
					cv2.circle(img, (cx,cy) , 5, (255,0,0) , cv2.FILLED)

		return lmList


def main():
	cap = cv2.VideoCapture('Media/video (1).mp4')

	pTime = 0

	detector = PoseDetector()

	while True:

		success , img = cap.read()

		img2 = detector.findPose(img)

		lmList = detector.findPosition(img2)

		print(lmList)
	
		cTime = time.time()

		fps = 1/(cTime - pTime)

		pTime = cTime

		cv2.putText(img, str(int(fps)),(70,50), cv2.FONT_HERSHEY_PLAIN,3, (255,0,0),3)

		

		cv2.imshow("Image" , img2)

		cv2.waitKey(1)




if __name__ == "__main__" : 
	main()