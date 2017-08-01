n = 0
sai = 0
media = 0
while sai<2:
	n = float(input())
	if(n<0 or n>10):
		print("nota invalida")
	else:
		media+=n
		sai +=1
	if(sai==2):
		print("media = %.2f"%(media/2))
		break