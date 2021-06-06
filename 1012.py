import math

a = float(input())
b = float(input())
c = float(input())

print("TRIANGULO: ", round((a*(1/2)*c), 3))
print("CIRCULO: ", round(math.pi*(c**2), 3))
print("TRAPEZIO: ", round((1/2)*(a+b)*c, 3))
print("QUADRADO: ", round(b**2, 3))
print("RETANGULO: ", round(a*b, 3))

