entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])
if(a==b or a==c or b==c):
	print("S")
elif(a+b==c or a+c==b or b+c==a):
	print("S")
else:
	print("N")