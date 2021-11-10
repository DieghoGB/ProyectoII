import cv2
import numpy as np
from tkinter import *
from PIL import Image
from PIL import ImageTk


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
            frame = cv2.resize(frame, (600,600), None, 0.25, 0.25)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, visualizar)

        else:
            lblVideo.image = ""
            cap.release()
            
def escanear():
    print("pro")  
    
cap = None
root = Tk()
btnEscanear = Button(root, text="Escanear", command=escanear)
btnEscanear.grid(column=1, row=0)
lblVideo = Label(root)
lblVideo.grid(column=0, row=1, columnspan=2)
iniciar()
root.mainloop()