L_size = 5
list1 = []

even = 0
odd = 0
positive = 0
negative = 0

for i in range(L_size):
	n = int(input())
	if n % 2 == 0:
		even += 1
	else:
		odd += 1

	if n > 0:
		positive += 1
	elif n < 0:
		negative += 1

print("""%d valor(es) par(es)
%d valor(es) impar(es)
%d valor(es) positivo(s)
%d valor(es) negativo(s)""" %(even, odd, positive, negative))