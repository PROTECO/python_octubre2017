
##########################
# Tipos de datos basicos
#
# Listas
##########################

#Son estructuras de datos dinamicas de alto nivel que representan una
#coleccion ordenada de objetos


enteros=[12,13,4,5,2.5] #lista de enteros
print(enteros)
copiaenteros=enteros[:] #haciendo un slicing regresa una lista nueva
print(enteros[1:]) #lista con slicing desde el elemento 1 al final
print(enteros) #no se afecta la lista original

vocales=["E","O","I"]
vocales=["A"]+vocales
print(vocales)
vocales=vocales+["U"]}#solo se le pueden aumentar otras listas []
print(vocales)
#metodos internos de la clase list, nos permite ordenar alfabeticamente
vocales.sort()
print(vocales)

enteros.reverse() #se modifica solo el original
print(enteros)

print(copiaenteros)


a = [1,2,4,6,3,2,5] #lista de enteros
a[0] = 8 #son mutables
b = [2,5,"hola",7,"Mundo"] #pueden tener tipos de datos mezclados
c = [[1,2,5],["hola",3],[0x67, 'c']] #pueden tener cualquier tipo adentro, incluso otra lista
print (a[4]) #pueden ser indexadas
print (a[3:6]) #se puede aplicar slicing
print( b[-3]) #soporta indices negativos
print (c[2][1]) #para listas dentro de listas, usar doble indice

#Concatenacion
lista=["a","b"]+["A"]*3
print(lista)
print(lista.index("A"))
lista.insert(0,"A")
#Usando listas como pilas
tope=lista.pop(0)
print(tope)
print(lista)
#Metodos comunes

a.sort() #ordena la lista en orden ascendente
a.reverse() #ordena la lista en forma descendente
print(a.index(1))#nos regresa el indice de la pirmera ocurencia que encontro

print a #los dos metodos anteriores excepto index, modifican la lista original
a.append(3) #agrega el objeto al final de la lista
print a
b.insert(0,"hola") #inserta el elemento en el indice especificado
x = a.pop() #elimina el ultimo elemento
print x
a.pop(2) #puede recibir un indice para que en vez de que sea el ultimo sea uno en especifico
a.count(3) #cuenta cuantas veces aparece en la lista el elemento especificado
a.remove(2) #quita el objeto especificado de lista
            #importante recordar, no quita el objeto que este en el indice 2,
            #sino el primer 2 como tal que encuentre

#Funciones predefinidas
max(a) #devuelve el maximo elemento de una lista
len(a) #devuelve la longitud de la lista
del(a[3]) #elimina el elemento de la lista


