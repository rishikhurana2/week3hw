import sys
import cv2
import numpy as np
if (sys.argv[0] == "-i"):
	file = "index.png"
	image = cv2.imread(file)
	cv2.imshow("A Picture", image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
if (sys.agrv[1] == "-l"):
	cv2.NamedWindow("Feed", cv2.CV_WINDOW_AUTOSIZE)
	capture = cv2.CaptureFromCAM(0)
	While (True):
		frame = cv2.QueryFrame(capture)
		cv2.ShowImage("Camera Feed". frame)
		key = cv2.waitKey(10)
		if (key == 27):
			break
	cv2.destroyWindow("preview")
