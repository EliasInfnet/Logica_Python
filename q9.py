from bs4 import BeautifulSoup

import requests

html = requests.get("https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html").content

soup = BeautifulSoup(html, 'html.parser')



lista_estados = []

linha = soup.findAll("div", class_ = "linha")
dic = soup.findAll("div", class_ = "celula")

for i in linha:
    children = i.findChildren("div")
    estado = []
    for x in children:
        estado.append(x.string)
    lista_estados.append(estado)    

print("Lista de estados")

print('------------------')

for row in lista_estados:
    print(row)

print('==================')

sigla = str(input("Entre com uma sigla de estado do centro oeste: "))

print('Dados do estado que você escolheu :')
print('')

if(lista_estados[0][0] == sigla):
  print(lista_estados[0])
if(lista_estados[1][0] == sigla):
  print(lista_estados[1])
if(lista_estados[2][0] == sigla):
  print(lista_estados[2])   
if(lista_estados[3][0] == sigla):
  print(lista_estados[3])

print('------------------')