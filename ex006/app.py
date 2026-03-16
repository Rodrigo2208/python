try:
    hora = int(input("Digite as horas trabalhadas no ano : "))
    hora_ex = int(input("Digite as horas extras trabalhadas no ano :"))
    valor = hora *10 + hora_ex * 15
    print (f"O valor a ser recebido é de {valor} R$")
except ValueError:
    print("Essa porra não é um número inteiro, porra!")