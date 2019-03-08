import cv2
def image(image, video = False):
    for i in range(int(len(image)/2)):
        cv2.imshow(image[2*i], image[2*i+1])
        if(i == (len(image)/2)-1):
            break
    if(video == False):
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def finish(frame):
    cv2.destroyAllWindows()
    print('windows destroyed')
    frame.release()
    print('capturing stopped')
