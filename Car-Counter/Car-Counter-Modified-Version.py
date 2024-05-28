from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *;
# cap = cv2.VideoCapture(0)# For webcam
# cap.set(3, 1280)
# cap.set(4, 720)
cap = cv2.VideoCapture("car.mp4")

model = YOLO(" ../Yolo-Weights/yolov8n.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]
mask = cv2.imread("mask.png")

if mask is None:
    print("Error: Couldn't load the mask image.")

#Tracking
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

limits = [350,297,670,297]
totalCount = []


while True:
    success, img = cap. read()
    imgRegion = cv2.bitwise_and(img, mask)

    imgGraphics = cv2.imread("graphics.png", cv2.IMREAD_UNCHANGED)
    img = cvzone.overlayPNG(img, imgGraphics, (0, 0))
    results = model(imgRegion, stream=True)


    detection = np.empty((0,5))


    for r in results:
        boxes = r.boxes
        for box in boxes:
            #Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            #cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # x1, y1, w, h = box.xywh[0]
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h), l = 9,rt = 5)

            #Confidence
            conf= math.ceil((box.conf[0] * 100)) / 100
            print(conf)
            cvzone.putTextRect(img, f'{conf}', (max(0, x1), max(35, y1)))

            #Class Name
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if currentClass == "car" or currentClass == "truck" or currentClass=="bus" or currentClass == "motorbike" and conf > 0.3:
                #cvzone.putTextRect(img, f'{currentClass}{conf} ', (max(0, x1), max(35, y1)),scale=3,thickness=3,offset=3)
                #cvzone.cornerRect(img, (x1, 1, w, h), l = 9)
                currentArray = np.array([x1,y1,x2,y2,conf])
                detection = np.vstack((detection,currentArray))

    resultsTracker = tracker.update(detection)
    cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 0, 255), 5)

    for result in resultsTracker:
        x1,y1,x2,y2,id = result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        print(result)
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img,(x1, y1, w, h), l = 9,rt = 2,colorR=(255,0,255))
        cvzone.putTextRect(img, f'{int(id)} ', (max(0, x1), max(35, y1)), scale=3, thickness=3, offset=3)


        cx,cy = x1+w//2,y1+h//2
        cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)

        if limits[0]<limits[2] and limits[1] - 15 < cy < limits[1] + 20:
            if totalCount.count(id) == 0:
                totalCount.append(id)
                cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255,0), 5)
    #cvzone.putTextRect(img, f' Count : {len(totalCount)} ', ( 50 , 50 ))
    cv2.putText(img, str(len(totalCount)), (250, 100), cv2.FONT_HERSHEY_PLAIN, 5, (50,50,355), 8)


    cv2.imshow("Image" , img)
    #cv2.imshow("ImageRegion",imgRegion)
    cv2.waitKey(1)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

