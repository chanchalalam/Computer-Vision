# import cv2
# import numpy as np
# import time
# import os
#
# import self as self
# from matplotlib.pyplot import draw
#
# # Import your hand tracking module
# import HandTrackingModule as htm
# from HandTracking.ProjectExampleHT import lmlist
#
# brushThickness = 25
# eraserThickness = 100
#
# folderPath = "Header"
# myList = os.listdir(folderPath)
# print(myList)
# overlayList = []
# for imPath in myList:
#     image = cv2.imread(f'{folderPath}/{imPath}')
#     if image is None:
#         print(f"Error loading image: {imPath}")
#         continue  # Skip to the next image if loading fails
#     overlayList.append(image)
# print(len(overlayList))
# header = overlayList[0]
# drawColor = (255, 0, 255)
#
# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 720)
#
# detector = htm.handDetector(detectionCon=0.65, maxHands=1)
# xp, yp = 0, 0
# imgCanvas = np.zeros((720, 1280, 3), np.uint8)
#
# def fingersUp(self):
#     fingers = []
#
#     if self.results.multi_hand_landmarks:
#         myHand = self.results.multi_hand_landmarks[0]  # Access the first hand
#         for id, lm in enumerate(myHand.landmark):
#             # ... finger detection logic based on landmark positions ...
#             pass
#
#     return fingers
#
#
# while True:
#
#     # 1. Import image
#     success, img = cap.read()
#     if not success:
#         print("Ignoring empty camera frame")
#         continue
#
#     img = cv2.flip(img, 1)  # Flip the image horizontally (optional)
#
#     # 2. Find Hand Landmarks
#     img = detector.findHands(img, draw)
#     lmList = detector.findPosition(img)
#
#     if len(lmList) != 0:
#         print(lmlist[4])
#
#         # Tip of index and middle fingers
#         x1, y1 = lmList[8][1:]
#         x2, y2 = lmList[12][1:]
#
#         # 3. Check which fingers are up
#         fingers = detector.fingersUp()
#
#         # 4. If Selection Mode - Two finger are up
#         if fingers[1] and fingers[2]:
#             print("Selection Mode")
#             if y1 < 125:
#                 if 250 < x1 < 450:
#                     header = overlayList[0]
#                     drawColor = (255, 0, 255)
#                 elif 550 < x1 < 750:
#                     header = overlayList[1]
#                     drawColor = (255, 0, 0)
#                 elif 800 < x1 < 950:
#                     header = overlayList[2]
#                     drawColor = (0, 255, 0)
#                 elif 1050 < x1 < 1200:
#                     header = overlayList[3]
#                     drawColor = (0, 0, 0)
#             cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)
#
#         # 5. If Drawing Mode - Index finger is up
#         if fingers[1] and fingers[2] == False:
#             cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
#             print("Drawing Mode")
#             if xp == 0 and yp == 0:
#                 xp, yp = x1, y1
#
#             # Draw line based on drawing color
#             if drawColor == (0, 0, 0):  # Eraser mode
#                 cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
#                 cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)  # Erase on canvas
#             else:  # Drawing mode
#                 cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
#                 cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)  # Draw on canvas
#
#             xp, yp = x1, y1
#
#     # Setting the header image
#     img[0:128, 0:1280] = header
#     cv2.imshow("Image", img)
#     cv2.imshow("Canvas", imgCanvas)
#     cv2.imshow("Inv", img)
#     cv2.waitKey(1)

# #
# import cv2
# import numpy as np
# import time
# import os
#
# from HandTrackingModule import handDetector as htm  # Assuming handDetector is defined in HandTrackingModule.py
#
# brushThickness = 25
# eraserThickness = 100
#
# folderPath = "Header"
# myList = os.listdir(folderPath)
# print(myList)
# overlayList = []
# for imPath in myList:
#     image = cv2.imread(f'{folderPath}/{imPath}')
#     if image is None:
#         print(f"Error loading image: {imPath}")
#         continue  # Skip to the next image if loading fails
#     overlayList.append(image)
# print(len(overlayList))
# header = overlayList[0]
# drawColor = (255, 0, 255)  # Adjust this for a visible color
#
# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 720)
#
# detector = htm(detectionCon=0.65, maxHands=1)
# xp, yp = 0, 0  # Initialize outside the loop
#
# imgCanvas = np.zeros((720, 1280, 3), np.uint8)  # Create a separate canvas
#
# def fingersUp(self):
#     fingers = []
#
#     if self.results.multi_hand_landmarks:  # Check if hand detection is successful
#         myHand = self.results.multi_hand_landmarks[0]  # Access the first hand
#         for id, lm in enumerate(myHand.landmark):
#             # Assuming you're using MediaPipe Solutions for hand landmarks
#             # Replace this placeholder with logic to determine finger states
#             # based on landmark positions and thresholds
#             # Here's an example using z-coordinate (depth) for simplicity:
#             if lm.z < 0.1:  # Adjust threshold based on your setup
#                 fingers.append(1)  # Finger is up (closer to camera)
#             else:
#                 fingers.append(0)  # Finger is down (farther from camera)
#     else:  # Handle hand detection failure (optional)
#         print("Hand detection failed")
#         # You can return a specific value (e.g., None) or raise an exception here
#
#     return fingers
#
#
# while True:
#
#     # 1. Import image
#     success, img = cap.read()
#     if not success:
#         print("Ignoring empty camera frame")
#         continue
#
#     img = cv2.flip(img, 1)  # Flip the image horizontally (optional)
#
#     # 2. Find Hand Landmarks
#     img = detector.findHands(img, draw=True)  # Draw landmarks for visualization
#     lmList = detector.findPosition(img)
#
#     if len(lmList) != 0:
#         # Tip of index finger
#         x1, y1 = lmList[8][1:]
#
#         # 3. Check which fingers are up
#         fingers = detector.fingersUp()
#
#         # 4. Selection Mode - Two finger are up (handle empty fingers list)
#         if len(fingers) >= 2 and fingers[1] and fingers[2]:
#             print("Selection Mode")
#             if y1 < 125:
#                 if 250 < x1 < 450:
#                     header = overlayList[0]
#                     drawColor = (255, 0, 255)
#                 elif 550 < x1 < 750:
#                     header = overlayList[1]
#                     drawColor = (255, 0, 0)
#                 elif 800 < x1 < 950:
#                     header = overlayList[2]
#                     drawColor = (0, 255, 0)
#                 elif 1050 < x1 < 1200:
#                     header = overlayList[3]
#                     drawColor = (0, 0, 0)  # Black for eraser
#                 cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)
#
#         # 5. Drawing Mode - Index finger is up
#         if len(fingers) >= 1 and fingers[1]:  # Check for at least one finger up and index finger specifically
#             cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
#             print("Drawing Mode")
#             if xp == 0 and yp == 0:
#                 xp, yp = x1, y1
#
#             # Draw line based on drawing color
#             if drawColor == (0, 0, 0):  # Eraser mode
#                 cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
#                 cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)  # Erase on canvas
#             else:  # Drawing mode
#                 cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
#                 cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)  # Draw on canvas
#
#             xp, yp = x1, y1
#
#
#     # Setting the header image
#     img[0:128, 0:1280] = header
#     #img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)
#     cv2.imshow("Image", img)
#     # cv2.imshow("Canvas", imgCanvas)
#     # cv2.imshow("Inv", img)
#     cv2.waitKey(1)


#
# import cv2
# import numpy as np
# import time
# import os
# import HandTrackingModule as htm
#
#
# def virtual_Painter():
#     # print("started")
#     brushThickness = 5
#     eraserThickness = 150
#     folderPath = "Header"
#     myList = os.listdir(folderPath)
#     # print(myList)
#     overlayList = []
#     for imPath in myList:
#         image = cv2.imread(f'{folderPath}/{imPath}')
#         overlayList.append(image)
#     # print(len(overlayList))
#     header = overlayList[0]
#     drawColor = (255, 0, 255)
#     shape = 'freestyle'
#     cap = cv2.VideoCapture(0)
#     cap.set(3, 1280)
#     cap.set(4, 720)
#
#     detector = htm.handDetector(detectionCon=0.85, maxHands=1)
#     xp, yp = 0, 0
#     imgCanvas = np.zeros((720, 1280, 3), np.uint8)
#     while True:
#
#         # 1. Import image
#         success, img = cap.read()
#         img = cv2.flip(img, 1)
#
#         # 2. Find Hand Landmarks
#         img = detector.findHands(img)
#         lmList = detector.findPosition(img, draw=False)
#
#         if len(lmList) != 0:
#             # print(lmList)
#
#             # tip of index and middle fingers
#             x1, y1 = lmList[8][1:]
#             x2, y2 = lmList[12][1:]
#             x0, y0 = lmList[4][1:]
#             # 3. Check which fingers are up
#             fingers = detector.fingersUp()
#             # print(fingers)
#
#             # 4. If Selection Mode - Two finger are up
#             if len(fingers) >= 2 and fingers[1] and fingers[2]:
#                 xp, yp = 0, 0
#                 # print("Selection Mode")
#                 # # Checking for the click
#                 if y1 < 120:
#                     if 250 < x1 < 450:
#                         header = overlayList[0]
#                         drawColor = (255, 0, 255)
#                     elif 550 < x1 < 750:
#                         header = overlayList[1]
#                         drawColor = (255, 0, 0)
#                     elif 800 < x1 < 950:
#                         header = overlayList[10]
#                         drawColor = (0, 255, 0)
#                     elif 1050 < x1 < 1200:
#                         header = overlayList[5]
#                         drawColor = (0, 0, 0)
#                 if y1 > 120 and y1 < 210:
#                     if x1 < 250:
#                         header = overlayList[9]
#
#                     elif 250 < x1 < 450 and drawColor == (255, 0, 255):
#                         header = overlayList[0]
#                         shape = 'freestyle'
#                     elif 550 < x1 < 750 and drawColor == (255, 0, 255):
#                         header = overlayList[6]
#                         shape = 'circle'
#                     elif 800 < x1 < 950 and drawColor == (255, 0, 255):
#                         header = overlayList[7]
#                         shape = 'rectangle'
#                     elif 1050 < x1 < 1200 and drawColor == (255, 0, 255):
#                         header = overlayList[8]
#                         shape = 'elipse'
#                     elif 250 < x1 < 450 and drawColor == (255, 0, 0):
#                         header = overlayList[10]
#                         shape = 'freestyle'
#                     elif 550 < x1 < 750 and drawColor == (255, 0, 0):
#                         header = overlayList[11]
#                         shape = 'circle'
#                     elif 800 < x1 < 950 and drawColor == (255, 0, 0):
#                         header = overlayList[12]
#                         shape = 'rectangle'
#                     elif 1050 < x1 < 1200 and drawColor == (255, 0, 0):
#                         header = overlayList[13]
#                         shape = 'elipse'
#                     if 250 < x1 < 450 and drawColor == (0, 255, 0):
#                         header = overlayList[1]
#                         shape = 'freestyle'
#                     elif 550 < x1 < 750 and drawColor == (0, 255, 0):
#                         header = overlayList[2]
#                         shape = 'circle'
#                     elif 800 < x1 < 950 and drawColor == (0, 255, 0):
#                         header = overlayList[3]
#                         shape = 'rectangle'
#                     elif 1050 < x1 < 1200 and drawColor == (0, 255, 0):
#                         header = overlayList[4]
#                         shape = 'elipse'
#                 cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)
#             if len(fingers) >= 1 and fingers[1]:
#                 cv2.circle(img, (x1, y1), 15, drawColor)
#                 # print("Drawing Mode")
#                 if xp == 0 and yp == 0:
#                     xp, yp = x1, y1
#
#                 cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
#
#                 if drawColor == (0, 0, 0):
#                     eraserThickness = 50
#                     z1, z2 = lmList[4][1:]
#                     # print(z1,z2)
#                     result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
#                     # print(result)
#                     if result < 0:
#                         result = -1 * result
#                     u = result
#                     if fingers[1] and fingers[4]:
#                         eraserThickness = u
#                     # print(eraserThickness)
#                     cv2.putText(img, str("eraserThickness="), (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
#                     cv2.putText(img, str(int(eraserThickness)), (450, 700), cv2.FONT_HERSHEY_PLAIN, 3,
#                                 (255, 0, 255), 3)
#                     cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
#                     cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
#
#                 else:
#                     brushThickness = 5
#                     # z1, z2 = lmList[4][1:]
#                     # print(z1,z2)
#                     # result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
#                     # print(result)
#                     # if result < 0:
#                     #     result = -1 * result
#                     # u = result
#                     # brushThickness = int(u)
#                     # print(eraserThickness)
#
#                     # draw
#                     if shape == 'freestyle':
#                         z1, z2 = lmList[4][1:]
#                         # print(z1,z2)
#                         result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
#                         # print(result)
#                         if result < 0:
#                             result = -1 * result
#                         u = result
#                         cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
#                         if u <= 25:
#                             cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
#                             cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
#                         cv2.putText(img, str(u), (600, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
#                         cv2.putText(img, str("brushThickness="), (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
#                         cv2.putText(img, str(int(brushThickness)), (450, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255),
#                                     3)
#
#                     # Rectangle
#                     if shape == 'rectangle':
#                         z1, z2 = lmList[4][1:]
#                         # print(z1,z2)
#                         result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
#                         # print(result)
#                         if result < 0:
#                             result = -1 * result
#                         u = result
#                         cv2.rectangle(img, (x0, y0), (x1, y1), drawColor)
#                         cv2.putText(img, "Length of Diagonal = ", (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
#                         cv2.putText(img, str(u), (530, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
#                         if fingers[4]:
#                             cv2.rectangle(imgCanvas, (x0, y0), (x1, y1), drawColor)
#                             cv2.circle
#
#                     # Circle
#                     if shape == 'circle':
#                         z1, z2 = lmList[4][1:]
#                         # print(z1,z2)
#                         result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
#                         # print(result)
#                         if result < 0:
#                             result = -1 * result
#                         u = result
#                         cv2.putText(img, "Radius Of Circe = ", (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
#                         cv2.putText(img, str(u), (450, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
#                         cv2.circle(img, (x0, y0), u, drawColor)
#                         if fingers[4]:
#                             cv2.circle(imgCanvas, (x0, y0), u, drawColor)
#
#                     # Ellipse
#                     if shape == 'elipse':
#                         z1, z2 = lmList[4][1:]
#                         # cv2.ellipse(img,(x1,y1),(int(z1/2),int(z2/2)),0,0,360,255,0)
#                         a = z1 - x1
#                         b = (z2 - x2)
#                         if x1 > 250:
#                             b = int(b / 2)
#                         if a < 0:
#                             a = -1 * a
#                         if b < 0:
#                             b = -1 * b
#                         cv2.ellipse(img, (x1, y1), (a, b), 0, 0, 360, 255, 0)
#                         cv2.putText(img, "Major AL, Minor AL = ", (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
#                         cv2.putText(img, str(a), (550, 700), cv2.FONT_HERSHEY_PLAIN, 3, (123, 20, 255), 3)
#                         cv2.putText(img, str(b), (700, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
#                         if fingers[4]:
#                             cv2.ellipse(imgCanvas, (x1, y1), (a, b), 0, 0, 360, 255, 0)
#
#                 xp, yp = x1, y1
#
#             # Clear Canvas when 2 fingers are up
#             if len(fingers) >= 1 and fingers[1]:
#                 imgCanvas = np.zeros((128, 1280, 3), np.uint8)
#
#         imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
#         _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
#         imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
#         img = cv2.bitwise_and(img, imgInv)
#         img = cv2.bitwise_or(img, imgCanvas)
#
#         # Setting the header image
#         img[0:128, 0:1280] = header
#         # img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
#
#         cv2.imshow("Image", img)
#         # cv2.imshow("Canvas", imgCanvas)
#         # cv2.imshow("Inv", imgInv)
#         cv2.waitKey(1)
#
#
# virtual_Painter()
#
#
#

#import cv2
# import numpy as np
# import time
# import os
#
# from HandTrackingModule import handDetector as htm  # Assuming handDetector is defined in HandTrackingModule.py
#
# brushThickness = 25
# eraserThickness = 100
#
# folderPath = "Header"
# myList = os.listdir(folderPath)
# print(myList)
# overlayList = []
# for imPath in myList:
#     image = cv2.imread(f'{folderPath}/{imPath}')
#     if image is None:
#         print(f"Error loading image: {imPath}")
#         continue  # Skip to the next image if loading fails
#     overlayList.append(image)
# print(len(overlayList))
# header = overlayList[0]
# drawColor = (255, 0, 255)  # Adjust this for a visible color
#
# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 720)
#
# detector = htm(detectionCon=0.65, maxHands=2)
# xp, yp = 0, 0  # Initialize outside the loop
#
# imgCanvas = np.zeros((720, 1280, 3), np.uint8)  # Create a separate canvas
#
# def fingersUp(self):
#     fingers = []
#
#     if self.results.multi_hand_landmarks:  # Check if hand detection is successful
#         myHand = self.results.multi_hand_landmarks[0]  # Access the first hand
#         for id, lm in enumerate(myHand.landmark):
#             # Assuming you're using MediaPipe Solutions for hand landmarks
#             # Replace this placeholder with logic to determine finger states
#             # based on landmark positions and thresholds
#             # Here's an example using z-coordinate (depth) for simplicity:
#             if lm.z < 0.1:  # Adjust threshold based on your setup
#                 fingers.append(1)  # Finger is up (closer to camera)
#             else:
#                 fingers.append(0)  # Finger is down (farther from camera)
#     else:  # Handle hand detection failure (optional)
#         print("Hand detection failed")
#         # You can return a specific value (e.g., None) or raise an exception here
#
#     return fingers
#
#
# while True:
#
#     # 1. Import image
#     success, img = cap.read()
#     if not success:
#         print("Ignoring empty camera frame")
#         continue
#
#     img = cv2.flip(img, 1)  # Flip the image horizontally (optional)
#
#     # 2. Find Hand Landmarks
#     img = detector.findHands(img, draw=True)  # Draw landmarks for visualization
#     lmList = detector.findPosition(img)
#
#     if len(lmList) != 0:
#         # Tip of index finger
#         x1, y1 = lmList[8][1:]
#
#         # 3. Check which fingers are up
#         fingers = detector.fingersUp()
#
#         # 4. Selection Mode - Two finger are up (handle empty fingers list)
#         if len(fingers) >= 2 and fingers[1] and fingers[2]:
#             xp, yp = 0, 0
#             print("Selection Mode")
#             # # Checking for the click
#             if y1 < 125:
#                 if 250 < x1 < 450:
#                     header = overlayList[0]
#                     drawColor = (255, 0, 255)
#                 elif 550 < x1 < 750:
#                     header = overlayList[1]
#                     drawColor = (255, 0, 0)
#                 elif 800 < x1 < 950:
#                     header = overlayList[2]
#                     drawColor = (0, 255, 0)
#                 elif 1050 < x1 < 1200:
#                     header = overlayList[3]
#                     drawColor = (0, 0, 0)
#             cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)
#
#         # 5. Drawing Mode - Index finger is up
#         if len(fingers) >= 1 and fingers[1]:  # Check for at least one finger up and index finger specifically
#             cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
#             print("Drawing Mode")
#             if xp == 0 and yp == 0:
#                 xp, yp = x1, y1
#
#             cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
#
#             if drawColor == (0, 0, 0):
#                 cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
#                 cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
#
#             else:
#                 cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
#                 cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
#
#             xp, yp = x1, y1
#
#
#     # Setting the header image
#     img[0:128, 0:1280] = header
#     img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)
#     cv2.imshow("Image", img)
#     cv2.imshow("Canvas", imgCanvas)
#     cv2.imshow("Inv", img)
#     cv2.waitKey(1)

#
# import cv2
# import numpy as np
# import time
# import os
#
# from HandTrackingModule import handDetector as htm
#
# brushThickness = 25
# eraserThickness = 100
#
# folderPath = "Header"
# myList = os.listdir(folderPath)
# print(myList)
# overlayList = []
# for imPath in myList:
#     image = cv2.imread(f'{folderPath}/{imPath}')
#     if image is None:
#         print(f"Error loading image: {imPath}")
#         continue
#     overlayList.append(image)
# print(len(overlayList))
# header = overlayList[0]
# drawColor = (255, 0, 255)
#
# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 720)
#
# detector = htm(detectionCon=0.65, maxHands=2)
# xp, yp = 0, 0
#
# imgCanvas = np.zeros((720, 1280, 3), np.uint8)
# #imgCanvas[:]= (255,255,255)
#
# def fingersUp(self):
#     fingers = []
#
#     if self.results.multi_hand_landmarks:
#         myHand = self.results.multi_hand_landmarks[0]  # Access the first hand
#         for id, lm in enumerate(myHand.landmark):
#             # ... finger detection logic based on landmark positions ...
#             pass
#
#     return fingers
#
# while True:
#     success, img = cap.read()
#     if not success:
#         print("Ignoring empty camera frame")
#         continue
#
#     img = cv2.flip(img, 1)
#
#     img = detector.findHands(img, draw=True)
#     lmList = detector.findPosition(img)
#
#     if len(lmList) != 0:
#         x1, y1 = lmList[8][1:]
#         fingers = fingersUp(detector)
#
#         if len(fingers) >= 2 and fingers[1] and fingers[2]:
#             xp, yp = 0, 0
#             if y1 < 125:
#                 if 250 < x1 < 450:
#                     header = overlayList[0]
#                     drawColor = (255, 0, 255)
#                 elif 550 < x1 < 750:
#                     header = overlayList[1]
#                     drawColor = (255, 0, 0)
#                 elif 800 < x1 < 950:
#                     header = overlayList[2]
#                     drawColor = (0, 255, 0)
#                 elif 1050 < x1 < 1200:
#                     header = overlayList[3]
#                     drawColor = (0, 0, 0)
#
#         if len(fingers) >= 1 and fingers[1]:
#             cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
#             if xp == 0 and yp == 0:
#                 xp, yp = x1, y1
#
#             cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
#
#             if drawColor == (0, 0, 0):
#                 cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
#
#             xp, yp = x1, y1
#
#     img[0:128, 0:1280] = header
#
#     cv2.imshow("Canvas", imgCanvas)
#
#     cv2.imshow("Image", img)
#
#     cv2.waitKey(1)