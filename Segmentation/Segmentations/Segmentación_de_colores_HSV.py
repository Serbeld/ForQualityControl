# encoding: utf-8 

# Programador Sergio Luis Beleño Díaz
# 9.Nov.2019

import cv2
import numpy as np
 
imagen = cv2.imread('imagen_7.png')
imagen = cv2.resize(imagen, (300,300))
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

#Mostrar la mascara final y la imagen
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Rojo', mascara_Rojo)
cv2.imshow('Dorado', mascara_Dorado)
cv2.imshow('Negro', mascara_Negro)
 
#Salir con la letra "q"
while(True):
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break 
 
cv2.destroyAllWindows()