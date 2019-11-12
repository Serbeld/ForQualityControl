from colorfilters import HSVFilter
import cv2 as cv

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
[rec, imagen] = cap.read()
img = imagen

#img = cv.imread("black.png")
img = cv.resize(img,(300,300))
window = HSVFilter(img)
window.show()

print(f"Image filtered in HSV between {window.lowerb} and {window.upperb}.")
#Image filtered in HSV between [51, 0, 183] and [63, 255, 255].