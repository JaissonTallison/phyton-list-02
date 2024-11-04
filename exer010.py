# Verificar se um número é múltiplo de 3 e 5
# Peça um número e verifique se ele é divisível por 3 e por 5 ao mesmo tempo.
print('=============================================================')

num = int(input('Digite um número: '))
print('=============================================================')

if (num % 5 != 0):
    print(f'O número {num} não é multiplo de 5')
else:
    somaAlg = sum(int(digito) for digito in str(num))
    if (somaAlg % 3 == 0):
        print(f'O número {num} é multiplo de 3 e 5')
    else:
        print(f'O {num} multiplo de 5, mas não de 3')
        
print('=============================================================')
