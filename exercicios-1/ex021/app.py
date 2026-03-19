x = int(input("Digite o valor de X: "))
n = int(input("Digite o valor de N: "))

soma = 0
num = 1

while num <= n:
    soma = soma + x ** num
    num = num + 1

print("Resultado:", soma)