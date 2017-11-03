import pandas as pd 
import matplotlib.pyplot as plt 

data=pd.read_csv('datosTelescopio.csv')
"""
Si no cargan las cabeceras, se debe hacer
manualmente

headers=['Distancia','Velocidad de recesión']
data_no_headers= pd.read_csv('datosTelescopio.csv',names=headers)
print(data_no_headers.head())
"""
#Se muestran los primeros cinco datos de 
#nuestro archivo CSV (Comma Separated Values)

print(data.head())

data.set_index('Distancia',inplace=True)

print(data.head())

data.plot()

plt.show()