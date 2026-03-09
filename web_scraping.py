from bs4 import BeautifulSoup
import requests
import re

link = 'https://coinmarketcap.com/'
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, 'html.parser')

tbody = site.find('tbody')
linhas = site.find_all('tr')
linhas.remove(linhas[0])

moedas = {}

for linha in linhas:
  try:
    nome = linha.find(class_="coin-item-name").text
    codigo = linha.find(class_="coin-item-symbol").text

    valores = linha.find_all(string=re.compile('\$'))
    preco = valores[0]
    market_cap = valores[2]
    volume = valores[3]

    percentuais = linha.find_all(string=re.compile('%'))

    for i, percentual in enumerate(percentuais):
      if 'fDGzbr' in percentual.parent['class']:
        percentuais[i] = '-' + percentual

    var_1h = percentuais[0]
    var_24h = percentuais[1]
    var_7d = percentuais[2]

    dic = {'Nome': nome, 'Código': codigo, 'Preço':preco, 'Market Cap': market_cap, 'Volume':volume, '1h %':var_1h, '24h %': var_24h, '7d %':var_7d}
    moedas[nome] = dic

  except AttributeError:
    break

print(moedas)