try: 
    numero = int(input("Coloque um número: "))

    if numero > 0:
        print(f"{numero} é psitivo")
    elif numero < 0:
        print(f"{numero} é negativo")
    else:
        print(f"{numero} é nulo")

except ValueError:
    print("não é um número intiro")