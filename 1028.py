#TODO ask why there was "time limit exceeded in URI report"
n = int(input())

for i in range(n):
	n1, n2 = list(map(int, input().split(" ")))
	temp = 0
	nod = 0

	if (n1 > n2):
		temp = n1 
		n1 = n2
		n2 = temp 

	for j in range(1, n1+1):
		if (n1 % j == 0 and n2 % j == 0):
			nod = j

	print(nod)