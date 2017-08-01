while True:
	try:
		n = int(input())
		maior = 0
		for i in range(1,n+1):
			t,d = map(int, input().split())
			if(d/t>maior):
				print(i)
				maior = d/t
	except EOFError:
		break