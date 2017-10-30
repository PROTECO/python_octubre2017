#########################
#### ENCAPSULAMIENTO ####
#########################
"""
El encapsulamiento nos va a permitir esconder información
sensible de un objeto. En Python tendremos dos niveles de
encapsulamiento:
Público: Cualquier parte del programa puede acceder a los
atributos y métodos del objeto.
Privado: Los métodos y atributos sólo pueden ser utilizados
dentro del objeto que los define.
"""
class Computadora:
	def __init__(self, color, tam, cpu, ram, hdd):
		#Los siguientes dos atributos son públicos.
		self.color = color
		self.tam = tam
		#Los siguientes tres atributos son privados.
		self.__cpu = cpu
		self.__ram = ram
		self.__hdd = hdd

	#Este método hace uso de los atributos privados.
	def lanzarJuego (self):
		if self.__ram < 1024:
			print("No se puede lanzar el juego")
		elif self.__ram >= 1024 and self.__ram < 2048:
			print("Corriendo juego en calidad media.")
		else:
			print("Corriendo a máxima calidad.")
	
	#Este método hace uso de los atributos tanto públicos
	#como privados.
	def verCaracteristicas (self):
		print("Color:",self.color)
		print("Tamaño:", self.tam)
		print("Cantidad de RAM", self.__ram)

	#Dado que no se puede modificar un atributo privado desde
	#fuera de la clase que lo define, defino un método público 
	#que me permita modificarlo desde dentro de ésta.
	def cambiarRam (self, ram):
		contraseña = input("Para cambiar la RAM, ingresa la contraseña: ")
		if (contraseña == "123"):
			self.__ram = ram
			print("RAM cambiada a", ram)
		else:
			print("No tienes permiso.")

#Instancío tres objetos de la clase Computadora
computadoraVieja = Computadora("negro", 14, 3, 512, 1000)
computadora = Computadora("amarillo", 15, 6, 1500, 2000)
computadoraNueva = Computadora("gris", 17, 10, 4096, 5000)

print("Vemos las características de una computadora...")
computadoraVieja.verCaracteristicas()
#Podemos ver que aunque estoy haciendo referencia a un atributo
#de la clase Computadora, tratar de modificarlo de esta forma
#no hace ninguna diferencia:
computadoraVieja.__ram = 1536
print("Vemos las características de una computadora...")
computadoraVieja.verCaracteristicas()
#Para poder modificar la RAM, que es un atributo privado,
#utilizaré el método publico que definí que me permite hacerlo.
computadoraVieja.cambiarRam(1536)
computadoraVieja.verCaracteristicas()