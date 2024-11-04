# Tabuada de um número.
# Peça um número e exiba sua tabuada de 1 a 10.
print('============TABUADA==================')

num = int(input('Informe um número: '))

print('=====================================')


for i in range(1, 11):
    tabuada = num * i
    print(f'{num} x {i} = {tabuada}')

print('=====================================')
