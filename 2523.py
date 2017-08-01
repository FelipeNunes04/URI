while True:
	try:
		letras = input()
		n = int(input())
		pos = list(map(int, input().split()))
		saida = [letras[i-1] for i in pos]
		saida  = ''.join(saida)
		print(saida)
	except EOFError:
		break