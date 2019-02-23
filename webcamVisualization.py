import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('camera', frame) #Show each frame every frame
    cv2.imshow('camera2', grayFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'): #Press q = finish loop
        break

cap.release()
cv2.destroyAllWindows()
