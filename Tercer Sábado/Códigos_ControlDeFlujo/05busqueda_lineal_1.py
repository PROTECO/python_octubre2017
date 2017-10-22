#-*-Coding:utf-8-*-

#Busar el elemetno mas grande de una lista
num_grande = -1
print ("Al iniciar el numero vale:", num_grande)
for num_posible in [9, 41, 12, 3, 74, 15] :
   if num_posible > num_grande :
      num_grande = num_posible
print ("El numero mas grande es", num_grande)
