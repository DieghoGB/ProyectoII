from typing_extensions import runtime
from cv2 import imshow
import cv2.cv2

from funciones import *
def IniciarCamara():
    root.iconify()
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        rostrosCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, rostrosCurFrame)
        for encodeRostro,  rostroLoc in zip(encodesCurFrame, rostrosCurFrame):
            matches = face_recognition.compare_faces(encodeListaConocido, encodeRostro)
            rostroDis = face_recognition.face_distance(encodeListaConocido, encodeRostro)
            matchIndex = np.argmin(rostroDis)
            if matches[matchIndex]:
                
                    name = classNames[matchIndex].upper()
                    type(name)
                    y1,x2,y2,x1 = rostroLoc
                    y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
                    cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
                    cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1 , (255,255,255), 2)
                    conexion = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    passwd='n1k_lh345',
                    database='buscados'
                    )
                    rut=int(name)
                    print(rut )
                    print(type(rut))
                    def cerrarVentana():
                            ventanaDatos.destroy()
                            IniciarCamara()  
                                          
                    ventanaDatos = tkinter.Toplevel(root)
                    ventanaDatos.geometry("1200x600")
                    cursor = conexion.cursor()
                    consultaBD = "select * from datosbuscados where rut = %s"
                    #asignar variable en la consulta
                    cursor.execute(consultaBD, (rut,))
                    registro = cursor.fetchall()
                    for columna in registro:
                        print(columna)
                    label1 = tkinter.Label(ventanaDatos, text="Rut:")
                    label1.place(x=1,y=1)
                    labelRut = tkinter.Label(ventanaDatos, text=columna[0])
                    labelRut.place(x=30,y=1) 
                    label2 = tkinter.Label(ventanaDatos, text="Nombre:")
                    label2.place(x=1,y=20) 
                    labelNombre = tkinter.Label(ventanaDatos, text=columna[1])
                    labelNombre.place(x=60,y=20)  
                    label3 = tkinter.Label(ventanaDatos, text="Apellido:")
                    label3.place(x=1,y=42)
                    labelApellido = tkinter.Label(ventanaDatos, text=columna[2])
                    labelApellido.place(x=60,y=42)
                        
                    label3 = tkinter.Label(ventanaDatos, text="Antecedentes Penales:")
                    label3.place(x=1,y=63) 
                    labelAntecedentes = tkinter.Label(ventanaDatos, text=columna[3])
                    labelAntecedentes.place(x=120,y=63)   
                       
                    label3 = tkinter.Label(ventanaDatos, text="Buscado:")
                    label3.place(x=1,y=84)
                    labelBuscado = tkinter.Label(ventanaDatos, text=columna[4])
                    labelBuscado.place(x=60,y=84)   
                    
                    foto = PhotoImage(file= path + '/' + columna[0].strip('\n') + '.png')
                    fotolabel = tkinter.Label(ventanaDatos,image=foto)
                    fotolabel.place(x=700,y=100) 
                    fotolabel.pack(side="right")

                    button = tkinter.Button(ventanaDatos,text = "Ok", 
                                        command = cerrarVentana)
                    button.place(x=50,y=110)
                    ventanaDatos.mainloop() 
                                        
                    cap.release()
                    cv2.destroyAllWindows()

    

                           
                #sql fin

            else:
                name="no registrado"
                y1,x2,y2,x1 = rostroLoc
                y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
                cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
                cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1 , (255,255,255), 2)
        cv2.imshow('Reconocimiento Facial', img)


        if cv2.waitKey(20) & 0xFF==ord('k'):
            break
    cap.release()
    cv2.destroyAllWindows()

    cv2.waitKey(1)
def finprograma():
    print("El programa ha finalizado")
    exit()
    
def iniciarPrograma(usuario):
    canvas = Canvas(root, width = 700, height = 400)
    canvas.pack()
    consultaBD = "select * from PDI where usuario = %s"
            # asignar variable en la consulta
    cursor.execute(consultaBD, (usuario,))
 
    registro = cursor.fetchall()
    for columna in registro:
        print(columna)
    usuario = "bienvenido " + str(columna[0])
    
    img2 = PhotoImage(file="ciber2.ppm")
    canvas.create_image(0,0, anchor=NW, image=img2)
    root.geometry("600x400")
    root.title(usuario)
      
    botonEscanear=Button(root,text="Comenzar Escaneo",command=IniciarCamara)
    botonEscanear.place(x=250,y=165)
    botonRegistrar=Button(root,text="Registrar Persona",command=ingresarPersona)
    botonRegistrar.place(x=254,y=195)
    botonSalir=Button(root,text="Salir",command=finprograma)
    botonSalir.place(x=290,y=225)
    root.mainloop()





