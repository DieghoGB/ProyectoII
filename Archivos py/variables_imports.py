import face_recognition
import cv2
import os
import numpy as np
import tkinter
import cv2
import numpy as np
from tkinter import *
from PIL import Image
from PIL import ImageTk
import mysql
import mysql.connector


#face_recognition
path = 'Referencias imagenes'
imagenes = []
classNames = []
myList = os.listdir(path)
print(myList)
cap = None
root = Tk()




try:
    conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='n1k_lh345',
    database='buscados'
    )
    id=1111111
    cursor = conexion.cursor()
    consultaBD = "select * from datosbuscados where rut = %s"
    # asignar variable en la consulta
    cursor.execute(consultaBD, (id,))
    registro = cursor.fetchall()
    for columna in registro:

            
        print("Rut: ",columna[0])
        print("Nombre: ",columna[1])
        print("Apellido: ",columna[2])
        if columna[3] == 1:
            print("Antecendentes Penales: Si")
        else:
            print("Antecedentes Penales: No")
        if columna[4] == 1:
            print("Antecendentes Penales: Si")
        else:
            print("Antecedentes Penales: No")
except mysql.connector.Error as e:
    print("Error al obtener el registro de la tabla MySQL")
finally:
    if conexion.is_connected():
        conexion.close()
        cursor.close()
        print("La conexion MySQL se ha cerrado")


sql_select_Query = "select * from datosbuscados "






'''
rostroLoc = face_recognition.face_locations(imgHouse)[0]
encodeHouse = face_recognition.face_encodings(imgHouse)[0]
cv2.rectangle(imgHouse, (rostroLoc[3],rostroLoc[0]), (rostroLoc[1],rostroLoc[2]), (255, 0, 255), 2)

rsotroLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (rsotroLocTest[3],rsotroLocTest[0]), (rsotroLocTest[1],rsotroLocTest[2]), (255, 0, 255), 2)

resultados = face_recognition.compare_faces([encodeHouse], encodeTest)
distanciaRostro = face_recognition.face_distance([encodeHouse], encodeTest)
'''