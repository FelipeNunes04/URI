nums = int(input())
l = map(int, input().split())
mult2,mult3,mult4,mult5=0,0,0,0
for num in l:
	if(num%2==0): mult2+=1
	if(num%3==0): mult3+=1
	if(num%4==0): mult4+=1
	if(num%5==0): mult5+=1
print("%d Multiplo(s) de 2"%mult2)
print("%d Multiplo(s) de 3"%mult3)
print("%d Multiplo(s) de 4"%mult4)
print("%d Multiplo(s) de 5"%mult5)