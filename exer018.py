# Verificar se um número é primo
# Receba um número inteiro e verifique se ele é primo (divisível apenas por 1 e por ele mesmo).

numero = int(input("Digite um número inteiro: "))

if numero <= 1:
  print(numero, "não é um número primo.")
else:
  eh_primo = True
  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      eh_primo = False
      break
  if eh_primo:
    print(numero, "é um número primo.")
  else:
    print(numero, "não é um número primo.")