from math import sqrt
n = int(input())
fibonacci = (pow(((1+sqrt(5))/2),n)-pow(((1-sqrt(5))/2),n))/sqrt(5)
print("%.1f"%fibonacci)