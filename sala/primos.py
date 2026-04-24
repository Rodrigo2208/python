import math
n = int(input("Digite um número inteiro positivo: "))
primo = True
for i in range (2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        primo = False
if primo == True:
    print(f"{n} é primo")
else:
    print(f"{n} não é primo")
