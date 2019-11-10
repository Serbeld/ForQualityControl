# encoding: utf-8 

# Programador Sergio Luis Beleño Díaz
# 9.Nov.2019

import cv2
import numpy as np
 
imagen = cv2.imread('1.png')
imagen = cv2.resize(imagen, (300,300))
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
fr = 1.042 # Factor de multiplicación de Paint

#Rango de colores detectados:

#Rojo:
Rojo_bajos = np.array([int(225*fr),int(66*fr),int(60*fr)], dtype=np.uint8)
Rojo_altos = np.array([int(238*fr),int(118*fr),int(140*fr)], dtype=np.uint8)

#Rojo2:
Rojo_bajos2 = np.array([int(0*fr),int(70*fr),int(50*fr)], dtype=np.uint8)
Rojo_altos2 = np.array([int(12*fr),int(240*fr),int(168*fr)], dtype=np.uint8)

#Dorado:
Dorado_bajos = np.array([0,0,0], dtype=np.uint8)
Dorado_altos = np.array([0,0,0], dtype=np.uint8)

#Negro:
Negro_bajos = np.array([35,36,48], dtype=np.uint8)
Negro_altos = np.array([57,68,92], dtype=np.uint8)

#Crear las mascaras
mascara_Rojo = cv2.inRange(hsv, Rojo_bajos, Rojo_altos)
mascara_Rojo2 = cv2.inRange(hsv, Rojo_bajos2, Rojo_altos2)
mascara_Dorado = cv2.inRange(hsv, Dorado_bajos, Dorado_altos)
mascara_Negro = cv2.inRange(hsv, Negro_bajos, Negro_altos)

mascara_Rojo = cv2.add(mascara_Rojo, mascara_Rojo2)

#Mostrar la mascara final y la imagen
cv2.imshow('Rojo', mascara_Rojo)
cv2.imshow('Dorado', mascara_Dorado)
cv2.imshow('Negro', mascara_Negro)
 
#Salir con la letra "q"
while(True):
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break 
 
cv2.destroyAllWindows()