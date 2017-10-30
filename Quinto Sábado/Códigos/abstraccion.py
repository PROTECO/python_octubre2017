#########################
###### ABSTRACCIÓN ######
#########################
"""
La abstracción se refiere a obtener los atributos (características) 
y los métodos (acciones) mediante los cuales interactuaremos 
con esos atributos, a partir un objeto de la realidad según lo que 
requerimos como programador.
Dependiendo del problema que queremos atacar en nuestro 
programa debemos definir qué tienen y qué hacen nuestros objetos.
"""
#Definimos una clase "Computadora" que servirá como molde
#para crear diferentes objetos de ella.
class Computadora:
	#Definimos un constructor. Aquí escribimos e inicializamos 
	#todos los atributos que tendrán nuestros objetos.
	def __init__(self, color, tam, cpu, ram, hdd):
		self.color = color
		self.tam = tam
		self.cpu = cpu
		self.ram = ram
		self.hdd = hdd

	#Definimos un método que interactúa con el atributo "ram".
	#Nótese que el atributo se manda llamar como "self.ram" 
	#y así debe ser siempre que utilicemos los atributos dentro
	#de una clase dentro de ella misma.
	def lanzarJuego (self):
		if self.ram < 1024:
			print("No se puede lanzar el juego. RAM insuficiente.")
		elif self.ram >= 1024 and self.ram < 2048:
			print("Corriendo juego en calidad media.")
		else:
			print("Corriendo a máxima calidad.")
	
	#Definimos un método que únicamente imprime algunos
	#atributos de esta clase.
	def verCaracteristicas (self):
		print("Color:", self.color)
		print("Tamaño:", self.tam)
		print("Cantidad de RAM", self.ram)

#Hacemos un objeto (instancia) de Computadora y lo inicializamos
#con los valores entre paréntesis. Éstos deben corresponder a lo
#definido en el constructor de nuestra clase.
computadoraVieja = Computadora("negro", 14, 3, 512, 1000)
#Hacemos otro objeto de Computadora y lo inicializamos.
computadora = Computadora("amarillo", 15, 6, 1500, 2000)
#Hacemos otro objeto de Computadora y lo inicializamos.
computadoraNueva = Computadora("gris", 17, 10, 4096, 5000)

#Utilizaré el método lanzarJuego() de dos objetos diferentes. 
#Nótese que éste está definido en la clase Computadora, pero como
#ambos objetos son instancias de la clase Computadora, ambos pueden
#utilizar este método aunque arrojarán diferentes resultados porque
#sus atributos tienen valores diferentes.
print("Lanzando juego en una computadora con altas características...")
computadoraNueva.lanzarJuego()
print("Lanzando juego en una computadora con bajas características...")
computadoraVieja.lanzarJuego()
print("Vemos las características de una computadora...")
computadoraVieja.verCaracteristicas()
#Vemos que computadoraVieja no puede lanzar el juego por su
#cantidad de RAM, entonces modificamos el atributo ram del objeto.
print("Modificando la RAM...")
computadoraVieja.ram = 1536
print("Vemos las características de una computadora...")
computadoraVieja.verCaracteristicas()
print("Lanzando juego en una computadora con características modificadas.")
computadoraVieja.lanzarJuego()