#-*-coding:utf-8-*-
############################################
########EXTRAER DATOS#######################
############################################
from pandas import Series,DataFrame

#Para seleccionar datos utilizaremos los métodos
#loc: Permite seleccionar datos usando etiquetas de filas y columnas
#iloc: Se basa en la posición(índice)
#ix: Se basa en etiquetas así como la posición 

#Sintaxis para los metodos en Series
"""
Series loc[etiqueta_fila]
Series iloc[indice_fila]
Series ix[indice/etiqueta_fila]
"""

serie=Series([1,2,3,4],index=['a','b','c','d'])
print("\t\tPara Series ********************************************\n")

print('Accedemos al elemento con la etiqueta "a": ',serie.loc['a'])
print('Accedemos al elemento con el índice 2 en lista : ',serie.iloc[2])
print('Selecciona el elemento con el índice 2 en lista: ',serie.ix[2])
print('Selecciona el elemento con la etiqueta "b": ',serie.ix['b'])

#Sintaxis para los metodos en DataFrames
"""
DataFrame loc[etiqueta_fila, etiqueta_columna]
DataFrame iloc[indice_fila, indice_columna]
DataFrame iloc[indice/etiqueta_fila, indice/etiqueta_columna]
"""
print('\t\tPara dataframes *****************************************\n')
dataframe=DataFrame({'Uno' : Series([1,2,3], index=['a','b','c']),
 					 'Dos' : Series([1,7,8,4],index=['a','b','c','d'])})

print('Accedemos la elemento con la etiqueta "a" en ambas columnas: \n',dataframe.loc['a'])
print('Accedemos la elemento con la etiqueta "a" de la fila dos: ',dataframe.loc['a','Dos']) 
print('Accedemos al elemento con el índice 1 en las listas: \n', dataframe.iloc[1])
print('Accedemos al elemento con el índice 2 en la lista Uno: ',dataframe.iloc[2,1]) 
print('Accedemos al elemento con el índice 1 en las listas: \n',dataframe.ix[1])
print('Accedemos al elemento con la etiqueta b y el índice 1 de la primera lista: ',dataframe.ix['d',0])




