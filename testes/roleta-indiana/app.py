try:
    import random

    num = random.randint(1, 5468220)

    valor = int(input("-Escolha um número entre 1 e 5468220: "))

    if valor == num:
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print("-Não nasceu na Índia mas você continua sendo gay")
    elif valor < 1 or valor > 5468220:
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print("-Tentou burlar as regras? Além de indigéna nasceu com uma mutação genêtica rara, seu pai comeu uma vaca sagrada")
        print("-Parabéns, você agora tem duas bundas")
    else:
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print("-Vai nascer Índia seu gay")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    res = input("-Deseja ser abortado? Responda apesnas com Sim ou Não: ")

    if res == "Sim" or res == "sim":
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print("-Você foi servido como tira gosto nas ruas igienizadas da Índia (;")
    elif res == "Não" or res == "não":
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print("-Péssima escolha );")
    else:
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print("-Além de torto é burro.")

    print(f"O número era: {num}")

except ValueError:
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("Número muito grande ou inválido!")