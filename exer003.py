# Maior entre dois números. Receba dois números e exiba qual deles é maior, ou diga se são iguais.
print('=============================================================')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
print('=============================================================')
if num1 > num2:
    print(f'O número {num1} é maior que o número {num2}')
elif num1 < num2:
    print(f'O número {num2} é maior que o número {num1}')
else:
    print(f'Os Números {num1} e {num2} iguais!')

print('=============================================================')
