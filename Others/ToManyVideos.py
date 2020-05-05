import cv2
import numpy as np
from scipy import ndimage

cap = cv2.VideoCapture('B1.mp4') #Video1
cap2 = cv2.VideoCapture('A6.mp4') #Video2
cap3 = cv2.VideoCapture('A7.mp4') #Video3
cap4 = cv2.VideoCapture('B11.mp4') #Video4
cap5 = cv2.VideoCapture('B6.mp4') #Video5
cap6 = cv2.VideoCapture('A1.mp4') #Video6
cap7 = cv2.VideoCapture('A11.mp4') #Video7
cap8 = cv2.VideoCapture('B9.mp4') #Video8

# Toma parámetros de captura de la cámara
[rec, camara] = cap.read()
plane = cv2.resize(camara,(800,800))

def takepicture(camara):
	# rotation angle in degree
	camara = cv2.resize(camara, None, fx = 0.75, fy= 0.75)
	camara = camara[0:480, 0:640]

	# Reescala la imagen
	camara = cv2.resize(camara, (300,200))
	camara = ndimage.rotate(camara, -90)
	return camara

fourcc = cv2.VideoWriter_fourcc(*'mp4v')#configuracion de codec de video
videofps = 100
[rec, camara] = cap.read()
video_salida = cv2.VideoWriter('InOfCans.mp4',fourcc, videofps,(800, 800))# Creacion de video de salida procesado
frame_actual=0

while(rec == 1):

	# Toma parámetros de captura de la cámara
	[rec, camara] = cap.read()
	[rec1, camara2] = cap2.read()
	[rec2, camara3] = cap3.read()
	[rec3, camara4] = cap4.read()
	[rec4, camara5] = cap5.read()
	[rec5, camara6] = cap6.read()
	[rec6, camara7] = cap7.read()
	[rec7, camara8] = cap8.read()

	# Muestra la imagen tomada en una ventana
	if (rec ==1):

		plane[0:100, :] = 0
		plane[100:400, 0:200] = takepicture(camara)
		plane[100:400, 200:400] = takepicture(camara2)
		plane[100:400, 400:600] = takepicture(camara3)
		plane[100:400, 600:800] = takepicture(camara4)
		plane[400:700, 0:200] = takepicture(camara5)
		plane[400:700, 200:400] = takepicture(camara6)
		plane[400:700, 400:600] = takepicture(camara7)
		plane[400:700, 600:800] = takepicture(camara8)
		plane[700:800, :] = 0

		plane = cv2.resize(plane,(350,350))
		plane = cv2.resize(plane, (800, 800))

		video_salida.write(plane)  # grabacion de frames en el video de salida

		if (frame_actual % 10 == 0):
			print('Frame actual=' + str(frame_actual))
			cv2.imshow('Camara', plane)

		frame_actual = frame_actual + 1

	if frame_actual==7000:
		break
		
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
video_salida.release()
cv2.destroyAllWindows()
