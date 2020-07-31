import sqlite3
conexion=sqlite3.connect("base.sqlite3")
cursor=conexion.cursor()
cursor.execute("INSERT INTO PRODUCTOS VALUES(10,'COMIDA PARA PERROS EN LATAX500',3600)")
conexion.commit()
conexion.close()
