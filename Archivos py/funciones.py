import cv2.cv2
import mysql.connector
from variables_imports import *
from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils

    
#sql
''''
________________________________________
|                                      |
|Poner en comentario las partes del sql|
|______________________________________|
'''''
def datosBuscados(id,):
    try:        
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

def ingresarPersona():
    ventana= Tk() 
    ventana.geometry("800x600") 
    ventana.title(" Registrar persona ")
    #registrar rut
    label1 = tkinter.Label(ventana, text="rut(sin guion):")
    label1.grid(row=3,column=1)
    #escribir apellido
    texto1 = tkinter.Text(ventana, height=1, width=10, bg='white')
    texto1.grid(row=3,column=2)
    #registrar nombre
    label2 = tkinter.Label(ventana, text="nombre y apellido:")
    label2.grid(row=4,column=1)
    #escribir nombre
    texto2 = tkinter.Text(ventana, height=1, width=10, bg='white')
    texto2.grid(row=4,column=2)
    
    #verificacion de datos
    my_str = tkinter.StringVar()
    l5 = tkinter.Label(ventana,  textvariable=my_str, width=10 )  
    l5.grid(row=3,column=3) 
    my_str.set("Output")    
    #boton aceptar
    aceptarBoton= Button(ventana, text="Subir", command=lambda:subirPersona())
    aceptarBoton.grid(row=5,column=2)
    
    def subirPersona():
        flag_validation = True #para verificar datos
        rut=texto1.get("1.0",END) # lee el rut
        nombre=texto2.get("1.0",END) # lee el nombre
        
        #verifica el tamanho del nombre y el rut
        if (len(rut)<2 or len(nombre)<2):
            flag_validation= False
        try:
            val = int(rut) # verifica que se ingresen numeros
        except:
            flag_validation=False
            
        if(flag_validation):
            
            #parte de sql
            query ="INSERT INTO datosbuscados (rut, nombre) VALUES (%s, %s)"
            datos= (rut,nombre)
            
            id=cursor.execute(query,datos) #insertar datos a la BD  
            #se suben los datos a la BD
            sacarFoto(rut)       
            print("se ingreso el nombre: " , nombre)
            print("se ingreso el rut: ", rut)
            
            
        else:
            l5.config(fg='green')   # foreground color
            l5.config(bg='yellow') # background color
            my_str.set('Revise los datos')
        #insert into datosbuscados values('1111111','Hector Ossandon');


#fin sql

def sacarFoto(rut):
    cap = cv2.VideoCapture(0)
    flag = cap.isOpened()
    while(flag):
        success, img = cap.read()
        imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        cv2.imshow("Capture_Paizhao",img)
        k = cv2.waitKey(1) & 0xFF
        
        if k == ord ('s'): #Presione la tecla s para ingresar a la siguiente operación de guardado de imágenes
            
            cv2.imwrite("imagen"  + ".jpg", imgS)
            print("-------------------------")
            #conexion.comit()
        elif k == ord ('q'): #Presione la tecla q, el programa sale
            break
    cap.release()
    cv2.destroyAllWindows()
    




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