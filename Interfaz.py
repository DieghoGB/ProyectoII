from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils

cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        cv2.rectangle(img, (150, 50), (500, 400), (0, 0, 0), thickness=3)
        cv2.putText(img, 'Posicione su Rostro', (150,40), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 3)
        cv2.imshow('Reconocimiento Facial', img)
        
        if cv2.waitKey(20) & 0xFF==ord('a'): 
            cv2.imwrite("\Referencias imagenes" + str(rut) + ".jpg", img)
            print(cap.get(3))
            print(cap.get(4))
            print("save" + str(rut) + ".jpg successfuly!")
            print("-------------------------")