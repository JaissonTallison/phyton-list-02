# Soma apenas de números pares até N.
# Peça ao usuário um número N e exiba a soma de todos os números pares de 1 até N.

num = int(input('Digite um número: '))

soma = 0

for num in range(2, num + 1, 2):
    soma += num
print(f"A soma dos números pares de 1 até", num, "é:", soma)
