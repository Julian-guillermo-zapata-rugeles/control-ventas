__Author__="Julian Guillermo Zapata Rugeles"
"""
MotorSQL().escribir( * , * , * ) # llamar a la base de datos para escribir
MotorSQL().MostrarDatos() # retornar/imprimir la base de datos
MotorSQL().ActualizarElemento(* , *) arg1= nueva cantidad , arg2= nombre del producto
"""
#----------- constantes ------------
DATABASE_FILE="base.sqlite3" # DDBB
#-----------------------------------

import sqlite3



class MotorSQL():
    ''' Agilizar la escritura / lectura de la base de datos sqlite3 '''
    def __init__(self):
        ''' Constructor base '''
        self.conexion=sqlite3.connect(DATABASE_FILE)
        self.cursor=self.conexion.cursor()

    def escribir(self,unidades,nombre,precio):
        ''' Escribir valores nuevos a la base de datos '''
        try:
            self.cursor.execute("INSERT INTO PRODUCTOS VALUES({},'{}',{})".format(unidades,nombre,precio))
            self.conexion.commit()
            print("Cambios realizados")
            self.conexion.close()
            print("conexion cerrada.")
            return True
        except Exception as e:
            print("alerta -> conexion  abortada (vacio ó repetida)")
            return False

    def MostrarDatos(self,mostrar=0):
        ''' Leer los datos de la base de datos -- retornarla '''
        self.cursor.execute("SELECT * FROM PRODUCTOS")
        loadData=self.cursor.fetchall()
        self.conexion.close()
        if mostrar==1:
            for data in loadData:
                print(data)
        else:
            return loadData
    def ActualizarElemento(self,nuevaCantidad,producto):
        print("se actualizará a ",nuevaCantidad," -> ",producto)
        self.cursor.execute("UPDATE PRODUCTOS set CANTIDAD={} WHERE ID='{}'".format(nuevaCantidad,producto))
        self.conexion.commit()
        self.conexion.close()
        print("cambios realizados a la bbdd")

    def Make(self,producto,cantidad):
        self.cursor.execute("SELECT * FROM PRODUCTOS WHERE ID='{}'".format(producto))
        elementReady=self.cursor.fetchall()
        actual=int(elementReady[0][1])
        nuevo=actual-int(cantidad)
        return [nuevo,elementReady[0][0]]

    def ObtenerProducto(self,nombreProducto):
        self.cursor.execute("SELECT * FROM PRODUCTOS WHERE ID='{}'".format(nombreProducto))
        elementReady=self.cursor.fetchall()
        self.conexion.close()
        print("ok-----!")
        return elementReady
#MotorSQL().escribir(8,"mani dulce con maiz x 100 ",3200)
#MotorSQL().MostrarDatos(1)
#MotorSQL().ActualizarElemento(4,"COMIDA PARA GATOS EN LATAX500")
