A = int(input())
B = int(input())
C = int(input())

if A >= B+C :
    print("NAO FORMA TRIANGULO")
if A**2 == B**2 + C**2 :
    print("TRIANGULO RETANGULO")
if A**2 > B**2 + C**2 :
    print("TRIANGULO OBTUSANGULO")
if A**2 < B**2 + C**2 :
    print("TRIANGULO ACUTANGULO")
if A == B == C :
    print("TRIANGULO EQUILATERO")
if A == B == C :
    print("TRIANGULO ISOSCELES")