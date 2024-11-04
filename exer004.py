# Verificar se o ano é bissexto Peça ao usuário um ano e determine se ele é bissexto (divisível por 4, mas não por 100, exceto se for divisível por 400).

print('=============================================================')
ano = int(input('Digite um ano: '))
print('=============================================================')

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'Não é BISSEXTO!')
print('=============================================================')
