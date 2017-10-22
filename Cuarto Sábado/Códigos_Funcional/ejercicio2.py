#-*-coding:utf-8-*-
#Parámetros por omisión
"""
def saludar(nombre,mensaje='Hola amigo '):
	print(mensaje,nombre)

saludar(nombre=input('¿Cómo te llamas?'))
"""

#Parámetros arbitrarios 
#Los parámetros arbitrarios se guardan en una tupla
"""def recorre_parametros_arbitrarios(parametro_fijo,*arbitrarios):
	print(parametro_fijo)
	for argumeto in arbitrarios:
		print(argumeto)
	return arbitrarios
tipo=recorre_parametros_arbitrarios('Soy fijo',
	'Arbitrario1','Arbitrario2','Arbitrario3',
	'Arbitrario4','Arbitrario5')
print(type(tipo))
"""
"""
#keywords kwargs
def recorre_parametros_arbitrarios(parametro_fijo,*arbitrarios,**kwargs):
	#Arbitrarios
	for argumeto in arbitrarios:
		print(argumeto)
	#kwargs
	for clave in kwargs:
		print("El valor de ",clave,"es",kwargs[clave])

recorre_parametros_arbitrarios('Soy fijo',
	'Arb1','Arb2','Arb3',clave1='valor1',clave2='valor2',
	clave3='valor3')
"""

#Desempaquetar 
"""
def calcular(importe,descuento):
	return importe -(importe*descuento/100)

datos=[1500,10]
#Toma cada elemento de la lista y por posición se lo pasa
#a la función
print(calcular(*datos))
"""

def calcular(importe,descuento):
	return importe -(importe*descuento/100)

datos={"descuento":10,"importe":1500}

print(calcular(**datos))