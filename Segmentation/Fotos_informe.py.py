# encoding: utf-8 

# Fotos_informe.py
# Este código va orientado a la toma de imágenes de video mediante la librería open cv en Python...
# Reescala imagenes y las guarda

# Programador Sergio Luis Beleño Díaz
# 9.Nov.2019

#Para empezar se importa la librería de Open cv para visión Artificial

import cv2, os

# Asignamos la cámara ingresando cv2.VideoCapture(0)
# Si quiere asignar una segunda cámara externa puede usar cv2.VideoCapture(1)
cap = cv2.VideoCapture('1.png')

formato = '.png'
dir = "C:/Users/SerBeld/Desktop/Design_of_applications_through_the_use_of_artificial_vision_for_quality_control/Segmentation"
name = 'imagen_1'

# Toma parámetros de captura de la cámara
[rec, camara] = cap.read()

# Muestra la imagen tomada en una ventana
cv2.imshow('Captura', camara)
	
file = str(name) + formato
	
# Reescala la imagen a 1000x1000px
camara = cv2.resize(camara, (1000,1000))

# Guarda la imagen tomada
cv2.imwrite(os.path.join(dir,file),camara)

cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
