"""Faça um programa que leia uma temperatura em graus Celsius e a converta para Fahrenheit.
A fórmula de conversão é: F = (Cx9/5)+ 32 """

import math

celsius = float(input("Informe a temperatura em Celsius: "))
fahrenheit = 9 * celsius / 5 + 32
print("fahrenheit: ", fahrenheit)


