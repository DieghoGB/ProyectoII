import mysql.connector
import face_recognition
import cv2
import os 
import numpy as np


path = 'Referencias imagenes'
imagenes = []
classNames = []
myList = os.listdir(path)
print(myList)

'''
rostroLoc = face_recognition.face_locations(imgHouse)[0]
encodeHouse = face_recognition.face_encodings(imgHouse)[0]
cv2.rectangle(imgHouse, (rostroLoc[3],rostroLoc[0]), (rostroLoc[1],rostroLoc[2]), (255, 0, 255), 2)

rsotroLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (rsotroLocTest[3],rsotroLocTest[0]), (rsotroLocTest[1],rsotroLocTest[2]), (255, 0, 255), 2)

resultados = face_recognition.compare_faces([encodeHouse], encodeTest)
distanciaRostro = face_recognition.face_distance([encodeHouse], encodeTest)
'''