import math

a, b, c = list(map(float, input().split(" ")))
#map function completes function "float" with input.split(" ") as an arg
#list is one of 4 built-in data types for storing data, changeable

pi = round(math.pi, 5) 
#not that sure whether reserving memory for the new var
#is a good decision, yet it is definitely better than magic

triangle = a*(1/2)*c
cicrcle = pi*(c**2)
trapezium = (1/2)*(a+b)*c
square = b**2
rectangle = a*b
#round() cannot be used when there is exact precision of 3 digits
#after zero no matter what, so you have to do this mumbo jumbo

print("TRIANGULO: %.3f" % triangle)
print("CIRCULO: %.3f" % cicrcle)
print("TRAPEZIO: %.3f" % trapezium)
print("QUADRADO: %.3f" % square)
print("RETANGULO: %.3f" % rectangle)