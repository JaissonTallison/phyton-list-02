# Classificação de notas Receba uma nota de 0 a 10 e exiba:
# Aprovado (nota ≥ 7)
# Recuperação (nota entre 5 e 6.9)
# Reprovado (nota < 5)
print('=============================================================')

nota = float(input('Qual foi sua Nota? '))

print('=============================================================')

if (nota >= 7):
    print('Aprovado!')
elif (nota >= 5 and nota <= 6.9):
    print('Recuperação!')
else:
    print('Reprovado!')

print('=============================================================')
