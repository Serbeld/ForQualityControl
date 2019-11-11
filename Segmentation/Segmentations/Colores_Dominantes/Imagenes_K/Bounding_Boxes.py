from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import random as rng

rng.seed(12345)

def thresh_callback(val):

    threshold = val

    imagen = cv.imread('imagen_1.png')
    hsv = cv.cvtColor(imagen, cv.COLOR_BGR2HSV)

    #Rango de colores detectados:

    #Rojo:
    Rojo_bajos = np.array([167,86,0], dtype=np.uint8)
    Rojo_altos = np.array([180,255,255], dtype=np.uint8)

    #Rojo2:
    Rojo_bajos2 = np.array([0,80,0], dtype=np.uint8)
    Rojo_altos2 = np.array([6,255,255], dtype=np.uint8)

    #Crear las mascaras
    mascara_Rojo = cv.inRange(hsv, Rojo_bajos, Rojo_altos)
    mascara_Rojo2 = cv.inRange(hsv, Rojo_bajos2, Rojo_altos2)

    mascara_Rojo = cv.add(mascara_Rojo, mascara_Rojo2)


    #canny_output = cv.Canny(mascara_Rojo, threshold, threshold * 2)
    canny_output = cv.Canny(mascara_Rojo,threshold,threshold*2)
    
    contour = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    contours = contour[0]
    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    centers = [None]*len(contours)
    
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])
    
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    
    for i in range(len(contours)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv.drawContours(drawing, contours_poly, i, color)
        cv.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
          (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)
    
    
    cv.imshow('Contours', drawing)
    
parser = argparse.ArgumentParser(description='Code for Creating Bounding boxes and circles for contours tutorial.')
parser.add_argument('--input', help='Path to input image.', default='stuff.jpg')
args = parser.parse_args()
src = cv.imread('imagen_1.png')
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)
# Convert image to gray and blur it
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3,3))
source_window = 'Source'
cv.namedWindow(source_window)
cv.imshow(source_window, src)
max_thresh = 1000
thresh = 100 # initial threshold
cv.createTrackbar('Canny thresh:', source_window, thresh, max_thresh, thresh_callback)
thresh_callback(thresh)
cv.waitKey()