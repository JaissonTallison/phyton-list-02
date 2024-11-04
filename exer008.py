# Cálculo de desconto em compras.
# Peça o valor de uma compra. Se o valor for maior que 100 reais, aplique um desconto de 10% e exiba o valor final.

print('=============================================================')
valorCompra = int(input('Qual O valor da sua compra? '))

print('=============================================================')
valorFinal = valorCompra - (valorCompra * (10/100))

if (valorCompra > 100):
    print(f'O valor Final com desconto é: {valorFinal}')
else:
    print(f'O valor Final é: {valorCompra}')
print('=============================================================')
