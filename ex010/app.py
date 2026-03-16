litros = float(input("Média de consume de litros de combustível po mês: "))
preco = 6.13

if litros <= 50000:
    print(f"{preco * 1.20:.2f} é o novo valor da gasoza")
else:
    print(f"{preco * 1.12:.2f} é o novo valor da gasoza")