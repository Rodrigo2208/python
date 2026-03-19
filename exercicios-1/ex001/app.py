try:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0 :
        print(f"{numero} é par!")
    else:
        print(f"{numero}  é ímpar!")
except ValueError:
    print("Digite apenas números inteiros.")
    