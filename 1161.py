from math import factorial
while True:
	try:
		entrada = input().split()
		a,b = int(entrada[0]),int(entrada[1])
		print(factorial(a)+factorial(b))
	except EOFError:
		break
