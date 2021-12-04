import cv2.cv2
import mysql.connector


from variables_imports import *


conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='n1k_lh345',
        database='buscados'
            )
cursor = conexion.cursor()
    
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
        consultaBD = "select * from datosbuscados where rut = %s"
        # asignar variable en la consulta
        cursor.execute(consultaBD, (id,))
        registro = cursor.fetchall()
        for columna in registro:
            print("Rut: ",columna[0])
            print("Nombre: ",columna[1])
            print("Apellido: ",columna[2])
            print("Antecendentes Penales: ",columna[3])
            print("Buscado: ",columna[4])
        

        
        # obtener resultado
        #registro = cursor.fetchall()
        #for columna in registro:
        #   print("Rut= ", columna[0])
        
        



    except mysql.connector.Error as e:
        print("Error al obtener el registro de la tabla MySQL")
    finally:
            if conexion.is_connected():
                conexion.close()
                cursor.close()
                print("La conexion MySQL se ha cerrado")
             
#fin sql
def ingresarPersona():
    ventana= Tk()
    ventana.geometry("350x140")
    ventana.title(" Registrar persona ")
    #registrar rut
    label1 = tkinter.Label(ventana, text="Rut (sin guion):")
    label1.grid(row=7,column=4)
    #escribir rut
    texto1 = tkinter.Text(ventana, height=1, width=10, bg='white')
    texto1.grid(row=7,column=5)
    #registrar nombre
    label2 = tkinter.Label(ventana, text="Nombre:")
    label2.grid(row=8,column=4)
    #escribir nombre
    texto2 = tkinter.Text(ventana, height=1, width=10, bg='white')
    texto2.grid(row=8,column=5)
    label3 = tkinter.Label(ventana, text="Apellido:")
    label3.grid(row=9,column=4)
    #escribir nombre
    texto3 = tkinter.Text(ventana, height=1, width=10, bg='white')
    texto3.grid(row=9,column=5)
    
    #verificacion de datos
    my_str = tkinter.StringVar()
    l5 = tkinter.Label(ventana,  textvariable=my_str, width=10 )  
    l5.grid(row=3,column=3) 
    my_str.set("Output")    
    #boton aceptar
    aceptarBoton= Button(ventana, text="Subir", command=lambda:subirPersona())
    aceptarBoton.grid(row=10,column=5)
    
    def subirPersona():
        flag_validation = True #para verificar datos
        rut=texto1.get("1.0",END) # lee el rut
        nombre=texto2.get("1.0",END) # lee el nombre
        apellido=texto3.get("1.0",END)#lee apellido
        #verifica el tamanho del nombre y el rut
        if (len(rut)<2 or len(nombre)<2 or len(apellido)<2):
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
                    #parte de sql
                    query ="INSERT INTO datosbuscados VALUES (%s, %s,%s,'Ninguno','No')"
                    datos= (rut,nombre,apellido)
                    cursor.execute(query,datos) #insertar datos a la BD  
                    #se suben los datos a la BD
                    conexion.commit()
                    sacarFoto(rut)
                
            else:
                
                showinfo("Error","Existe una persona registrada con ese rut en la BD!!!")

            
            
        else:
            showinfo("Error","Campos en blanco!!!")
        #insert into datosbuscados values('1111111','Hector Ossandon');


#fin sql

def sacarFoto(rut):
    cap = cv2.VideoCapture(0)
    flag = cap.isOpened()
    while(flag):
        success, img = cap.read()
        
        imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        cv2.imshow("Presione S para guardar la imagen, q para cerrar el programa",img)
        k = cv2.waitKey(1) & 0xFF
        
        if k == ord ('s'): #Presione la tecla s para ingresar a la siguiente operación de guardado de imágenes
            a=int(rut)
            cv2.imwrite(path + '/' + str(a) + '.png' ,img)
            print("Imagen guardada")
            cv2.imshow(path + '/' + str(a) + '.png' ,img)
            if not (path + '/' + str(a) + '.png' ,img):
                 print('Imagen no se pudo guardar')
            print("-------------------------")
            
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

