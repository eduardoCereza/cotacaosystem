#importando bibliotecas
import requests

url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
app = requests.get(url)