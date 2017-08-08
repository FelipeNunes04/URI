notas = [2, 5, 10, 20, 50, 100]
while True:
	n,m=map(int, input().split())
	troco = m-n
	if(n==0 and m==0):
		break
	elif troco<4:
		print("impossible")
	elif (any(i==troco%2 for i in notas) and troco//2==1) or \
	(any(i==troco%5 for i in notas) and troco//5==1) or \
	(any(i==troco%10 for i in notas) and troco//10==1) or \
	(any(i==troco%20 for i in notas) and troco//20==1) or \
	(any(i==troco%50 for i in notas) and troco//50==1) or \
	(any(i==troco%100 for i in notas) and troco//100==1) or\
	any(i*2==troco for i in notas):
		print("possible")
	else:
		print("impossible")