nota_1 = float(input("Primeira nota: "))

while nota_1 < 0 or nota_1 > 10:
    print("Nota inválida!")
    nota_1 = float(input("Coloque um valor de 0 a 10:- "))

nota_2 = float(input("Primeira nota: "))

while nota_2 < 0 or nota_2 > 10:
    print("Nota inválida")
    nota_2 = float(input("Coloque um valor de 0 a 10:-- "))

media = (nota_1 + nota_2) / 2
print(f"A média das duas notas é {media:.2f}")