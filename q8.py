import csv
import requests

CSV_URL = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv'

with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    my_list.pop(0)

def verifica_item_dentro_lista(item, lista):
  verificar = False
  index = 0
  for i in lista:
    if item in i:
      verificar = True
      index = lista.index(i)
  return [verificar,index]

# 0 : Nome da empresa
# 1 : Publicações de Action
# 2 : Publicações de Shooter
# 3 : Publicações de Platform
# 4 : Total de publicações
# 5 : Total de vendas
# 6 : Quantas publicações depois de 2011 Action
# 7 : Quantas publicações depois de 2011 Shooter
# 8 : Quantas publicações depois de 2011 Platform
# 9 :  Quantas vendas depois de 2011  Action
# 10 : Quantas vendas depois de 2011  Shooter
# 11 : Quantas vendas depois de 2011  Platform

def retorna_publishers():
  listaPublisher = []
  for item in my_list:
    if not [item[4],0,0,0,0,0,0,0,0,0,0,0] in listaPublisher:
      listaPublisher.append([item[4],0,0,0,0,0,0,0,0,0,0,0])
  return sorted(listaPublisher)

def contador_publishers():
  lista = retorna_publishers()
  for item in my_list:
    if verifica_item_dentro_lista(item[4], lista)[0]:
      if item[3] == "Action":
        lista[verifica_item_dentro_lista(item[4], lista)[1]][1] += 1
        lista[verifica_item_dentro_lista(item[4], lista)[1]][4] += 1
        lista[verifica_item_dentro_lista(item[4], lista)[1]][5] += round(float(item[9]))
        if item[2] >= '2011':
          lista[verifica_item_dentro_lista(item[4], lista)[1]][6] += 1
          lista[verifica_item_dentro_lista(item[4], lista)[1]][9] += round(float(item[9]))
      if item[3] == "Shooter":
        lista[verifica_item_dentro_lista(item[4], lista)[1]][2] += 1
        lista[verifica_item_dentro_lista(item[4], lista)[1]][4] += 1
        lista[verifica_item_dentro_lista(item[4], lista)[1]][5] += round(float(item[9]))
        if item[2] >= '2011':
          lista[verifica_item_dentro_lista(item[4], lista)[1]][7] += 1
          lista[verifica_item_dentro_lista(item[4], lista)[1]][10] += round(float(item[9]))
      if item[3] == "Platform":
        lista[verifica_item_dentro_lista(item[4], lista)[1]][3] += 1  
        lista[verifica_item_dentro_lista(item[4], lista)[1]][4] += 1
        lista[verifica_item_dentro_lista(item[4], lista)[1]][5] += round(float(item[9]))
        if item[2] >= '2011':
          lista[verifica_item_dentro_lista(item[4], lista)[1]][8] += 1
          lista[verifica_item_dentro_lista(item[4], lista)[1]][11] += round(float(item[9]))    
  return lista

print('=================================')

def questao_1():
  print("As três marcas que mais publicaram jogos dos três generos combinados foram: ")
  for i in range(0,3):
    marca = sorted(contador_publishers(), key=lambda x: x[4],reverse=True)[i]
    print(marca[0] + ', com ' + str(marca[4]) + ' jogos publicados')

questao_1()

print('=================================')

def questao_2():
  print("As três marcas que mais venderam jogos dos três generos combinados foram: ")
  for i in range(0,3):
    marca = sorted(contador_publishers(), key=lambda x: x[5],reverse=True)[i]
    print(marca[0] + ', com ' + str(marca[5]) + ' de pontuação de vendas')

questao_2()

print('=================================')

def questao_3():
  marcaAction = sorted(contador_publishers(), key=lambda x: x[6],reverse=True)[0]
  print("A marca que mais publicou jogos Action nos últimos dez anos foi : ") 
  print(marcaAction[0] + ' com ' + str(marcaAction[6]) + ' publicações Action no total')
  print('---------------------------')

  marcaShooter = sorted(contador_publishers(), key=lambda x: x[7],reverse=True)[0]
  print("A marca que mais publicou jogos Shooter nos últimos dez anos foi : ") 
  print(marcaShooter[0] + ' com ' + str(marcaShooter[7]) + ' publicações Shooter no total')
  print('---------------------------')

  marcaPlatform = sorted(contador_publishers(), key=lambda x: x[8],reverse=True)[0]
  print("A marca que mais publicou jogos Platform nos últimos dez anos foi : ") 
  print(marcaPlatform[0] + ' com ' + str(marcaPlatform[8]) + ' publicações Platform no total')
  

questao_3()

print("=================================")

def questao_4():
  marcaAction = sorted(contador_publishers(), key=lambda x: x[9],reverse=True)[0]
  print("A marca que mais vendeu jogos Action nos últimos dez anos foi : ") 
  print(marcaAction[0] + ' com ' + str(marcaAction[9]) + ' de pontuação de vendas Action')
  print('---------------------------')

  marcaShooter = sorted(contador_publishers(), key=lambda x: x[10],reverse=True)[0]
  print("A marca que mais vendeu jogos Shooter nos últimos dez anos foi : ") 
  print(marcaShooter[0] + ' com ' + str(marcaShooter[10]) + ' de pontuação de vendas Shooter')
  print('---------------------------')

  marcaPlatform = sorted(contador_publishers(), key=lambda x: x[11],reverse=True)[0]
  print("A marca que mais vendeu jogos Platform nos últimos dez anos foi : ") 
  print(marcaPlatform[0] + ' com ' + str(marcaPlatform[11]) + ' de pontuação de vendas Platform')

questao_4()

print("=================================")