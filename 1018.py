#TODO: apply data structures and for
cash = int(input())

cash100 = int(cash / 100)
cash50 = int(cash % 100 / 50)
cash20 = int(cash % 100 % 50 / 20)
cash10= int(cash %100 %50 % 20 / 10)
cash5 = int(cash %100 %50 %20 % 10 / 5)
cash2 = int(cash %100 %50 %20 %10 %5 /2)
cash1 = int(cash %100 %50 %20 %10 %5 %2)

print(cash)
print("%d nota(s) de R$ 100,00" % cash100)
print("%d nota(s) de R$ 50,00" % cash50)
print("%d nota(s) de R$ 20,00" % cash20)
print("%d nota(s) de R$ 10,00" % cash10)
print("%d nota(s) de R$ 5,00" % cash5)
print("%d nota(s) de R$ 2,00" % cash2)
print("%d nota(s) de R$ 1,00" % cash1)