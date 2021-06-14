L_SIZE = 10
list1 = []

for i in range(L_SIZE): #list is iterable int is not
	n = int(input())
	if n <= 0:
		n = 1
		list1.append(n)
	else:
		list1.append(n)
	print("X[%d] = %d" % (i, n))