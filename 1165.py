#TODO: correct

import math

isPrime = True

n = int(input())

for i in range(n):
	num = int(input())

	for j in range(1, num+1):

		if num % j == 0 and j != 1 and j != num:
			isPrime = False
		else:
			isPrime == True

	if isPrime == True:
		print("%d eh primo" % num)
	else:
		print("%d nao eh primo" % num)
