import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imagesToManipulate/jorge1.jpg', cv2.IMREAD_COLOR)
#IMREAD_GRAYSCALE = 0, IMREAD_COLOR = 1, IMREAD_UNCHANGED = -1


#Can also
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.plot([400,100],[800,900], 'c', linewidth=5)
# plt.show()

cv2.line(img, (0,0), (400,400), (150,0,255), 15) #start line, finish line, color(BGR), width
cv2.rectangle(img, (400,300), (900,900), (255,0,255), 10)
cv2.circle(img, (400,300), 100,(255,255,255), -1) #-1 value in width to fill the figure
points = np.array( ([40,40],[40,20],[800,800],[400,400],[250,70],[30,120]) , np.int32)
cv2.polylines(img, [points], True, (0,255,255,255), 3) #Third value is to finish or not to finish the polygon
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Hy', (600,500), font, 3, (255,255,255), 1, cv2.LINE_AA )


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('imagesToManipulate/transformedImages/jorge1mod.png', img)
