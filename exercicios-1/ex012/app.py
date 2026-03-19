hora = float(input("Digite as horas trabalhadas no ano : "))
hora_ex = float(input("Digite as horas extras trabalhadas no ano :"))
valor = hora * 10 + hora_ex * 15
valor_max = 12000

if valor <= valor_max:
    imposto = valor * 0.1
    print(f"Vai receber {imposto} de imposto. Faz o l")
else:
    imposto = (valor_max * 0.1) + ((valor - valor_max) * 0.25)
    print(f"vai receber {imposto} de imposto. Faz o L")

resposta = input("Deseja fazer um novo cálculo?")

while resposta == "sim" or resposta == "Sim":
    hora = float(input("Digite as horas trabalhadas no ano : "))
    hora_ex = float(input("Digite as horas extras trabalhadas no ano :"))
    valor = hora * 10 + hora_ex * 15
    valor_max = 12000

    if valor <= valor_max:
        imposto = valor * 0.1
        print(f"Vai receber {imposto} de imposto. Faz o l")
    else:
        imposto = (valor_max * 0.1) + ((valor - valor_max) * 0.25)
        print(f"vai receber {imposto} de imposto. Faz o L")

    resposta = input("Deseja fazer um novo cálculo?")

print("Fim do programa")
