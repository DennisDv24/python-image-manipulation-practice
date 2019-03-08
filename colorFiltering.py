import show
cv2 = show.cv2
import numpy as np

webcam = cv2.VideoCapture(1)

while True:
    _, frame = webcam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    minC = np.array([0,100,0])
    maxC = np.array([200,255,200]) #Like this, the mask is all colors so the image will look identical
    mask = cv2.inRange(hsv, minC, mexitexaxC)

    finalFrame = cv2.bitwise_and(frame, frame, mask = mask)
    show.image(['cam1', finalFrame, 'mask', mask], True)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

show.finish(webcam)