n=int(input())
for i in range(n):
	t = int(input())
	if(t>=2015):
		ano = 2015-t-1
		print("%d A.C."%(ano*-1))
	else:
		ano = 2015-t
		print("%d D.C."%ano)