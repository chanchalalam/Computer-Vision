import cv2
import numpy as np
import time
import os

from HandTrackingModule import handDetector as htm

brushThickness = 25
eraserThickness = 100

folderPath = "Headers"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    if image is None:
        print(f"Error loading image: {imPath}")
        continue
    overlayList.append(image)
print(len(overlayList))
header = overlayList[0]
drawColor = (255, 0, 255)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm(detectionCon=0.65, maxHands=2)
xp, yp = 0, 0

imgCanvas = np.zeros((720, 1280, 3), np.uint8)
#imgCanvas[:] = (255, 255, 255)

def fingersUp(self):
    fingers = []
    if self.results.multi_hand_landmarks:
        myHand = self.results.multi_hand_landmarks[0]
        for id, lm in enumerate(myHand.landmark):
            if lm.z < 0.1:  # Adjust threshold based on your setup
                fingers.append(1)
            else:
                fingers.append(0)
    return fingers

while True:
    success, img = cap.read()
    if not success:
        print("Ignoring empty camera frame")
        continue

    img = cv2.flip(img, 1)

    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        fingers = fingersUp(detector)

        # Selection Mode
        if len(fingers) >= 2 and fingers[1] and fingers[2]:
            xp, yp = 0, 0
            if y1 < 125:
                if 250 < x1 < 450:
                    header = overlayList[0]
                    drawColor = (255, 0, 255)
                elif 550 < x1 < 750:
                    header = overlayList[1]
                    drawColor = (255, 0, 0)
                elif 800 < x1 < 950:
                    header = overlayList[2]
                    drawColor = (0, 255, 0)
                elif 1050 < x1 < 1200:
                    header = overlayList[3]
                    drawColor = (0, 0, 0)

        # Drawing Mode
        if len(fingers) >= 1 and fingers[1]:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp, yp = x1, y1

    img[0:125, 0:1280] = header

    #cv2.imshow("Canvas", imgCanvas)
    img = cv2.addWeighted(img, 0.7, imgCanvas, 1, 0)
    cv2.imshow("Image", img)

    cv2.waitKey(1)
