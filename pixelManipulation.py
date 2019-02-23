import imageVisualization as iv
import cv2

img = iv.img

px = img[800,850]
print(px)
img[800,850] = [255,255,255]
print(img[800,850])

roi = img[100:150, 100:150] #roi = region of image
print(roi)
img[100:150, 100:150] = [255,255,25]
print(img[100:150, 100:150])

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite('imagesToManipulate/transformedImages/jorge2mod.png', img)
