import cv2
import easyocr
import matplotlib.pyplot as plt
from easyocr import Reader
image_path = 'text1.jpg'
img = cv2.imread(image_path)

reader= easyocr.Reader(['en'])

text = reader.readtext(img)

# for t in text:
#     print(t)

print(text)