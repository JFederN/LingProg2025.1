A = int(input("Digite o valor de A (limite inferior do intervalo): "))
B = int(input("Digite o valor de B (limite superior do intervalo): "))

if A > B:
    A, B = B, A

for i in range(A, B + 1):
    if i % 2 != 0:
        print(i)
