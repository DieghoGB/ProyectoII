from funciones import *
#Iniciar camara
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
            print(name)
            #sql parte
            datosBuscados(name) 
            #sql fin
            y1,x2,y2,x1 = rostroLoc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1 , (255,255,255), 2)    
    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
    
