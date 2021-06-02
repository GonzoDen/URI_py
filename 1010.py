line1 = input().split(" ")
line2 = input().split(" ")

id1, quant1, price1 = line1
id2, quant2, price2 = line2

valor = int(quant1) * float(price1) + int(quant2) * float(price2)

print("VALOR A PAGAR: R$ %.2f" % valor)