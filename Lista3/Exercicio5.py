N = int(input("Digite um número N para exibir os N primeiros termos da sequência de Fibonacci: "))

a, b = 0, 1

print(f"Os {N} primeiros termos da sequência de Fibonacci são:")
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b 
