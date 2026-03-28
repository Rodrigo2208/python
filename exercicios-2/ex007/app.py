n = int(input("Coloque números inteiros: "))
f = 0
q = n
total = 1

while f < q:
    total = total * n
    f = f + 1
    n = n - 1

print(f"O fatorial de {q}! é {total}.")