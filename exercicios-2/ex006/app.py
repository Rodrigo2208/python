q = 1
par = 0
impar = 0

while q < 11:
    q = q + 1
    n = int(input("Coloque números inteiros: "))
    n = n % 2
    if n == 0:
        par = par + 1
    else:
        impar = impar + 1

print(f"Você digitou {par} números pares e {impar} números impáres.")