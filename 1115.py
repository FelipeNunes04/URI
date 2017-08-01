x = 1
y = 1
while(x!=0 and y!=0):
	entrada = input().split()
	x = int(entrada[0])
	y = int(entrada[1])
	if(x==0 or y==0):
		break
	elif(x>0 and y>0):
		print("primeiro")
	elif(x<0 and y>0):
		print("segundo")
	elif(x<0 and y<0):
		print("terceiro")
	else:
		print("quarto")