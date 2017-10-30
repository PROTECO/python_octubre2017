#########################
##### POLIMORFISMO ######
#########################
"""
El polimorfismo es la capacidad que tiene un objeto de adaptarse
para responder a algún llamado que se le hace.
"""
#Defino una clase Perro.
class Perro:
	#Defino un atributo nombre.
	def __init__ (self, nombre):
		self.nombre = nombre

	#Defino un método jugar que interactúa con un objeto llamado
	#amigo. Si el objeto amigo tiene un atributo llamado nombre,
	#podremos interactuar con él. A ésto se refiere el polimorfismo;
	#el objeto se puede adaptar al método que lo esté mandando llamar.
	def jugar (self, amigo):
		print(self.nombre, "juega con", amigo.nombre)

#Instancío dos objetos de la clase Perro con nombres diferentes.
perro1 = Perro("Paco")
perro2 = Perro("Difo")
#Hago que perro1 interactúe con perro2. La interacción debe ser exitosa
#por la forma en que yo definí este método.
perro1.jugar(perro2)
#perro1.jugar([1,2,3])
#La línea anterior marcaría error. La clase a partir de la cual se
#instancían las listas no pueden adaptarse al método que la pretende utilizar.