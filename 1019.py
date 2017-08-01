x = int(input())
h = int(x/3600)
x = x%3600
m = int(x/60)
s = x%60
print("%d:%d:%d"%(h,m,s))