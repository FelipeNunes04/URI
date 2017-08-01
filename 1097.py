z=7
y=4
for i in range(1,10,2):
	for x in range(z,y,-1):
		print("I=%d J=%d"%(i,x))
	z+=2
	y+=2