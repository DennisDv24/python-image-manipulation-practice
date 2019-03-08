import show
cv2 = show.cv2

img = [cv2.imread('imagesToManipulate/lg0.png'),
       cv2.imread('imagesToManipulate/lg1.png'),
       cv2.imread('imagesToManipulate/curca.png')]

#add = img[0] + img[1]
#add = cv2.add(img[0], img [1])
add = cv2.addWeighted(img[0], 0.6, img[1], 0.4, 0)
show.image(['img', add])

rows, cols, channels = img[2].shape
roi = img[0][0:rows, 0:cols]


imgGrayed = cv2.cvtColor(img[2], cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(imgGrayed, 220, 255, cv2.THRESH_BINARY_INV) #mask like the photoshop one
show.image(['curcas mask', mask])
maskNot = cv2.bitwise_not(mask)
img0BG = cv2.bitwise_and(roi, roi, mask = maskNot)
img2FG = cv2.bitwise_and(img[2], img[2], mask = mask)

f = cv2.add(img0BG, img2FG)
img[0][0:rows, 0:cols] = f
show.image(['f image', img[0]])
