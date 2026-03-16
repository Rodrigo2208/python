try:
    num = int(input("Coloque um número inteiro:"))

    if num >= 0 and num <=9:
        print(f"{num} está entre 0 e 9") 
    else:
        print(f"{num} não está entre 0 e 9")

except ValueError:
    print("Essa porra não é um número inteiro")