# Calculadora Simples O programa deve pedir dois números e uma operação (+, -, *, /) e exibir o resultado da operação entre os números.


print('=============================================================')
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print('=============================================================')
opcao = input('Escolha uma operação: ')
print('=============================================================')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
if opcao == '1':
    soma = num1 + num2
    print(f'A soma é: {soma}')
elif opcao == '2':
    subtracao = num1 - num2
    print(f'A subtração é: {subtracao}')
elif opcao == '3':
    multi = num1 * num2
    print(f'O resultado da multiplicão é: {multi}')
elif opcao == '4':
    if num2 == 0:
        print('Divisão por zero não EXISTE!')
    else:
        div = num1 / num2
        print(f'O resultado da Divisão é: {div}')
else:
    print("Opção inválida.")
print('=============================================================')
