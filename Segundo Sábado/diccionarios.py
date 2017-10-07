#!/usr/bin/python3
##########################
# Tipos de datos basicos
#
# Diccionarios
##########################

#Estructuras de datos que mapean un objeto (llave) con otro (valor)

diccionario={1:"alan",2:"roberto",3:"luis"}

print(diccionario) #imprime todo el diccionario
print(diccionario[1]) #imprime el valor de la llave 1



calificaciones = {"juan":10, "pepe":9, "pedro":7} #se escribe entre llaves {}
print calificaciones["pepe"] #el acceso no es por indice sino por la llave
#importante recordar, el acceso no es por indice, asi que no hay una garantia
#en cuanto al orden en que python guarda las entradas en el diccinario
#por esto tampoco se puede aplicar slicing


d = {"uno":1, "dos":2, "uno":3}
print d #no puede dos llaves iguales en el mismo diccionario
        #(si se intenta meter otra igual, simplemente sobreescribe a la anterior)

#el valor de las llaves tiene que ser un dato inmutable: Cadenas, numeros, tuplas
e = {"cadena": 2, ("tu","pla"): 3, 0x3679: ["l","i","s","t","a"]} #las llaves deben ser necesariamente
    #objetos inmutables, los valores pueden ser cualquier objeto, inmutable o no

#Metodos comunes
x = calificaciones.get("lilia") #obtiene el valor asociado con la llave, sino
    #existe no arroja un error, a diferencia de usando la notacion de corchetes
x = calificaciones.get("mario",0) #se le puede asignar opcionalmente un valor por defecto
    #(si no encuentra la llave, arroja ese valor)
print x
calificaciones.update({"maria":10}) #agregar nuevas entradas al diccionario
print calificaciones.keys() #nos da todas las llaves en una tupla
print calificaciones.values() #nos da todos los valores en una tupla
print(calificaciones.items()) #nos da todos los valores y llaves en tuplas

print(calificaciones.get("juan")) #buscar un elemento por su llave

diccionario2=diccionario.copy() #copiar un diccionario