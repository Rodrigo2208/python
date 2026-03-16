valor_1 = int(input("Digite o primeiro valor: "))
valor_2 = int(input("Digite o segundo valor: "))

while valor_2 == 0:
    valor_2 = int(input("Digite um número diferente de 0: "))   
print(f"{valor_1} / {valor_2} = {valor_1 / valor_2}")
            