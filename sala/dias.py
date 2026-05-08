dias = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

dia = int(input("Escreva o atual dia: "))
mes = int(input("Escreva o atual mês: "))
soma = 0
for i in range (0, mes):
    soma = soma + dias[i]
print(soma + dia)


    

