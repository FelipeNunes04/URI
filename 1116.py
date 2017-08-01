n = int(input())
for i in range(0,n):
	entrada = input().split()
	x = float(entrada[0])
	y = float(entrada[1])
	if(y==0):
		print("divisao impossivel")
	else:
		print("%.1f"%(x/y))