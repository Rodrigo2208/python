a1 = int(input("insira um valor: "))
a2 = int(input("insira um valor: "))
a3 = int(input("insira um valor: "))
a4 = int(input("insira um valor: "))
a5 = int(input("insira um valor: "))

maior = a1
menor = a1

if a2 > a1:
    maior = a2
elif a3 > a2:
    maior = a3
elif a4 > a3:
    maior = a4
elif a5 > a4:
    maior = a5

if a2 < a1:
    menor = a2
elif a3 < a2:
    menor = a3
elif a4 < a3:
    menor = a4
elif a5 < a4:
    menor = a5
    
print(f"O maior número é {maior} e o menor é {menor}.")
