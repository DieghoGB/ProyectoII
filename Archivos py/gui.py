import face_recognition
import cv2
import os
import numpy as np
import tkinter
import cv2
import numpy as np
from tkinter import * 
import mysql.connector
from PIL import Image
from PIL import ImageTk
from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils

conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='n1k_lh345',
        database='buscados'
            )
cursor = conexion.cursor()


sql_select_Query = "select * from datosbuscados "
        # asignar variable en la consulta
cursor.execute(sql_select_Query)
        # obtener resultado
registro = cursor.fetchall()
for columna in registro:
    print("rut= ",  columna[0])
    rut=columna[0]
    print("nombre= ", columna[1] , "\n")

cap = cv2.VideoCapture(0)
flag = cap.isOpened()
while(flag):
	index=rut 
 	ret, frame = cap.read()
   	cv2.imshow("Capture_Paizhao",frame)
    k = cv2.waitKey(1) & 0xFF
	if k == ord ('s'): #Presione la tecla s para ingresar a la siguiente operación de guardado de imágenes
    	print(rut)
        print(f'{path}/')
        cv2.imwrite(f'{path}/' + rut + ".jpg", frame)
        print("save" + rut + ".jpg successfuly!")
        print("-------------------------")
    elif k == ord ('q'): #Presione la tecla q, el programa sale
		break
	cap.release()
    cv2.destroyAllWindows()