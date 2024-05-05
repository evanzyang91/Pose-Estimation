import cv2
import mediapipe as mp
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)
pTime=0
detector = pm.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()