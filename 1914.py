n = int(input())
for i in range(n):
	jog1,esco1,jog2,esco2 = input().split()
	num1,num2 = input().split()
	soma = int(num1)+int(num2)
	if(soma%2==0):
		if(esco1=="PAR"):
			print(jog1)
		else:
			print(jog2)
	else:
		if(esco1=="IMPAR"):
			print(jog1)
		else:
			print(jog2)