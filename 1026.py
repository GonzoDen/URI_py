while True:
	try:
		line = input().split()
	
		a, b = line

		s = int(a)^int(b) #in python "^" stads for exclusive-or

		print(s)

	except:
		break
