L_SIZE = 20
list1 = []

for i in range(L_SIZE):
	list1.append(int(input()))

for i in range(L_SIZE):
	print("N[%d] = %d" % (i, list1[(L_SIZE-1)-i]))
