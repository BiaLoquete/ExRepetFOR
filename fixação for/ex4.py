conta = 0

for n in range (5,101):
    if n % 7 == 0 and n %5 != 0:
        print(n)
        conta += 1

#para pular uma linha, o \n é dentro das aspas
print("\nQuantidade de números: ",conta)