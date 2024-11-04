# Fatorial de um número Receba um número inteiro positivo e exiba seu fatorial (ex.: 5! = 5 × 4 × 3 × 2 × 1 = 120).

num =  int(input('Digite um número: '))

fatorial = 1

if num < 0:
    print('Fatorial não para 0')
else:
    for i in range(1, num + 1):
     fatorial = fatorial * i
     print(f"O fatorial de {num} é {fatorial}")  