from bs4 import BeautifulSoup

import requests

html = requests.get("https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html").content

soup = BeautifulSoup(html, 'html.parser')

sigla = str(input("Entre com uma sigla de estado do centro oeste: "))

lista_estados = []

linha = soup.findAll("div", class_ = "linha")
dic = soup.findAll("div", class_ = "celula")

for i in linha:
    children = i.findChildren("div")
    estado = []
    for x in children:
        estado.append(x.string)
    lista_estados.append(estado)    

print(sigla)
if(lista_estados[0][0] == sigla):
    print(lista_estados[0])
    if(lista_estados[1][1] == sigla):
        print(lista_estados[1])
        if(lista_estados[2][2] == sigla):
            print(lista_estados[2])   
            if(lista_estados[3][3] == sigla):
                print(lista_estados[3])