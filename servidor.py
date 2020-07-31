from flask import Flask , redirect , url_for
from flask import render_template
from flask import request
from datetime import datetime
import analisis
import os
import time
import principal
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def welcome():
    #serverTime=os.popen("date").read()
    return render_template('home.html')

@app.route('/full')
def limpiar():
    removit=open("cache","w")
    removit.close()
    return redirect(url_for('vender'))

@app.route("/analisis")

def analizar():
    analisis.update()
    return render_template("analisis.html")

@app.route('/inventario')
def inventario():
    encabezado=["ID","Cantidad Disponible","Descripción del producto","Precio de venta"]
    items=principal.MotorSQL().MostrarDatos()
    return render_template('inventario.html',columns=encabezado,items=items)
@app.route('/reporte')
def reportar():
    x=open("ventas.csv").read().split("\n")
    identy=["Fecha","Id","Descripción","Precio Base","Unidades","Iva","TOTAL"]
    bol=[]
    for j in x:
        k=j.split(";")
        bol.append(k)
    info=analisis.contador()
    return render_template("reporte.html",encabezado=identy,cache=bol,info=info)
@app.route('/vender')
def vender():
    encabezado=["ID","PRODUCTO","VALOR","CANTIDAD","IVA","TOTAL"]
    cache=open("cache").read().split("\n")
    empty=[]
    total=0
    for i in cache:
        try:
            sub=i.split(";")
            if len(sub)>2:
                empty.append(sub)
                total=total+int(sub[5])
        except Exception as e:
            pass
    items=principal.MotorSQL().MostrarDatos()
    return render_template('vender.html',productos=items,encabezado=encabezado,cache=empty,total=total)

@app.route("/public", methods=["GET","POST"])
def public():
    try:
        id_producto=request.form["producto"]
        id_cantidad=request.form["cantidad"]
        id_producto=id_producto.replace("(","");id_producto=id_producto.replace(")","")
        print(id_producto)
        id_producto=id_producto.split("---")
        obtenido=principal.MotorSQL().ObtenerProducto(id_producto[0])
        obtenido=obtenido[0] ; total=int(id_cantidad)*obtenido[3];iva=(int(id_cantidad)*obtenido[3])*0.19
        cadena="{};{};{};{};{};{}\n".format(obtenido[0],obtenido[2],obtenido[3],id_cantidad,iva,total)
        cache=open("cache","a") ; cache.write(cadena) ;cache.close()
        return redirect(url_for('vender'))
    except Exception as e:
        return "error"
@app.route("/make")
def make():
    cache=open("cache").read().split("\n")
    venta=open("ventas.csv","a")
    getTime=time.asctime()
    for element in cache:
        if element!="":
            confirmada=""
            confirmada=getTime+";"+element+"\n"
            venta.write(confirmada)
            producto=element.split(";")
            sub=producto[0]
            cantidad=producto[3]
            print(sub,cantidad)
            readyChange=principal.MotorSQL().Make(sub,cantidad)
            print("la operación quedó así --- > ",readyChange)
            principal.MotorSQL().ActualizarElemento(readyChange[0],readyChange[1])
    remove=open("cache","w")
    remove.close()
    venta.close()
    return render_template('home.html',msg="Transacción realizada correctamente!")
if __name__ == '__main__':
    TEMPLATES_AUTO_RELOAD = True
    app.run(host='0.0.0.0', debug=True ,port=12966)
