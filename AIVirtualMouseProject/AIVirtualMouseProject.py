
import cv2
import time
import HandTrackingModule as htm
import numpy as np
import pyautogui

fingers = []

wCam, hCam = 640, 480
frameR = 100  # frame reduction
smoothening = 8
pTime = 0
plocX, plocY = 0, 0  # previous locations of x and y
clocX, clocY = 0, 0  # current locations of x and y

cap = cv2.VideoCapture(0)
cap.set(3, wCam)  # width
cap.set(4, hCam)  # height
detector = htm.handDetector(detectionCon=0.60, maxHands=1)  # only one hand at a time
wScr, hScr = pyautogui.size()

while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2. Handle no hand detected scenario
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)

        # 3. Check finger status only if hand is detected
        if len(fingers) >= 3:  # Check if list has at least 3 elements for finger detection
            fingers = detector.fingersUp()

            # 4. Draw detection region
            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

            # 5. Only Index Finger : Moving Mode
            if fingers[1] == 1 and fingers[2] == 0:
                # 6. Convert Coordinates
                x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))  # converting x coordinates
                y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))  # converting y

                # 7. Smoothen Values
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening

                # 8. Move Mouse (avoid mirror effect)
                pyautogui.moveTo(wScr - clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)  # circle for moving mode
                plocX, plocY = clocX, clocY

            # 9. Both Index and middle fingers are up : Clicking Mode
            if fingers[1] == 1 and fingers[2] == 1:
                # 10. Find distance between fingers
                length, img, lineInfo = detector.findDistance(8, 12, img)

                # 11. Click mouse if distance short
                if length < 30:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    pyautogui.click()

    # 12. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # 13. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)

# Release resources
cap.release()
cv2.destroyAllWindows()
