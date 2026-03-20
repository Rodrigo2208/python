cod_peca1, num_peca1, val_peca1 = input().split()
cod_peca1 = int(cod_peca1)
num_peca1 = int(num_peca1)
val_peca1 = float(val_peca1)

tot_peca1 = num_peca1 * val_peca1

print(f"VALOR A PAGAR: R$ {tot_peca1:.2f}")
