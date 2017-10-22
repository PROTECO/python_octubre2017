#-*-coding:utf-8-*-
"""
def factorialIterativo(n):
	acum=1
	if n==1 or n==0:
		return 1
	else:
			for num in range(1,n+1):
				acum=acum*num
				#acum*=acum Forma corta de hacer lo de arriba
			return acum
print("El factorial de %d es %d"%(0,factorialIterativo(0)))
print("El factorial de %d es %d"%(1,factorialIterativo(1)))
print("El factorial de %d es %d"%(2,factorialIterativo(2)))
print("El factorial de %d es %d"%(3,factorialIterativo(3)))
print("El factorial de %d es %d"%(10,factorialIterativo(10)))

def factorialRecursivo(n):
	if n<2:
		return 1
	return n*factorialRecursivo(n-1)

print("El factorial recursivo de %d es %d"%(0,factorialRecursivo(0)))
print("El factorial recursivo de %d es %d"%(1,factorialRecursivo(1)))
print("El factorial recursivo de %d es %d"%(2,factorialRecursivo(2)))
print("El factorial recursivo de %d es %d"%(3,factorialRecursivo(3)))
print("El factorial recursivo de %d es %d"%(1000,factorialRecursivo(999)))
"""
#Recursión doble, que se termina las llamas el doble de rapido
def fibo(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		print(fibo(n-1)+fibo(n-2))
		return fibo(n-1)+fibo(n-2)

print("El fibonacci de %d es %d"%(0,fibo(0)))
print("El fibonacci de %d es %d"%(1,fibo(1)))
print("El fibonacci de %d es %d"%(2,fibo(2)))
print("El fibonacci de %d es %d"%(3,fibo(3)))
print("El fibonacci de %d es %d"%(4,fibo(4)))
print("El fibonacci de %d es %d"%(10,fibo(10)))
print("El fibonacci de %d es %d"%(10,fibo(10)))




