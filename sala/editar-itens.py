compras = []
opcao = 0
while opcao != 0:
    print("1 inserir iten\n1 excluir iten\n1 editar iten\n1 listar iten\n1 sair \n")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        nome = input("Nome: ")
        quantidade = input("quantidade: ")
        valor = input("valor: ")
        iten = [nome, quantidade, valor]
        compras.append(iten)
    elif opcao == 2:
        editar = int(input("Qual o intem que deseja editar?: "))
        
