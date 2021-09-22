def potencia(a,b):
  valor = a
  for i in range(1,b):
    valor = valor * a
  return valor

valor1 = int(input("Entre com o primeiro valor (A): "))
valor2 = int(input("Entre com o segundo valor (B): "))

print(potencia(valor1,valor2))