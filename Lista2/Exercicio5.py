import math
l1 = float(input("Digite o tamanho do primeiro lado: "))
l2 = float(input("Digite o tamanho do segundo lado: "))
l3 = float(input("Digite o tamanho do quarto lado: "))

if(l1+l2) > l3:
    print("Triangulo valido")
if(l1+l3) > l2:
    print("Triangulo valido")
if(l2+l3) > l1:
    print("Triangulo valido")
