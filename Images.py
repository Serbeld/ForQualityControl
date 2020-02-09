# encoding: utf-8 

# Images.py
# Este código va orientado a la toma de imágenes de video mediante la librería open cv en Python...
# Genera un número finito de imagenes en la carpeta enumerandolas del 1 al final de la toma de datos
# Para finalizar la toma de datos pulsa la tecla Q minúscula "q"

# Programador Sergio Luis Beleño Díaz
# 29.Octubre.2019

#Para empezar se importa la librería de Open cv para visión Artificial

import cv2
import os
#import vlc
#import time

# Asignamos la cámara ingresando cv2.VideoCapture(0)
# Si quiere asignar una segunda cámara externa puede usar cv2.VideoCapture(1)
cap = cv2.VideoCapture('C3.mp4')

formato = '.jpg'
name = 11637
tipo = 'Background_'

# Toma parámetros de captura de la cámara
[rec, camara] = cap.read()

while(rec == 1):

	# Toma parámetros de captura de la cámara
	[rec, camara] = cap.read()
	name = name + 1 # Contador de imagenes tomadas

	# Muestra la imagen tomada en una ventana
	if (rec ==1):


		#cv2.imshow('Captura', camara)
		file = str(tipo) + str(name) + formato
		# rotation angle in degree
		camara = cv2.resize(camara, None, fx = 0.7, fy= 0.7)
		camara = camara[0:480, 0:640]

		# Reescala la imagen
		#camara = cv2.resize(camara, (240,320))

		cv2.imshow('Camara',camara)

		if name%8 == 0:
			# Guarda la imagen tomada
			cv2.imwrite('7_Background/'+file,camara)
			contador_de_retardo = 0

		print("Imagen numero: " + str(name))

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#plays = vlc.MediaPlayer("Beep_Short.mp3")
#plays.play()
#time.sleep(1)

cap.release()
cv2.destroyAllWindows()
