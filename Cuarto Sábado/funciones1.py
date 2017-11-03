#-*-coding:utf-8-*-
"""
def soy_una_funcion():
	Aquí adentro va el código que deseamos
	que realice la función.
	Para llamar a una función, solamente basta
	poner su nombre
soy_una_funcion()
"""
#Las cadenas que se encuentran despues de la declaración de una función nos ayudan
#a documentar nuestro código y hacerlo más legible para otros programadores
def hola():
	"""
	Esta función saluda a los amigos del curso de python
	"""
	print("Hola amigos del curso de python, soy una función")
hola()
#Podemos acceder a la cadena de documentación de la siguiente forma:
print(hola.__doc__)



























