# -*- coding:utf8 -*-
import cv2
import numpy as np
from PIL import ImageGrab
import matplotlib.pyplot as plt

screen = ImageGrab.grab()
print(screen)
#screen.show()
screen_np = np.array(screen, dtype='uint8').reshape((screen.size[1], screen.size[0], 3))

plt.imshow(screen_np)
plt.show()
#or
#cv2.imshow("Dektop Screen", screen_np)
		
#close
cv2.destroyAllWindows()