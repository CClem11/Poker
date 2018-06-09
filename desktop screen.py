# -*- coding:utf8 -*-
import cv2
import numpy as np
from PIL import ImageGrab

capture = cv2.VideoCapture(0) #vive la webcam de m****


screen = ImageGrab.grab()
print(screen)
screen_np = np.array(screen, dtype='uint8').reshape((screen.size[1], screen.size[0], 3))

cv2.imshow('Dektop Screen', screen_np)

while True:
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

print("fdsfd")
		
#close
capture.release()
cv2.destroyAllWindows()