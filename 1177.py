AR_SIZE = 10
ar = []

n = int(input())

for i in range (AR_SIZE):
	for j in range (n):
		ar.append(j)
	print("N[%d] = %d" % (i, ar[i]))