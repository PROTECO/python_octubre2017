#-*-coding:utf-8-*-
############################################
########EXTRAER DATOS#######################
############################################
from pandas import concat,Series,DataFrame

serie1=Series([1,2,3,4],index=['a','b','c','d'])
print(serie1)

serie2=Series([4,5,6,7],index=['a','b','c','d'])
print(serie2)

print(concat([serie1,serie2]))