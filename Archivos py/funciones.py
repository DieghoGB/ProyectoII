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
    ventana.geometry("350x140")
    ventana.title(" Registrar persona ")
    #registrar rut
    label1 = tkinter.Label(ventana, text="Rut (sin guion):")
    label1.grid(row=7,column=4)
    #escribir apellido
    texto1 = tkinter.Text(ventana, height=1, width=10, bg='white')
    texto1.grid(row=7,column=5)
    #registrar nombre
    label2 = tkinter.Label(ventana, text="Nombre y Apellido:")
    label2.grid(row=8,column=4)
    #escribir nombre
    texto2 = tkinter.Text(ventana, height=1, width=10, bg='white')
    texto2.grid(row=8,column=5)
    
    #verificacion de datos
    my_str = tkinter.StringVar()
    l5 = tkinter.Label(ventana,  textvariable=my_str, width=10 )  
    l5.grid(row=3,column=3) 
    my_str.set("Output")    
    #boton aceptar
    aceptarBoton= Button(ventana, text="Subir", command=lambda:subirPersona())
    aceptarBoton.place(x=155,y=70)
    
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
            
            
            consultaBD = "select * from datosbuscados where rut = %s"
            # asignar variable en la consulta
            cursor.execute(consultaBD, (rut,))
            # obtener resultado
            bandera=True
            registro = cursor.fetchall()
            for columna in registro:
                if columna[0] == rut:
                    bandera=False
            if bandera==True: 
                print('no esta')
                #parte de sql
                query ="INSERT INTO datosbuscados (rut, nombre) VALUES (%s, %s)"
                datos= (rut,nombre)   
                id=cursor.execute(query,datos) #insertar datos a la BD  
                #se suben los datos a la BD
                sacarFoto(rut)       
                print("se ingreso el nombre: " , nombre)
                print("se ingreso el rut: ", rut)
            else:
                falloL = Label(ventana,text='Existe una persona registrada con ese rut en la BD')
                falloL.place(x=60,y=100)

            
            
        else:
            falloL = Label(ventana,text="Ingrese correctamente los datos!")
            falloL.place(x=90,y=100)
        #insert into datosbuscados values('1111111','Hector Ossandon');


#fin sql

def sacarFoto(rut):
    cap = cv2.VideoCapture(0)
    flag = cap.isOpened()
    while(flag):
        success, img = cap.read()
        
        
        cv2.imshow("Presione S para guardar la imagen, q para cerrar el programa",img)
        k = cv2.waitKey(1) & 0xFF
        
        if k == ord ('s'): #Presione la tecla s para ingresar a la siguiente operación de guardado de imágenes
            a=int(rut)
            cv2.imwrite(path + '/' + str(a) + '.jpg' ,img)
            print("Imagen guardada")
            cv2.imshow(path + '/' + str(a) + '.jpg' ,img)
            if not (path + '/' + str(a) + '.jpg' ,img):
                 print('Imagen no se pudo guardar')
            print("-------------------------")
            conexion.commit()
        elif k == ord ('q'): #Presione la tecla q, el programa sale
            
            break
    cap.release()
    cv2.destroyAllWindows()
    




#lista de rostros
def encontrarEncodigns(imagenes):
    encodeLista = []
    for img in imagenes:
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