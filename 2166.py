n = int(input())
if(n==0):
	print("{:.10f}".format(1))
elif(n==1):
	print("{:.10f}".format(1.5))
else:
	fracao = 2
	for i in range(1,n):
		fracao=2+(1/fracao)#fracao = 2+(1/2), fracao = 2+(1/2.5), fracao = 2+(1/2.4)
	print("{:.10f}".format(1/fracao+1))