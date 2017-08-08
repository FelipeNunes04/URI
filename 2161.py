n = int(input())
if(n==0):
	print("%.10f"%3)
else:
	fracao = 6
	for i in range(1,n):
		fracao=6+(1/fracao) 
	print("%.10f"%(1/fracao+3))