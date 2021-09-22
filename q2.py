valor = int(input("Entre com o valor: "))
contador = 0

for n in range(1,valor + 1):
  if(n%2 == 0):
    contador += n

print(contador)