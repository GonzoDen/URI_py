import math

isPrime = False

n = int(input())

for i in range(1, n+1):
	num = int(input())

	for j in range(2, int(math.sqrt(float(num)))):
		if num/j == 0:
			break
		else:
			isPrime == True
	print(isPrime)
