n = int(input("Coloque números inteiros: "))

if n <= 1:
    print("Não é primo")
else:
    i = 2
    primo = True

    while i < n:
        if n % i == 0:
            primo = False
            break
        i += 1

    if primo:
        print("É primo")
    else:
        print("Não é primo")