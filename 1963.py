v1,v2 = input().split()
v1,v2 = float(v1),float(v2)
if (v2-v1)==0:
	print("0.00%")
else:
	dif = v2-v1
	div = v1/dif
	porce = 100/div
	print("%.2f"%porce+"%")