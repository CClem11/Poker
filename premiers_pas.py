# -*- coding:utf8 -*-

#Premiers pas avec openCV

import cv2
from PIL import ImageGrab

capture = cv2.VideoCapture(0) #vive la webcam de m****
ret, frame = capture.read()
print('ret:', ret)

while True:
	ret, frame = capture.read()
	cv2.imshow('webcam', frame)
	
	#pour sortir
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#close
capture.release()
cv2.destroyAllWindows()