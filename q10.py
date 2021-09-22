import requests
from bs4 import BeautifulSoup

url = "http://brasil.pyladies.com/about/"

# Usando requests
html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

lista = soup.find_all("p",attrs={"class": "about-text"})

lista_palavras_unicas = []
lista_palavras_count = []
lista_palavras_totais = []
contador_palavras_totais = 0

for frase in lista:
  lista_aux_palavra = frase.text.split()
  for palavra in lista_aux_palavra:
    lista_palavras_totais.append(palavra)
    if not palavra in lista_palavras_unicas:
      lista_palavras_unicas.append(palavra)
      lista_palavras_count.append([palavra,0])

for dic in lista_palavras_count:
  dic[1] = lista_palavras_totais.count(dic[0])

lista_palavras_totais.append("palavra")
lista_palavras_totais.append("palavra")

def questao_01():

  print('==============================')  
  print(' ')

  lista_palavras_uma_vez = []

  for palavra_count in lista_palavras_count:
    if(palavra_count[1] == 1):
      lista_palavras_uma_vez.append(palavra_count[0])


  print("Total de palavras no texto : " + str(len(lista_palavras_totais)) + " de palavras")
  print("Total de palavras únicas no texto: " + str(len(lista_palavras_count)) + " de palavras")
  print("Total de palavras que apareceram uma vez no texto: " + str(len(lista_palavras_uma_vez)))
  print(' ')
  print(lista_palavras_uma_vez)
  print(' ')
  print('==============================')


questao_01()

def questao_02():

  print('')
  print('A palavra "ladies" apareceu ' + str(lista_palavras_totais.count('ladies')) + ' vezes.')
  print(' ')
  print('==============================')
  
questao_02()