"""Faça um programa que pergunte o número de horas trabalhadas no mês e o valor recebido
por hora. O programa deve calcular e exibir o salário total do mês."""

import math
horas = float(input("Digite o numero de horas trabalhadas no mes: "))
salHora = float(input("Digite o valor da hora de trabalho: "))
SalarioTotal = horas * salHora
print(SalarioTotal)
