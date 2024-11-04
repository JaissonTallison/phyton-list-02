# . Calcular a média de N númerosPeça ao usuário para informar quantos números deseja inserir e, em seguida, receba esses números e exiba a média deles.

n = int(input("Quantos números você deseja inserir? "))


soma = 0
contador = 0


for i in range(n):
    numero = float(input("Digite o número {}: ".format(i+1)))
    soma += numero
    contador += 1


media = soma / contador


print("A média dos números é:", media)