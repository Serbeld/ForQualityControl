# encoding: utf-8 

# Programador Sergio Luis Beleño Díaz
# 9.Nov.2019

import cv2
import numpy as np
 
imagenBGR = cv2.imread('10.png')
imagenBGR = cv2.resize(imagenBGR,(300,300))

cv2.imshow('Imagen Original', imagenBGR)

#Rango de colores detectados:
#Rojo:
#Rojo_bajos = np.array([41,45,77], dtype=np.uint8)
#Rojo_altos = np.array([73,71,148], dtype=np.uint8)
#Dorado:
#Dorado_bajos = np.array([0,0,0], dtype=np.uint8)
#Dorado_altos = np.array([0,0,0], dtype=np.uint8)

#Negro:
Negro_bajos = np.array([35,36,48], dtype=np.uint8)
Negro_altos = np.array([57,68,92], dtype=np.uint8)

#Crear las mascaras
#mascara_Rojo = cv2.inRange(imagenBGR, Rojo_bajos, Rojo_altos)
#mascara_Dorado = cv2.inRange(imagenBGR, Dorado_bajos, Dorado_altos)
mascara_Negro = cv2.inRange(imagenBGR, Negro_bajos, Negro_altos)
 
#Mostrar la mascara final y la imagen
#cv2.imshow('Rojo', mascara_Rojo)
#cv2.imshow('Dorado', mascara_Dorado)
cv2.imshow('Negro', mascara_Negro)
 
#Salir con la letra "q"
while(True):
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break 
 
cv2.destroyAllWindows()