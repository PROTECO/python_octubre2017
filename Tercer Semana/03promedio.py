#-*-Coding:utf-8-*-

#Promedio de una lista
count = 0
suma = 0
print ("Al inicio los contadores valen: ", count, suma)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    suma = suma + value
    print ("Tenemos en la vuelta actual ",count, "elementos, la suma de los elemtnos es ", suma)
print ("Al final sabemos que existen ", count, "elemntos en el arrelgo y la suma total es: ", suma, "El promedio por lo tanto es: ", suma / count)
