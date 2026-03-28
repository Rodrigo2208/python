numero = int(input("Coloque um número: "))
limite = 0
sequencia = 0
sequencia1 = 1

if numero%2 == 0:
    while numero/2 > limite:
        print(sequencia)
        print(sequencia1)
        sequencia = sequencia + sequencia1
        sequencia1 = sequencia1 + sequencia
        limite = limite + 1
else:
    while numero > limite:
        print(sequencia)
        sequencia = sequencia + sequencia1
    while numero > limite:
        print(sequencia1)
        sequencia1 = sequencia1 + sequencia
        limite = limite + 1