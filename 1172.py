L_SIZE = 10
list = []

for i in range(L_SIZE): #list is iterable int is not
	n = int(input())
	if n <= 0:
		n = 1
		list.append(n)
	else:
		list.append(n)
	print("X[%d] = %d" % (i, n))