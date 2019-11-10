# encoding: utf-8 

# Color_Dominante_clusters.py
# Este código va orientado a la toma de imágenes de video mediante la librería open cv en Python...

# Programador Sergio Luis Beleño Díaz
# 9.Nov.2019

import numpy as np
import cv2, os

number = '12'
dir = "C:/Users/SerBeld/Desktop/Design_of_applications_through_the_use_of_artificial_vision_for_quality_control/Segmentation/Segmentation_HSV_AND_RGB/Colores_Dominantes"
file = number + '.png'

img = cv2.imread(number + '.png')
img = cv2.resize(img,(1000,1000))
Z = img.reshape((-1,3))

# Convierte a np.float32
Z = np.float32(Z)

# Criterio, número de clusters(K) y aplica algoritmo de kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 10
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Convierte a uint8, y crea la imagen
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

# Crea la imagen
cv2.imwrite(os.path.join(dir,file),res2)

#cv2.imshow('res2',res2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()