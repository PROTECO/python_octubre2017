#-*-coding:utf-8-*-
############################################
##########SERIES############################
############################################
#Las Series se pueden crear tanto a partir de listas como de diccionarios. 
#De manera opcional podemos especificar una lista con las etiquetas de las filas.
from pandas import Series 

#Forma de crear una serie
serie=Series(['a','b','c'])

print(serie)
#print(type(serie))
#Podemos definir los indices de una serie pasandolos como parametros 
#a la función Series()
serie=Series(['a','b','c'],index=['pregunta 1','pregunta 2','pregunta 3'])

print(serie)

#También podemos pasar un diccionario a la función Series()
#Tomará las keys como índices

dicc={'pregunta 1':'a','pregunta 2':'b','pregunta 3':'c'}

serie=Series(dicc)

print(serie)

#Podemos controlar los datos que queremos incluir, como su orden especificado
#en el index

serie=Series(dicc,index=['pregunta 3','pregunta 2','pregunta 1'])

print(serie)