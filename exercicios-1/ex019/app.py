valor = int(input("Digite um valor inteiro entre 1 e 10: "))

num = 0

while valor < 1 or valor > 10:
    print("Valor inválido!!!")
    valor = int(input("Digite um valor inteiro entre 1 e 10: "))

while num < 10:
    num = num + 1
    print(f"{valor} * {num} = {valor * num}")
