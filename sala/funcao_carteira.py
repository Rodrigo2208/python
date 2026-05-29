def carteira(continuidade):
    print('1-Ver saldo \n2-Deposito \n3-Saque \n4-Sair')
    while continuidade == 1:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            print("Olhando Saldo")
        elif opcao == 2:
            print("Depositando")
        elif opcao == 3:
            print("Sacando como eu saco")
        elif opcao == 4:
            print("saindo")
        continuidade = int(input("Deseja continuar? Sim(1); Não(2): "))
    return continuidade
continuidade = int(input("Deseja continuar? Sim(1); Não(2): "))
if carteira(continuidade):
    print("Parabens!!!")