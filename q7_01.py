import csv
import requests

CSV_URL = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv'

with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    my_list.pop(0)

def questao_1():
  listaAux = [x for x in my_list if x[2] == 'Curling' or x[2] == 'Skating' or x[2] == 'Skiing' or x[2] == 'Ice Hockey']  
 
  lista = [x for x in listaAux if int(x[0]) > 2001]

  contadores = [['Suecia',0],['Dinamarca',0],['Noruega',0]]

  for item in lista:
    if(item[4]=='SWE' and item[7] == 'Gold'):
      contadores[0][1] += 1
    elif(item[4]=='DEN' and item[7] == 'Gold'):
      contadores[1][1] += 1
    elif(item[4]=='NOR' and item[7] == 'Gold'):
      contadores[2][1] += 1

  listaResultado = sorted(contadores, key=lambda item: item[1],reverse=True)
  print( '--------------------------' )
  print("O maior medalista de ouro foi " + listaResultado[0][0] + " com " + str(listaResultado[0][1]) + " medalhas.")
  print( '--------------------------' )

questao_1()

