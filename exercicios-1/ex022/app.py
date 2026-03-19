idade = int(input("Escreva sua idade: "))

if idade > 4 and idade < 8:
    print("Infantil A")
elif idade > 7 and idade < 11:
    print("Infantil B")
elif idade > 10 and idade < 14:
    print("juvenil A")
elif idade > 13 and idade < 18:
    print("juvenil B")
elif idade > 18:
    print("sênior")
else:
    print("Você ainda é menino novo!!!")