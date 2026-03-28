ano = int(input("Coloque um ano: "))

if ano % 4 == 0 or ano % 400 == 0 and not ano % 100 == 0:
    print("O ano é bissexoto")
elif ano % 4 == 0 and ano % 100 == 0:
    print("Isso não é um ano bissexto")
else:
    print("Isso não é um ano bissexto")
