for i in range(0,22,2):
	fi = float(i)
	for j in range(1,4):
		if((fi/10)==2.0 or (fi/10)==1.0 or (fi/10)==0.0):
			print ("I=%d J=%d"%(i/10,j+int(fi/10)))
		else:
			print ("I=%.1f J=%.1f"%(fi/10.0,j+(fi/10.0)))