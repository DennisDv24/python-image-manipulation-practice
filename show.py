import cv2
def image(windowName, image):
    cv2.imshow(windowName, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
