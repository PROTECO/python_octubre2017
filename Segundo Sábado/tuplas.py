#!/usr/bin/python3
##########################
# Tipos de datos basicos
#
# Tuplas y conjuntos
##########################

#Secuencia inmutable de objetos que puede ser desempaquetada
#diferentes formas de crear tuplas
tup=() #tupla vacia
tup1 = ('hola', 'mundo', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

a = 1,2,5,7,8 #enpaqueta todos los numeros en una tupla
print a[3] #puede ser indexada
#a[0] = 3 #es inmutable (descomentar esta linea provoca un error)
u,v,w,x,y = a #desempaqueta
#u,v,w = a  #debe coincidir el numero de variables y de elementos en la tupla
            #(descomentar la linea anterior marca error)
print u,v,w,x,y
b = (4,) #tupla de un solo elemento
c = (1,3),"Hola" #puede haber tuplas dentro de tuplas
x,y = c 
u,v = x

#Casteo de una lista a una tupla
lista=[1,2,3,4,4]
tuplaL=tuple(lista)
print(tuplaL)
#Conjunto, tal cual como se usa en matemáticas
#quita las repeticiones de la lista
conjunto=set(lista)
print(conjunto)