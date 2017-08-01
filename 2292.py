import time
n = int(input())
for i in range(n):
	entrada = input().split()
	inicio = time.time()
	l = entrada[0]
	lamp = []
	for i in l:
		lamp.append(i)
	c = int(entrada[1])
	for i in range(c):
		if lamp[0]=='O':
			lamp[0] = 'X'
			for i in range(1,len(lamp)):
				if lamp[i-1]=='X':
					if lamp[i]=='O':
						lamp[i] = 'X'
					else:
						lamp[i] = 'O'
						break
		else:
			lamp[0] = 'O'
	l = ''.join(lamp)
	fim = time.time()
	print(fim - inicio)
	print(l)