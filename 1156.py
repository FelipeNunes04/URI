s = 1
soma = 1
for i in range(3,40,2):
	soma += soma
	s += float(i/soma)
print("%.2f"%s)
