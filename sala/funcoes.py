def e_bisexto(Ano):
    r = Ano % 4 == 0 and Ano %100 != 100 or Ano % 400 == 0
    return r
Ano = int(input("Digite um número: "))
if e_bisexto(Ano):
    print ("o ano é bi")
else:
    print("Não é bi")