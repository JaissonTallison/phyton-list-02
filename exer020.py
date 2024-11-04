# Simular um caixa eletrônico Peça ao usuário o valor de um saque e exiba a quantidade de cédulas de 50, 20, 10 e 1 necessárias para o saque. Considere que o valor será sempre um número inteiro positivo

valorSaque = int(input("Digite o valor a ser sacado: "))

cedulas = [50, 20, 10, 1]
for c in cedulas:
    quantidadeCedulas = valorSaque // c
    valorSaque %= c
    if quantidadeCedulas > 0:
        print(f"{quantidadeCedulas} cédulas de R${c}")
