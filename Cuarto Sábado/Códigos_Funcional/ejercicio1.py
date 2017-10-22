#-*-coding:utf-8-*-
import os
import math
#Para limpiar la pantalla sería: 
#windows->os.system("cls")
#linux-mac->os.system("clear")

def cuadrado(lado):
	resultado=lado*lado
	return resultado
def triangulo(base,altura):
	return (base*altura)/2
def circulo(radio):
	#pi=3.1416
	return math.pi*radio*radio
	#return pi*radio**2

while True:
	opcion=int(input("Elige la opción: \n 1.-Cuadrado\n2.-Triángulo\n3.-Círculo\n4.-Salir"))
	os.system("clear")
	if (opcion==1):
		lado=float(input("Ingresa un lado: "))
		print(cuadrado(lado))
	elif(opcion==2):
		base=float(input("Ingresa la base: "))
		altura=float(input("Ingresa la altura: "))
		print(triangulo(base,altura))
	elif(opcion==3):
		radio=float(input("Ingresa el radio: "))
		print(circulo(radio))
	elif(opcion==4):
		break










