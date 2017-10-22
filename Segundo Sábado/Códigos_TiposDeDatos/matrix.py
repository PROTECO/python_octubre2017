#
#############################
# Tipos de datos basicos
#
# Matrices (listas anidadas)
############################

# Creamos una lista que contenga una lista de cinco elementos (del 0 al 4)
Matrix = [[0 for x in range(5)] for x in range(5)] 
#Podemos ingresad de la siguiente manera:

Matrix[0][0] = 1
Matrix[4][0] = 5

print (Matrix[0][0]) # impirme 1
print (Matrix[4][0]) # impirme 5



#Una forma mas facil es con el modulo numpy

import numpy
numpy.zeros((5, 5))
#creamos un array lleno de ceros
array([[ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.]])
#solo acedemos al metodo matrix
numpy.matrix([[1, 2],[3, 4]])
#Podemos hacerlo con listas
matrix([[1, 2],
        [3, 4]])
#Metodo para crear la matiz anterior
numpy.matrix('1 2; 3 4')