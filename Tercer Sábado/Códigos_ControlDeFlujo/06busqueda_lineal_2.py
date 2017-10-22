#-*-Coding:utf-8-*-

num_pequenno = None
print ("Al iniciar el numero vale:", num_pequenno)
for num_posible in [9, 41, 12, 3, 74, 15] :
   if num_posible < num_pequenno :
      num_pequenno = num_posible
   print num_pequenno, num_posible
print ("El numero mas pequeño es:", num_pequenno)