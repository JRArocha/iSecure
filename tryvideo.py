import cv2

vid = cv2.VideoCapture(0)

vid_count = 0

while True:
    ret, frame = vid.read()

    FlippedImage = cv2.flip(frame, 1)
    cv2.imshow("test", FlippedImage)
    k = cv2.waitKey(10)
    
    if k == 27:
        break

vid.release()
cv2.destroyAllWindows()



