import cv2
import numpy as np
from matplotlib import pyplot as plt
#import mathplotlib as plt

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

#image input
image = cv2.imread('stroopw.jpeg', 0)

def find_cookie(image)

	#Image scaling
	max_dimension = max(image.shape)
	scale = 700/max_dimension
	image = cv2.resize(image, None, fx=scale, fy=scale)

	#Image cleaning
	image_blur = cv2.GaussianBlur(image,(7,7),0)
	image_blur_hsv = cv2.cvtColor(image_blur, cv2.COLOR_RGB2HSV)

	#image colour detection
	min_brown = np.array([27,71,100])
	max_brown = np.array([27,71,28])
	mask_brown = cv2.inRange(image_blur_hsv, min_brown, max_brown)

	#image segmentation
	kernel = cv2.getStructuringElement(sv2.MORPH_ELLIPSE (15,15))
	mask_closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	mask_clean - cv2.morphologyEx(mask_closed, cv2.MORPH_OPEN, kernel)

	#find object overlay
	overlay = overlay_mask(mask_clean, image)

	#circle object
	circled = circle_contour(overlay, mask_clean)

	show(circled)

cv2.imshow("edges", edges)


cv2.waitKey(0)