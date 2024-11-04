# Contar números positivos inseridos pelo usuário Peça ao usuário para digitar números repetidamente até que ele digite 0. Exiba a quantidade de números positivos digitados


contador_positivos = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    elif numero > 0:
        contador_positivos += 1

print("Você digitou", contador_positivos, "números positivos.")
