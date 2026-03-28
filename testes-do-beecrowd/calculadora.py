n1 = float(input("Coloque um valor: "))
operador = input("Coloque um operador: ")
n2 = float(input("Coloque um valor: "))

if operador == "+":
    print(f"{n1} + {n2} = {n1 + n2}")
elif operador == "-":
    print(f"{n1} - {n2} = {n1 - n2}")
elif operador == "*":
    print(f"{n1} * {n2} = {n1 * n2}")
elif operador == "/":
    print(f"{n1} / {n2} = {n1 / n2}")
elif operador == "//":
    print(f"{n1} // {n2} = {n1 // n2}")
elif operador == "**":
    print(f"{n1} ** {n2} = {n1 ** n2}")
elif operador == "%":
    print(f"{n1} % {n2} = {n1 % n2}")