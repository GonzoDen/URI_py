line1 = input().split(" ")
line2 = input().split(" ")

x1, y1 = line1
x2, y2 = line2

def distance_btw_points(x1, y1, x2, y2):
	distance = ((float(x2)-float(x1))**2 + (float(y2)-float(y1))**2)**(1/2)
	return distance





print("%.4f" % distance_btw_points(x1, y1, x2, y2))

