try:
    hora = int(input("Digite a hora: "))
    hora_ex = int(input("Digite a hora extra: "))
    valor = hora *10 + hora_ex * 15
    print (f"O valor a ser recebido é de {valor} R$")
except ValueError:
    print("Essa porra não é um número inteiro, porra!")