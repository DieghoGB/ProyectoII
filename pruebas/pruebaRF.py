import face_recognition

# cargar las imagenes a un numpy(no se que significara) array
sandy_imagen = face_recognition.load_image_file("a.jpg")
jesus_imagen = face_recognition.load_image_file("judas.jpg")
desconocido_imagen = face_recognition.load_image_file("judas.jpg")


# Obtenemos los rostros codificados por cada rostro en cada archivo de imagen
try:
    sandy_rostro_codificado = face_recognition.face_encodings(sandy_imagen)[0]
    obama_rostro_codificado = face_recognition.face_encodings(jesus_imagen)[0]
    rostro_desconocido_codificado = face_recognition.face_encodings(desconocido_imagen)[0]
except IndexError:
    print("No pude localizar ningun rostro en al menos una de las imagenes. Terminando...")
    quit()
    
rostros_conocidos = [
        sandy_rostro_codificado, 
        obama_rostro_codificado
]

resultado = face_recognition.compare_faces(rostros_conocidos, rostro_desconocido_codificado)

# En caso de que la IA reconozca el rostro comparado nos retornara un true de lo contrario un false
print("Es el rostro desconocido muy feo? {}".format(resultado[0]))
print("Es el rostro desconocido del doctor house? {}".format(resultado[1]))
print("Es el rostro desconocido una nueva persona que nunca hemos visto antes? {}".format(not True in resultado))