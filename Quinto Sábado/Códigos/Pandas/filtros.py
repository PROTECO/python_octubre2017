#-*-coding:utf-8-*-
############################################
########EXTRAER DATOS#######################
############################################
#Para filtrar datos, le podemos pasar a la Serie o al DataFrame 
#una lista de valores lógicos (verdaderos y falsos) indicando 
#las filas que nos son de interés.
from pandas import Series,DataFrame
serie = Series([1,2,3,4], index=['a','b','c','d'])
print(serie[[True, False, True, False]])

dataframe = DataFrame({'Uno' : Series([1, 2, 3], index=['a', 'b', 'c']),
 'Dos' : Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])})
#En lugar de pasar una lista de valores lógicos 
#podemos pasar directamente una prueba lógica.

print('Valores de la serie donde el índice sea mayor a 3',serie[serie>=3])

print('Valores del dataframe cuya columna sea "Dos" y el índice mayor a 1: \n',dataframe[dataframe['Dos']>1])

print('Valores del dataframe en dónde el índice tengra la etiqueta c: \n',dataframe[dataframe.index=='c'])
