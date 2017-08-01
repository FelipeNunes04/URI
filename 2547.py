while True:
	try:
		n,minimo,maximo = map(int, input().split())
		cont = 0
		for i in range(n):
			altura = int(input())
			if(altura>=minimo and altura<=maximo): cont+=1
		print(cont)
	except EOFError:
		break