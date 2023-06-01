mulher = 0
homem = 0
soma = 0
idhomem = 0
idmulher = 0
idgeral = 0


for n in range (1,11):
    g = int(input("Digite seu gênero: 1 para mulher e 2 para homem: "))
    idade = int(input("Digite a idade:"))
    idgeral += idade

    if g == 1:
        idmulher += idade
        mulher +=1
    elif g == 2:
        idhomem +=idade
        homem += 1

mediaM = idmulher/mulher
mediaH = idhomem / homem
media = idgeral/10

print("A média de mulheres é ", mediaM)
print("A média de homens é ", mediaH)
print("A média geral é ", media)


