n = int(input("Coloque números inteiros: "))
q = 1
total = 0

while n != 0:
    total = total + n
    n = int(input("Coloque números inteiros: "))
    q = q + 1 

print(f"Você digitou {q} números.")
print(f"A soma desses números é {total}.")
