# Contagem regressiva de 10 a 0.
# Implemente uma contagem regressiva de 10 até 0 e exiba "Fogo!" ao final.
import time
print('====================================================')


num = int(input('Digite o valor para contagem: '))

print('====================================================')

while num >= 0:
    print(f'{num}')
    time.sleep(1)
    num = num - 1
print('Olha a bala viado!!!')
print('====================================================')
