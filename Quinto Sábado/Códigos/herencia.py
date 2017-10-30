#########################
####### HERENCIA ########
#########################
"""
La herencia nos permite crear una clase partiendo de otra.
Una clase padre heredará todos sus métodos y atributos a 
todas sus clases hijas, permitiéndoles utilizarlos como si
fueran sus propios.
"""
#Defino una clase Figura.
class Figura:
	#En mi constructor defino los atributos de área y perímetro,
	#pues sé que son características generales que tiene una figura.
	def __init__ (self, area, perimetro):
		self.area = area
		self.perimetro = perimetro

#Defino una clase Cuadrado. Entre paréntesis coloco la clase
#de la cual va a heredar, en este caso, figura.
class Cuadrado(Figura):
	#Defino un constructor para el cuadrado. Únicamente defino
	#el atributo lado, que es propio de un cuadrado, pero de 
	#Figura se heradará el atributo área y perímetro.
	def __init__ (self, lado):
		self.lado = lado

	#Este método utiliza el atributo area como uno propio,
	#pero le fue heredado de Figura.
	def calcularArea(self):
		self.area = self.lado**2
		print("El área del cuadrado es:", self.area)

class Hexagono(Figura):
	#Defino un constructor para un hexágono. Únicamente defino
	#atributos lado y apotema, propios de un hexágono, pero de 
	#Figura se heradará el atributo área y perímetro.
	def __init__ (self, lado, apotema):
		self.lado = lado
		self.apotema = apotema

	#Este método utiliza el atributo perimetro como uno propio,
	#pero le fue heredado de Figura.
	def calcularPerimetro (self):
		self.perimetro = self.lado*6

	#Este método utiliza los atributos area y perimetro como
	#propios, pero le fue heredados de Figura.
	def calcularArea(self):
		self.calcularPerimetro()
		self.area = self.perimetro*self.apotema
		print("El área del hexágono es:", self.area)

#Instancío un Cuadrado de lado 3. En este caso, los atributos que
#heredamos de Figura se calculan a partir de métodos.
cuadrito = Cuadrado(3)
cuadrito.calcularArea()

#Instancío un Cuadrado de lado 1 y apotema 2. En este caso, los
#atributos que heredamos de Figura se calculan a partir de métodos.
hexa = Hexagono(1, 2)
hexa.calcularArea()


