try:
    num = int(input("Coloque um número: "))

    if num >= 100 and num <= 999:
        print(f"{num // 100} é o primeiro dígito de {num}")
        print(f"{num % 100 // 10} é o segundo dígito de {num}")
        print(f"{num % 10} é o terceiro dígito de {num}")
    else:
        print(f"{num} não é um número de três dígitos")
except ValueError:
    print("Essa porra não é um número inteiro")