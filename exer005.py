# Classificação por idade Peça a idade do usuário e exiba se ele é:
# Criança (até 12 anos)
# Adolescente (de 13 a 17 anos)
# Adulto (18 anos ou mais)
print('=============================================================')
idade = int(input('Digite sua Idade: '))
print('=============================================================')

if (idade <= 12):
    print('Pela sua Idade vc é uma CRIANÇA!')
elif (idade > 12 and idade <= 17):
    print('Pela sua Idade vc é ADOLESCENTE!')
else:
    print('Pela sua Idade vc é ADULTO!')
print('=============================================================')
