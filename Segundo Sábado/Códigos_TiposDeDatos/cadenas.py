##########################
# Tipos de datos basicos
#
# Cadenas
##########################

a = "Hola mundo"    #declaracion entre comillas o comillas simples
b = 'Hola'          #Se puede usar indistinto, pero por convencion se usa:
					# ""-> cuando vas a modificar la cadena
					# ''-> cuando es un mensaje simple que no va a cambiar
print (a[3])          #pueden ser indexadas
#a[0] = 2           #Son inmutables (si se descomenta la linea, el programa marca error)
print (a[3:7])        #Subcadenas (intervalo no inclusive, aqui devuelve del indice 3 al 6)
print (a+a)           #Concatenacion
print (a*5)          #Concatenacion multiple

b=5						#b ahora es un numero, ya que hace uso del tipado dinamico
#a+b                  #El tipado fuerte impide que podamos sumar o concatenar cadenas con numeros

#Tipos de cadena
print ("Hola mundo \n")     #cadenas normales Toma el \n como salto del linea
print (r"Hola mundo \n")    #cadenas crudas. No toman las antidiagonales como secuencias de escape


#Impresion con formato
a = 3 
print ("El valor de a es ",a)             #solo imprimir una cosa tras otra
print ("El valor de a es %d y de b es %d" % (a,b))   #Poner entre los parentesis, separados por comas, (una tupla)
                                       #las variables que han de sustituir a los formatos de codigo (%d)
print ("El valor de a es {0}".format(a)) #Por medio de un metodo


