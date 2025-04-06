#importando bibliotecas
import requests

#define a URL como a API
url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
#pega(get) a API para podermos manipula-la e achar os valores
app = requests.get(url)

#importa o JSON
app = app.json()
#atribui a cada cotacao o seu valor, podendo ser achada no arquivo JSON
cotacao_dolar = float(input(app["USDBRL"]['bid']))
cotacao_euro = float(input(app["EURBRL"]['bid']))
cotacao_bitcoin = float(input(app["BTCBRL"]['bid']))

#sistema de opcao
print("Digite o número que corresponde ao conversor: ")
print('1. USD')
print('2. EUR')
print('3. BTC')

#pegar valor do usuario
valor = float(input("Digite o valor: "))
#logica em loop condicional
if 1:
    resltado = valor * cotacao_dolar
if 2:
    resultado = valor * cotacao_euro
if 3 :
    resultado = valor * cotacao_bitcoin

print(resultado)
