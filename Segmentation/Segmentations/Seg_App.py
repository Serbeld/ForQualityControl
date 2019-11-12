# encoding: utf-8 

# Programador Sergio Luis Beleño Díaz
# 9.Nov.2019

import cv2
import numpy as np
import random as rng

def segmentation(cap):

	[rec, imagen] = cap.read()
	#imagen = cv2.imread('imagen_1.png')
	#imagen = cv2.resize(imagen, (3260,2480))
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
	Dorado_bajos = np.array([10,0,244], dtype=np.uint8)
	Dorado_altos = np.array([115,209,255], dtype=np.uint8)
	Dorado_bajos2 = np.array([0,0,202], dtype=np.uint8)
	Dorado_altos2 = np.array([47,255,255], dtype=np.uint8)

	#Negro:
	Negro_bajos = np.array([18,0,0], dtype=np.uint8)
	Negro_altos = np.array([156,162,87], dtype=np.uint8)

	#Crear las mascaras
	mascara_Rojo = cv2.inRange(hsv, Rojo_bajos, Rojo_altos)
	mascara_Rojo2 = cv2.inRange(hsv, Rojo_bajos2, Rojo_altos2)
	mascara_Dorado = cv2.inRange(hsv, Dorado_bajos, Dorado_altos)
	mascara_Dorado2 = cv2.inRange(hsv, Dorado_bajos2, Dorado_altos2)
	mascara_Negro_1 = cv2.inRange(hsv, Negro_bajos, Negro_altos)

	mascara_Rojo = cv2.add(mascara_Rojo, mascara_Rojo2)
	mascara_Dorado = cv2.add(mascara_Dorado, mascara_Dorado2)

	#Filtro morfológico

	# Definimos el Kernel
	kernel = np.ones((10,10),np.uint8)
	kernel2 = np.ones((20,20),np.uint8)
	# Opening
	#mascara_Rojo = cv2.morphologyEx(mascara_Rojo, cv2.MORPH_OPEN,kernel)
	# Opening
	mascara_Rojo = cv2.morphologyEx(mascara_Rojo, cv2.MORPH_CLOSE,kernel)
	mascara_Dorado = cv2.morphologyEx(mascara_Dorado, cv2.MORPH_CLOSE,kernel)
	mascara_Negro_1 = cv2.morphologyEx(mascara_Negro_1, cv2.MORPH_CLOSE,kernel)
	# Dilate
	mascara_Rojo = cv2.morphologyEx(mascara_Rojo, cv2.MORPH_DILATE,kernel2)
	mascara_Dorado = cv2.morphologyEx(mascara_Dorado, cv2.MORPH_DILATE,kernel2)
	mascara_Negro_1 = cv2.morphologyEx(mascara_Negro_1, cv2.MORPH_DILATE,kernel2)

	#Mascara_de_la_Lata = dominante(mascara_Rojo,mascara_Dorado,mascara_Negro_1)

	imagen = dibujar_cajas(imagen,mascara_Rojo,(rng.randint(0,100), rng.randint(0,100), rng.randint(200,256)))
	imagen = dibujar_cajas(imagen,mascara_Dorado,(rng.randint(0,50), rng.randint(200,256), rng.randint(200,256)))
	imagen = dibujar_cajas(imagen,mascara_Negro_1,(rng.randint(0,50), rng.randint(0,50), rng.randint(0,50)))

	#Mostrar la mascara final y la imagen
	cv2.namedWindow('Imagen Original',cv2.WND_PROP_FULLSCREEN)
	cv2.setWindowProperty('Imagen Original', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	cv2.imshow('Imagen Original', imagen)
	#cv2.imshow('Rojo', mascara_Rojo)
	#cv2.imshow('Dorado', mascara_Dorado)
	#cv2.imshow('Negro', mascara_Negro_1)
	#cv2.imshow('Lata', Mascara_de_la_Lata)

	return rec

def Area(Mascara):

	# Centroide
 	Moments = cv2.moments(Mascara)
 	Area = int(Moments["m00"]) #Este elemento contiene el Area

 	return(Area)
'''
def dominante(mascara_Rojo,mascara_Dorado,mascara_Negro_1):
	#Areas de los componentes
	Area_Roja = Area(mascara_Rojo)
	Area_Dorada = Area(mascara_Dorado)
	Area_Negra = Area(mascara_Negro_1)

	if Area_Roja >= Area_Dorada and Area_Roja >= Area_Negra:
		return mascara_Rojo

	if Area_Dorada >= Area_Roja and Area_Dorada >= Area_Negra:
		return mascara_Dorado

	if Area_Negra >= Area_Dorada and Area_Negra >= Area_Roja:
		return mascara_Negro_1
'''
def dibujar_cajas(imagen,Mascara,color):

	number_of_size = 100 # Objetos inferiores a un area de number_of_size se desvanecen
	min_canny = 20
	max_canny = 100

	canny_output = cv2.Canny(Mascara,min_canny,max_canny)

	contour = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
	contours = contour[0]
	contours_poly = [None]*len(contours)
	boundRect = [None]*len(contours)
	centers = [None]*len(contours)

	for i, c in enumerate(contours):
		contours_poly[i] = cv2.approxPolyDP(c, 3, True)
		boundRect[i] = cv2.boundingRect(contours_poly[i])

	for i in range(len(contours)):
		#color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
		#color = (255,0,0)
		#color = (rng.randint(200,256), rng.randint(200,256), rng.randint(200,256))

		if boundRect[i][3] >= number_of_size and boundRect[i][1]>= number_of_size:
			cv2.rectangle(imagen, (int(boundRect[i][0]), int(boundRect[i][1])), \
				(int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)

	return imagen

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