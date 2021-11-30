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




#face_recognition
path = 'Referencias imagenes'
imagenes = []
classNames = []
myList = os.listdir(path)
print(myList)
cap = None
root = Tk()
root.geometry("1920x1080")
root.title("Reconocimiento Facial")
lblVideo = Label(root)
infoTextoLBL = tkinter.Text(root)
escanearTexto = tkinter.StringVar()
#sql parte
''''
________________________________________
|                                      |
|Poner en comentario las partes del sql|
|______________________________________|
'''''
conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='n1k_lh345',
        database='buscados'
            )
cursor = conexion.cursor(buffered=True)


'''sql_select_Query = "select * from datosbuscados "
        # asignar variable en la consulta
cursor.execute(sql_select_Query)
        # obtener resultado
registro = cursor.fetchall()
for columna in registro:
    print("rut= ",  columna[0])
    print("nombre= ", columna[1] )'''
#fin sql    





