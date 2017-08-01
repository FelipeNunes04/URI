n = 1
while n!=0:
	n = int(input())
	soma = 0
	if n==0:
		break
	else:
		if n%2==1 or n%2==-1:
			n += 1
			for x in range(0,5):
				soma+=n
				n+=2
		else:
			for x in range(0,5):
				soma+=n
				n+=2
	print(soma)
	n = 1
