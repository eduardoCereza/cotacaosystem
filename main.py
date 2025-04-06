#importando bibliotecas
import requests

#define a URL como a API
url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
#pega(get) a API para podermos manipula-la e achar os valores
app = requests.get(url)

#importa o JSON
app = app.json()
#atribui a cada cotacao o seu valor, podendo ser achada no arquivo JSON
cotacao_dolar = input(app["USDBRL"]['bid'])
cotacao_euro = input(app["EURBRL"]['bid'])
cotacao_bitcoin = input(app["BTCBRL"]['bid'])

#sistema de opcao
print("Digite o número que corresponde ao conversor: ")
print('1')
print('2')
print('3')

#pegar valor do usuario
valor = int(input("Digite o valor: "))
#logica em loop condicional
