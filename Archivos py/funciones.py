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
'''
             
'''
#Funcion para iniciar el video streaming
def iniciar():
    global cap
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    visualizar()
    
def visualizar():
    global cap
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.resize(frame, (900,900), None, 0.25, 0.25)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            imgfocus = cv2.cv2.imread('focus.png',0)
            lblVideo.configure(image=img)
            lblVideo.image = img
            cv2.imshow('image',imgfocus)
            lblVideo.after(10, visualizar)

            

            
        else:
            print("camara no conectada")
            lblVideo.image = ""
            cap.release()
            
def escanear():
    print('prueba')
''' 
    rostrosCurFrame = face_recognition.face_locations(frame)
    encodesCurFrame = face_recognition.face_encodings(frame, rostrosCurFrame)
    for encodeRostro,  rostroLoc in zip(encodesCurFrame, rostrosCurFrame):
        matches = face_recognition.compare_faces(encodeListaConocido, encodeRostro)
        rostroDis = face_recognition.face_distance(encodeListaConocido, encodeRostro)
        matchIndex = np.argmin(rostroDis)      
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1,x2,y2,x1 = rostroLoc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.rectangle(frame, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(frame, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1 , (255,255,255), 2) 
'''
    
