
import mysql.connector



try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='n1k_lh345',
        database='buscados'
            )
    cursor = conexion.cursor()
    sql_select_Query = "select * from datosbuscados"
    cursor.execute(sql_select_Query)
    registro = cursor.fetchall()
    print("Total de las columnas en la tabla: ",cursor.rowcount )

    print("Imprimiendo cada columna...")
    for columna in registro:
        print("Nombre= ", columna[0])
        print("Rut= ", columna[1] , "\n")

except mysql.connector.Error as e:
    print("Error leyendo la data de la tabla MySQL")
    
finally:
        if conexion.is_connected():
            conexion.close()
            cursor.close()
            print("La coneccion MySQL se ha cerrado")