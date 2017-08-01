
n = int(input())
if n>0 and n<= 10**6:
	hos = []
	for i in range(n):
		hos.append("Ho")
	sHos = " ".join(hos)
	print("%s!"%sHos)