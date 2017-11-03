#-*-coding:utf-8-*-
############################################
##########DATAFRAMES########################
############################################
#Los DataFrame se pueden crear de diferentes maneras, una forma común de crearlos 
#es partir de listas o diccionarios de listas, de diccionarios o de Series. 
#En los DataFrame tenemos la opción de especificar tanto 
#el index (el nombre de las filas) como columns (el nombre de las columnas).

from pandas import DataFrame,Series

list_listas = [[1,2,3,4],
			   [4,3,2,1],
			   [9,8,7,6],
			   [6,7,8,9]]

dataframe = DataFrame(list_listas, columns=['Uno', 'Dos','Tres','Cuatro'])

print(dataframe)

dicc_listas={'Uno':[1,2,3,4],'Dos':[4,3,2,1],'Tres':[9,8,7,6],'Cuatro':[6,7,8,9]}

dataframe=DataFrame(dicc_listas)

print(dataframe)

#También en los dataframes podemos sobreescribir los índices
dataframe=DataFrame(dicc_listas,index=['a','b','c','d'])

print(dataframe)

#Ahora pasaremos Series a un dataframe
dicc_series={'Uno':Series([1,2,3],index=['a','b','c']),
			 'Dos':Series([1,2,3,4],index=['a','b','c','d'])}

dataframe=DataFrame(dicc_series)

print(dataframe)

#Al igual que con las Series, podemos controlar tanto los datos que 
#queremos incluir como su orden especificando el index y/o columnas 
#que nos interesen

dataframe=DataFrame(dicc_series,index=['a','b','d'])

print(dataframe)

dataframe=DataFrame(dicc_series,index=['a','b','d'],columns=['Dos','Tres'])