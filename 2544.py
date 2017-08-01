from math import log2
while True:
	try:
		n = int(input())
		print(int(log2(n)))
	except EOFError:
		break