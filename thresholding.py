import show
cv2 = show.cv2
#import numpy as np

img = cv2.imread('imagesToManipulate/thres2.jpg')
rows, cols, channels = img.shape
img = cv2.resize(img, (int(rows/3), int(cols/3)))

ret, threshold = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY)
grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret2, threshold2 = cv2.threshold(grayed, 50, 255, cv2.THRESH_BINARY)
gauss = cv2.adaptiveThreshold(grayed, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 3)
ret2, otsu = cv2.threshold(grayed, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


show.image(['original' , img,
            'threshold', threshold,
            'thresh2'  , threshold2,
            'gauss'    , gauss,
            'otsu'     , otsu])
