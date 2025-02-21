import math

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('Reprovado: ' , media)
if media >= 5 and media <= 6.9:
    print('Recuperação: ', media)
if media >= 7:
    print('Aprovado: ', media)
