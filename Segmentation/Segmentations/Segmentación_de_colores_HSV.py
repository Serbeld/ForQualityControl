# encoding: utf-8 

# Programador Sergio Luis Beleño Díaz
# 9.Nov.2019

import cv2
import numpy as np
import random as rng

def segmentation(cap):

	[rec, imagen] = cap.read()
	#imagen = cv2.imread('imagen_1.png')
	imagen = cv2.resize(imagen, (300,300))
	#imagen[:,:,0] = cv2.blur(imagen[:,:,0] , (10,10))

	hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

	#Rango de colores detectados:

	#Rojo:
	Rojo_bajos = np.array([167,86,0], dtype=np.uint8)
	Rojo_altos = np.array([180,255,255], dtype=np.uint8)

	#Rojo2:
	Rojo_bajos2 = np.array([0,80,0], dtype=np.uint8)
	Rojo_altos2 = np.array([6,255,255], dtype=np.uint8)

	#Dorado:
	Dorado_bajos = np.array([12,76,0], dtype=np.uint8)
	Dorado_altos = np.array([47,255,255], dtype=np.uint8)

	#Negro:
	Negro_bajos = np.array([117,13,0], dtype=np.uint8)
	Negro_altos = np.array([151,255,255], dtype=np.uint8)
	Negro_bajos2 = np.array([7,70,0], dtype=np.uint8)
	Negro_altos2 = np.array([13,255,103], dtype=np.uint8)

	#Crear las mascaras
	mascara_Rojo = cv2.inRange(hsv, Rojo_bajos, Rojo_altos)
	mascara_Rojo2 = cv2.inRange(hsv, Rojo_bajos2, Rojo_altos2)
	mascara_Dorado = cv2.inRange(hsv, Dorado_bajos, Dorado_altos)
	mascara_Negro = cv2.inRange(hsv, Negro_bajos, Negro_altos)
	mascara_Negro2 = cv2.inRange(hsv, Negro_bajos2, Negro_altos2)

	mascara_Rojo = cv2.add(mascara_Rojo, mascara_Rojo2)
	mascara_Negro = cv2.add(mascara_Negro, mascara_Negro2)

	Mascara_de_la_Lata = cv2.add(mascara_Rojo, mascara_Dorado, mascara_Negro)

	#Areas de los componentes
	Area_Roja = centroide(mascara_Rojo)
	Area_Dorada = centroide(mascara_Dorado)
	Area_Negra = centroide(mascara_Negro)
	[Area_Total, x, y] = centroide(Mascara_de_la_Lata)

	threshold = 200
	canny_output = cv2.Canny(Mascara_de_la_Lata,0,600)

	contour = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
	contours = contour[0]
	contours_poly = [None]*len(contours)
	boundRect = [None]*len(contours)
	centers = [None]*len(contours)

	for i, c in enumerate(contours):
		contours_poly[i] = cv2.approxPolyDP(c, 3, True)
		boundRect[i] = cv2.boundingRect(contours_poly[i])

	for i in range(len(contours)):
		color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
		cv2.drawContours(imagen, contours_poly, i, color)
		cv2.rectangle(imagen, (int(boundRect[i][0]), int(boundRect[i][1])), \
			(int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)


	#Mostrar la mascara final y la imagen
	cv2.imshow('Imagen Original', imagen)
	cv2.imshow('Rojo', mascara_Rojo)
	cv2.imshow('Dorado', mascara_Dorado)
	cv2.imshow('Negro', mascara_Negro)
	#cv2.imshow('Lata', Mascara_de_la_Lata)

	return rec

def centroide(Mascara):

	# Centroide
 	Moments = cv2.moments(Mascara)
 	Area = int(Moments["m00"]) #Este elemento contiene el Area

 	if (Moments["m00"] != 0):

 		# Se calcula los centroides XY con el fin de ubicar el objeto 
 		cX = int(Moments["m10"] / Moments["m00"])
 		cY = int(Moments["m01"] / Moments["m00"])
 		
 	else:
 		cX, cY = 0,0

 	return(Area, cX, cY)

############################################################################

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while(True):

	segmentation(cap)

	# Sí se pulsa una tecla y la tecla es la letra "q" 
	# minuscula se rompe el bucle en el que se encuentre
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break 

cap.release()
cv2.destroyAllWindows()