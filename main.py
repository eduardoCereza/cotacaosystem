#importando bibliotecas
import requests
#pegar valor do usuario
valor = float(input("Digite o valor: "))

#pega(get) a API para podermos manipula-la e achar os valores
url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
app = requests.get(url)

#importa o JSON
app = app.json()
#atribui a cada cotacao o seu valor, podendo ser achada no arquivo JSON
cotacao_dolar = float((app["USDBRL"]['bid']))
cotacao_euro = float((app["EURBRL"]['bid']))
cotacao_bitcoin = float((app["BTCBRL"]['bid']))

#sistema de opcao
print('1. USD')
print('2. EUR')
print('3. BTC')
print("4. Sair")
opcao = int(input("Digite o número que corresponde ao conversor: "))



#logica em loop condicional
while True:
    if opcao == 1:
        resultado = valor * cotacao_dolar
        print(resultado)
        opcao = 4
    if opcao == 2:
        resultado = valor * cotacao_euro
        print(resultado)
        opcao = 4
    if opcao == 3:
        resultado = valor * cotacao_bitcoin
        print(resultado)
        opcao = 4
    if opcao == 4:
        break
