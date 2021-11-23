from tkinter import *

def finprograma():
    print("El programa ha finalizado")
    exit()
ventana=Tk()
canvas = Canvas(ventana, width = 700, height = 400)
canvas.pack()      
img = PhotoImage(file="ciber2.ppm")
canvas.create_image(0,0, anchor=NW, image=img)
ventana.geometry("600x400")
ventana.title("Reconocimiento Facial")
botonEscanear=Button(ventana,text="Comenzar Escaneo")
botonEscanear.place(x=200,y=175)
botonSalir=Button(ventana,text="Salir",command=finprograma)
botonSalir.place(x=350,y=175)
ventana.mainloop()
