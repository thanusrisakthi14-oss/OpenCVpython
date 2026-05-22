import cv2
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if not ret:
        print("camera failed to capture")
        break
    resized=cv2.resize(frame,(640,480))
    gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original",resized)
    cv2.imshow("Grayscale",gray)
    key=cv2.waitKey(1)
    if key == ord("s"):
        cv2.imwrite("Captured_image.jpg",gray)
        print("Image Saved")
    if key==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()