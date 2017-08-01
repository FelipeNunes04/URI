temperatura = input()
temperatura = temperatura.split()
temp1 = int(temperatura[0])
temp2 = int(temperatura[1])
temp3 = int(temperatura[2])
if temp1>temp2 and temp2<=temp3:
	print(":)")
elif temp1<temp2 and temp2>=temp3:
	print(":(")
elif (temp1<temp2 and temp2<temp3) and ((temp3-temp2)<(temp2-temp1)):
	print(":(")
elif (temp1<temp2 and temp2<temp3) and ((temp3-temp2)>=(temp2-temp1)):
	print(":)")
elif (temp1>temp2 and temp2>temp3) and ((temp2-temp3)<(temp1-temp2)):
	print(":)")
elif (temp1>temp2 and temp2>temp3) and ((temp2-temp3)>=(temp1-temp2)):
	print(":(")
elif temp1 == temp2:
	if temp3>temp2:
		print(":)")
	else:
		print(":(")
