#import modules



from MainRF import *
    

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='n1k_lh345',
    database='buscados'
    )
cursor = conexion.cursor()



def iniciarSesion():


    ventanaIniciarSesion = tkinter.Tk()
    ventanaIniciarSesion.geometry("200x100")
    
    labelUsuario = tkinter.Label(ventanaIniciarSesion,text="Usuario:").grid(row=2,column=2)
    textoUsuario = tkinter.Entry(ventanaIniciarSesion, width=10, bg='white')
    textoUsuario.grid(row=2,column=3)
    #texto1 = tkinter.Text(ventana, height=1, width=10, bg='white')
    labelPassword = tkinter.Label(ventanaIniciarSesion, text="contrasenha:").grid(row=3,column=2)
    textoPassword = tkinter.Entry(ventanaIniciarSesion, width=10,show="*" , bg='white')
    textoPassword.grid(row=3,column=3)
    
    botonLogearse = tkinter.Button(ventanaIniciarSesion,text="Iniciar Sesion",command=lambda:verificarCuenta()).grid(row=4,column=3)
    botonLogearse = tkinter.Button(ventanaIniciarSesion,text="salir",command=ventanaIniciarSesion.destroy).grid(row=4,column=4)
    def verificarCuenta():
        usuario=textoUsuario.get()
        password=textoPassword.get()
        if(usuario == "" or password == ""):
            showinfo("Error","Campos en blanco!!!")
        else:
            consultaBD = "select * from PDI where usuario = %s"
            # asignar variable en la consulta
            cursor.execute(consultaBD, (usuario,))
            bandera=True
            registro = cursor.fetchall()
            for columna in registro:
                if columna[0] == usuario:
                    bandera=False
            if bandera == True: 
                
                showinfo("","No existe alguien registrado con ese usuario en la BD")
                
                ventanaIniciarSesion.quit
            else:
                verificar=columna[1] # verificar contrasenha sea correcta
                if verificar == password:
                    showinfo("Exito","Logeando")
                    iniciarPrograma(usuario)
                    ventanaIniciarSesion.quit
                else:
                    showinfo("Error","Contrasenha incorrecta!!!")
                    
        
    
def registrarse():

    ventanaRegistrarse = tkinter.Tk()
    ventanaRegistrarse.geometry("200x100")
    
    labelUsuario = tkinter.Label(ventanaRegistrarse,text="Usuario(largo 10):").grid(row=2,column=2)
    textoUsuario = tkinter.Entry(ventanaRegistrarse, width=10, bg='white')
    textoUsuario.grid(row=2,column=3)
    #texto1 = tkinter.Text(ventana, height=1, width=10, bg='white')
    labelPassword = tkinter.Label(ventanaRegistrarse, text="contrasenha(largo 10):").grid(row=3,column=2)
    textoPassword = tkinter.Entry(ventanaRegistrarse, width=10,show="*" , bg='white')
    textoPassword.grid(row=3,column=3)
    
    botonLogearse = tkinter.Button(ventanaRegistrarse,text="registrarse",command=lambda:registrarCuenta()).grid(row=4,column=3)
    botonLogearse = tkinter.Button(ventanaRegistrarse,text="salir",command=ventanaRegistrarse.destroy).grid(row=4,column=4)
    
    def registrarCuenta():
        usuario=textoUsuario.get()
        password=textoPassword.get()
        if(usuario == "" or password == ""):
            showinfo("Error","Campos en blanco!!!")
        else:
            consultaBD = "select * from PDI where usuario = %s"
            # asignar variable en la consulta
            cursor.execute(consultaBD, (usuario,))
            # obtener resultado
            bandera=True
            registro = cursor.fetchall()
            for columna in registro:
                if columna[0] == usuario:
                    bandera=False
            if bandera == True: 
                query ="INSERT INTO PDI VALUES (%s, %s)"
                datos= (usuario,password)
                cursor.execute(query,datos) #insertar datos a la BD  
                #se suben los datos a la BD
                showinfo("","Cuenta registrada con exito!!")
                conexion.commit()
                ventanaRegistrarse.quit
            else:
                showinfo("Error","Existe alguien registrado con ese usuario!!!")   
                ventanaRegistrarse.quit
  
    
def ventanaInicio():
    ventanaInicio = tkinter.Tk()
    ventanaInicio.geometry("600x400")
    ventanaInicio.title("Iniciar Sesion")
    tituloLabel = tkinter.Label(ventanaInicio, text="Bienvenido").pack()
    botonIniciarSesion = tkinter.Button(ventanaInicio, text="Iniciar Sesion", command=iniciarSesion).pack(before=tituloLabel)
    botonRegistrarse = tkinter.Button(ventanaInicio,text="Registrarse", command=registrarse).pack(before=botonIniciarSesion)
    botonCerrar = tkinter.Button(ventanaInicio,text="Salir",command=ventanaInicio.quit).pack(before=botonRegistrarse)
    
    ventanaInicio.mainloop()
    #botonEscanear=Button(root,text="Comenzar Escaneo",command=IniciarCamara)
    


ventanaInicio()    