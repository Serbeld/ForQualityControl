from colorfilters import HSVFilter
import cv2 as cv

img = cv.imread("6.png")
window = HSVFilter(img)
window.show()

print(f"Image filtered in HSV between {window.lowerb} and {window.upperb}.")
#Image filtered in HSV between [51, 0, 183] and [63, 255, 255].