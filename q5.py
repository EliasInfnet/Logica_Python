tupla = (1,41,3,86,5,34,7,8)
listaImpar = []
listaPosicaoPar = []
for x in tupla:
    if x%2 !=0:
      listaImpar.append(x)
    if tupla.index(x)%2 == 1:
      listaPosicaoPar.append(x)
  
print(listaImpar)
print(listaPosicaoPar)