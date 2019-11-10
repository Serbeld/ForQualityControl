import cv2
import numpy as np

######################################################################################################

def control(nombre):
	
	imagen = cv2.imread(nombre)				       # Lee la imagen 
	#imagen = cv2.resize(imagen, (400,400))		   # redimensiona la imagen 

	# Binarización
	PromR = int((229+254+219+246+243+150+169+153)/8)
	PromG = int((107+105+101+120+98+57+76+41)/8)
	PromB = int((83+82+87+124+81+65+59+19)/8)
	colores_bajos = np.array([19,41,150], dtype=np.uint8)
	colores_altos = np.array([130, 115, 255], dtype=np.uint8)
	Mascara = cv2.inRange(imagen, colores_bajos, colores_altos)

	# Momentos
	Moments = cv2.moments(Mascara)
	area = int(Moments['m00'])
	print("El Area de la lata es de "+str(area) +" pixeles")

	if (Moments["m00"] != 0):
		# Se calcula los centroides XY con el fin de ubicar el objeto 
		centrox = int(Moments["m10"] / Moments["m00"])
		centroy = int(Moments["m01"] / Moments["m00"])

	else:
		centrox, centroy = 0,0

	cv2.rectangle(imagen,(int(centrox-(area*2E-5)-20), int(centroy-(area*3E-5)-20)),(int(centrox+(area*2E-5)+20), int(centroy+(area*3E-5)+20)), (177, 66, 75),3);
	cv2.putText(imagen,"Lata",(centrox-190,centroy),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.5,(177, 66, 75),2)
	print (centrox, centroy)

	cv2.imshow('Imagen de la camara',imagen)
	cv2.imshow('Binarizada',Mascara)

	return(centrox, centroy)

#####################################################################################################

formato = ".jpg"			# Formato de las imagenes
Ndata = 4					# Número de imagenes

for cond_i in range (0,Ndata):
	nombre = str(cond_i+1)+formato    # Nombre de la imagen actual
	[x,y] = control(nombre)	          # Area optenida del cultivo
	cv2.waitKey(0)
cv2.destroyAllWindows()