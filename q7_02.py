import csv
import requests

CSV_URL = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv'

with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    my_list.pop(0)

def questao_2():
  listaNomePaises = []
  for item in my_list:
    if not item[4] in listaNomePaises:
      listaNomePaises.append(item[4])

  listaContadorPais = []

  for item in listaNomePaises:
    listaContadorPais.append([item,0])  

  print(listaContadorPais)

  for item in listaContadorPais:
    listaMedalhasPais = []
    for i in my_list:
      if( i[4] == item[0] ):
        item[1] += 1
        listaMedalhasPais.append([i[4],i[0],i[1],i[2],i[6]])  
    print(item[0] + " ganhou " + str(item[1]) + " medalhas")  
    print("-------------------------")  
    for row in listaMedalhasPais:
      print(row)
    print("-------------------------")  

questao_2()