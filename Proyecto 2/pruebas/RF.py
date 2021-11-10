import cv2
import numpy as np
import face_recognition

imgHouse = face_recognition.load_image_file('Referencias imagenes/house.jpg')
imgHouse = cv2.cvtColor(imgHouse, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Referencias imagenes/house.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

rostroLoc = face_recognition.face_locations(imgHouse)[0]
encodeHouse = face_recognition.face_encodings(imgHouse)[0]
cv2.rectangle(imgHouse, (rostroLoc[3],rostroLoc[0]), (rostroLoc[1],rostroLoc[2]), (255, 0, 255), 2)

rostroLocEj = face_recognition.face_locations(imgTest)

rsotroLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (rsotroLocTest[3],rsotroLocTest[0]), (rsotroLocTest[1],rsotroLocTest[2]), (255, 0, 255), 2)

resultados = face_recognition.compare_faces([encodeHouse], encodeTest)
distanciaRostro = face_recognition.face_distance([encodeHouse], encodeTest)
print(resultados, distanciaRostro)
print(rostroLoc,rostroLocEj)
cv2.putText(imgTest,f'{resultados} {round(distanciaRostro[0],2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)

cv2.imshow('House' , imgHouse)
cv2.imshow('House Test' , imgTest)
cv2.waitKey(0)


