import cv2.cv2
import mysql.connector

from variables_imports import *


    
#sql
def datosBuscados(id,):
    try:
        conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='n1k_lh345',
        database='buscados'
            )
        cursor = conexion.cursor()
        print("Obteniendo datos...")
        sql_select_Query = "select * from datosbuscados where rut = %s"
        # asignar variable en la consulta
        cursor.execute(sql_select_Query, (id,))
        # obtener resultado
        registro = cursor.fetchall()
        for columna in registro:
            print("id= ", columna[0])
            print("nombre= ", columna[1] , "\n")


    except mysql.connector.Error as e:
        print("Error al obtener el registro de la tabla MySQL")

    finally:
            if conexion.is_connected():
                conexion.close()
                cursor.close()
                print("La conexion MySQL se ha cerrado")
#fin sql

#lista de rostros
def encontrarEncodigns(imagenes):
    encodeLista = []
    for img in imagenes:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0] 
        encodeLista.append(encode)
    return encodeLista
#fin lista de rostro


#separar extension
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    imagenes.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
encodeListaConocido = encontrarEncodigns(imagenes)
print('Encoding completado...')
#fin separar extension

