idade = 0
media = 0
cont = 0
while idade>=0:
	idade = int(input())
	if(idade<0):
		break
	else:
		media+=idade
		cont+=1
print("%.2f"%(media/cont))