x=0
y=1
while x!=y:
	entrada = input().split()
	x = int(entrada[0])
	y = int(entrada[1])
	if(x==y):
		break
	elif(x>y):
		print("Decrescente")
	else:
		print("Crescente")
