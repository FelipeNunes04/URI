entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])

q = int(a/b)
r = a%b
if(r<0):
	r = a - (q*b)
elif(r>0 and q<0):
	q-=1
print(q,r)