c = int (input("Quantidade de clientes: "))
soma = 0

for n in range (1, c+1):
    temperatura = float(input("Digite a temperatura: "))

    #esse += ta falando que a variável soma vai receber um acréscimo do valor da temperatura
    soma += temperatura

    if temperatura < 37.2:
        print("Temperatura está normal")
    elif  temperatura >= 37.3 and temperatura < 38:
        print("Estado febril")
    elif  temperatura >= 38 and temperatura < 39:
        print("com febre")
    elif temperatura >= 39:
        print("Febre alta")

#calcular a média
media = soma/c
print("A media das temperaturas é: ",media, "e a quantidade de clientes é: ",c)