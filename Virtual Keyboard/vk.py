import cv2
import math
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller

# Create a keyboard controller
keyboard = Controller()

# Initialize the video capture object
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize the hand detector
detector = HandDetector(detectionCon=0.8)

# Define the keys for the virtual keyboard
keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]
]
finalText = ""


# Function to draw all the buttons on the virtual keyboard
def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img

# Class to represent a button on the virtual keyboard
class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

def findDistance(self, p1, p2, img=None, color=(255, 0, 255), scale=5):

        x1, y1 = p1
        x2, y2 = p2
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        length = math.hypot(x2 - x1, y2 - y1)
        info = (x1, y1, x2, y2, cx, cy)
        if img is not None:
            cv2.circle(img, (x1, y1), scale, color, cv2.FILLED)
            cv2.circle(img, (x2, y2), scale, color, cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), color, max(1, scale // 3))
            cv2.circle(img, (cx, cy), scale, color, cv2.FILLED)

        return length, info, img


# Create button instances for each key
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

# Main loop
while True:
    # Read frame from the video capture
    success, img = cap.read()
    #img = detector.findDistance(img)
    # lmList, bboxInfo = detector.findDistance(img)
    # img = drawAll(img, buttonList)
    if not success:
        continue

    # Detect hands in the frame
    hands, img = detector.findHands(img)

    # Draw all the buttons on the virtual keyboard
    img = drawAll(img, buttonList)

    # Check if hands are detected
    if hands:
        # Loop through each detected hand
        for hand in hands:
            lmList = hand["lmList"]  # List of landmarks for the hand

            for button in buttonList:
                x, y = button.pos
                w, h = button.size

                # Check if the index finger landmark is within the button boundaries
                if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                    cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    # Corrected findDistance method call
                    length, _, _ = detector.findDistance(lmList[8][0:2], lmList[12][0:2], img)

                    # If the index finger is close to the button, press the corresponding key
                    if length < 30:
                        keyboard.press(button.text)
                        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                        finalText += button.text  # Update the finalText variable with the pressed key
                        sleep(0.15)  # Add a short delay to avoid multiple key presses

    # Display final text on the virtual keyboard
    cv2.rectangle(img, (50, 350), (700, 450), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 430), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    # Show the frame with the virtual keyboard
    cv2.imshow("Virtual Keyboard", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()






# import cv2
# import math
# from cvzone.HandTrackingModule import HandDetector
# from time import sleep
# from pynput.keyboard import Controller
#
# # Create a keyboard controller
# keyboard = Controller()
#
# # Initialize the video capture object
# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 720)
#
# # Initialize the hand detector
# detector = HandDetector(detectionCon=0.8)
#
# # Define the keys for the virtual keyboard
# keys = [
#     ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
#     ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
#     ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]
# ]
# finalText = ""
#
# # Class to represent a button on the virtual keyboard
# class Button():
#     def __init__(self, pos, text, size=[85, 85]):
#         self.pos = pos
#         self.size = size
#         self.text = text
#
# # Function to draw all the buttons on the virtual keyboard
# def drawAll(img, buttonList):
#     for button in buttonList:
#         x, y = button.pos
#         w, h = button.size
#         cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
#         cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
#     return img
#
# def findDistance(self, p1, p2, img=None, color=(255, 0, 255), scale=5):
#
#         x1, y1 = p1
#         x2, y2 = p2
#         cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
#         length = math.hypot(x2 - x1, y2 - y1)
#         info = (x1, y1, x2, y2, cx, cy)
#         if img is not None:
#             cv2.circle(img, (x1, y1), scale, color, cv2.FILLED)
#             cv2.circle(img, (x2, y2), scale, color, cv2.FILLED)
#             cv2.line(img, (x1, y1), (x2, y2), color, max(1, scale // 3))
#             cv2.circle(img, (cx, cy), scale, color, cv2.FILLED)
#
#         return length, info, img
#
#
# # Create button instances for each key
# buttonList = []
# for i in range(len(keys)):
#     for j, key in enumerate(keys[i]):
#         buttonList.append(Button([100 * j + 50, 100 * i + 50], key))
#
# # Main loop
# while True:
#     # Read frame from the video capture
#     success, img = cap.read()
#     if not success:
#         continue
#
#     # Detect hands in the frame
#     hands, img = detector.findHands(img)
#
#     # Draw all the buttons on the virtual keyboard
#     img = drawAll(img, buttonList)
#
#     # Check if hands are detected
#     if hands:
#         # Loop through each detected hand
#         for hand in hands:
#             lmList = hand["lmList"]  # List of landmarks for the hand
#
#             for button in buttonList:
#                 x, y = button.pos
#                 w, h = button.size
#
#                 # Check if the index finger landmark is within the button boundaries
#                 if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
#                     cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
#                     cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
#                     # Corrected findDistance method call
#                     length, _, _ = detector.findDistance(lmList[8][0:2], lmList[12][0:2], img)
#
#                     # If the index finger is close to the button, press the corresponding key
#                     if length < 30:
#                         keyboard.press(button.text)
#                         cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
#                         cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
#                         sleep(0.15)
#
#     # Display final text on the virtual keyboard
#     cv2.rectangle(img, (50, 350), (700, 450), (175, 0, 175), cv2.FILLED)
#     cv2.putText(img, finalText, (60, 430), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
#
#     # Show the frame with the virtual keyboard
#     cv2.imshow("Virtual Keyboard", img)
#
#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release the video capture object and close all OpenCV windows
# cap.release()
# cv2.destroyAllWindows()








# import cv2
# from cvzone.HandTrackingModule import HandDetector
# from pynput.keyboard import Controller, Key
#
# # Create a keyboard controller
# keyboard = Controller()
#
# # Initialize the video capture object
# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 720)
#
# # Initialize the hand detector
# detector = HandDetector(detectionCon=0.8)
#
# # Define the keys for the virtual keyboard
# keys = [
#     ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
#     ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
#     ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]
# ]
#
# # Function to draw all the buttons on the virtual keyboard
# def drawAll(img, buttonList):
#     for button in buttonList:
#         x, y = button.pos
#         w, h = button.size
#         cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
#         cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
#     return img
#
# # Class to represent a button on the virtual keyboard
# class Button():
#     def __init__(self, pos, text, size=[85, 85]):
#         self.pos = pos
#         self.size = size
#         self.text = text
#
# # Create button instances for each key
# buttonList = []
# for i in range(len(keys)):
#     for j, key in enumerate(keys[i]):
#         buttonList.append(Button([100 * j + 50, 100 * i + 50], key))
#
# # Main loop
# while True:
#     # Read frame from the video capture
#     success, img = cap.read()
#     if not success:
#         continue
#
#     # Detect hands in the frame
#     hands, img = detector.findHands(img)
#
#     # Draw all the buttons on the virtual keyboard
#     img = drawAll(img, buttonList)
#
#     # Check if hands are detected
#     if hands:
#         # Loop through each detected hand
#         for hand in hands:
#             lmList = hand["lmList"]  # List of landmarks for the hand
#
#             for button in buttonList:
#                 x, y = button.pos
#                 w, h = button.size
#
#                 # Check if the index finger landmark is within the button boundaries
#                 if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
#                     cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
#                     cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
#
#                     # If the index finger is close to the button, press the corresponding key
#                     keyboard.press(button.text)
#
#     # Display the frame with the virtual keyboard
#     cv2.imshow("Virtual Keyboard", img)
#
#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release the video capture object and close all OpenCV windows
# cap.release()
# cv2.destroyAllWindows()
