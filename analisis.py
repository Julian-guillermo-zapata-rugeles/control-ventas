import pandas as pd
import matplotlib.pyplot as plt

def update():
    data=pd.read_csv("ventas.csv",sep=";",names=['fechas','id','producto','precioReal','vendidos','iva','totalVentas'])
    data= data[data['producto'].notna()]
    data.plot(x="producto", y=["vendidos"],rot=80,kind="bar",color="blue",title="PRODUCTO CON MAS VENTAS X UNIDAD")
    plt.savefig('static/mayorventa.png',bbox_inches='tight')
    data.plot(x="fechas", y=["totalVentas"],rot=80,color="red",title="COMPORTAMIENTO DE VENTA EN FUNCION DEL TIEMPO")
    plt.savefig('static/vendidos.png',bbox_inches='tight')
def contador():

    data=pd.read_csv("ventas.csv",sep=";",names=['fechas','id','producto','precioReal','vendidos','iva','totalVentas'])
    data= data[data['producto'].notna()]
    totalventa=data['totalVentas'].sum()
    cantidad=data['vendidos'].sum()
    return (totalventa,cantidad)
