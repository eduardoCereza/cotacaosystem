#importando bibliotecas
import requests

url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
app = requests.get(url)

app = app.json()
cotacao_dolar = input(app["USDBRL"]['bid'])
cotacao_euro = input(app["EURBRL"]['bid'])
cotacao_bitcoin = input(app["BTCBRL"]['bid'])