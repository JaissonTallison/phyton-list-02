# Validação de senha simples O programa deve pedir uma senha e comparar com a senha "1234".
# Se a senha estiver correta, exiba "Acesso permitido", senão exiba "Senha incorreta"
print('=============================================================')
senha = int(input('Digite uma SENHA: '))
senhaCorreta = 1234
print('=============================================================')

if (senha == senhaCorreta):
    print('Senha Correta! Acesso Permitido!')
else:
    print('Senha Incorreta! Acesso Negado!')
print('=============================================================')
