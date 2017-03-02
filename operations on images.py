# -*- coding:utf8 -*-
import cv2
import numpy as np
from PIL import ImageGrab
import matplotlib.pyplot as plt

def get_desktop_screen():
	screen = ImageGrab.grab(bbox=(700, 50, 1600, 800))
	screen_np = np.array(screen, dtype='uint8').reshape((screen.size[1], screen.size[0], 3))
	return screen_np

def get_webcam():
	ret, frame = capture.read()
	return frame

capture = cv2.VideoCapture(0)
while True:
	frame1 = get_desktop_screen()
	frame2 = get_webcam()
	print(type(frame2))
	
	hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
	print(type(hsv))
	
	#cv2.imshow('desktop', gray1)
	cv2.imshow('webcam', frame2)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
#close
cv2.destroyAllWindows()