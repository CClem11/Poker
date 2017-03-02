# -*- coding:utf8 -*-
import cv2
import numpy as np
from PIL import ImageGrab
import matplotlib.pyplot as plt

def get_desktop_screen():
	screen = ImageGrab.grab(bbox=(500, 200, 1000, 600))
	screen_np = np.array(screen, dtype='uint8').reshape((screen.size[1], screen.size[0], 3))
	return screen_np
	
while True:
	frame = get_desktop_screen()
	cv2.imshow('webcam', frame)
	
	#pour sortir
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
#close
cv2.destroyAllWindows()