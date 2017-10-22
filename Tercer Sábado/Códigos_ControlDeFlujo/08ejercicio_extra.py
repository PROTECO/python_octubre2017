#-*-Coding:utf-8-*-

#Contar palabras

'''Este ejericicio no lo logramos a ver, pero la idea es:
Dar le un texto al programa y que cuente cuantas palabras de cada tipo le dimos.
con la ayuda de un diccionario, cada palabra nueva que veamos la agregaremos como llave y 
la clave será un varor de uno
Si encontramos mas veces esta palabra solamente iremos aumentando la clave.
Si tienen dudas mandenos mensajes o el siguiente sábado comentenos para ayudarles.
'''
counts = dict()
print ("Dame un texto:")
line = input("")
words = line.split()
print ("La lista de palabrar es:", words)
for word in words:
     counts[word] = counts.get(word,0) + 1
print ("Todas estas palabras (con y sin repeticiones) me has dado", counts)