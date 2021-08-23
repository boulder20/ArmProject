import cvzone
import cv2
import HandTrackingModule as htm
import SerialModule as sm
cap = cv2.VideoCapture(0)
detector = htm.HandDetector(maxHands=1, detectionCon=0.5)
mySerial = sm.SerialObject("COM3", 9600, 1)
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp()
        mySerial.sendData(fingers)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
