
### Exercícios - APIs ###


## http://numbersapi.com/ - Para os exercícios 1 ao 3

#1. Usando a Numbers API, faça um programa que sorteie um número de 1 a 1000 e imprima uma trivia sobre esse número.

import requests
from random import randint

site = "http://numbersapi.com/{}/{}"
num_sorteio = randint(1,1000)
tipo = 'trivia'
link = site.format(num_sorteio, tipo)
solicitacao = requests.get(link)
print()
print(solicitacao.text)
print()

# 2. Usando a Numbers API, faça um programa que sorteie um número de 1 a 1000 e imprima um fato matemático (tipo *math*) sobre esse número.

import requests
from random import randint

site = "http://numbersapi.com/{}/{}"
num_sorteio = randint(1,1000)
tipo = 'math'
link = site.format(num_sorteio, tipo)
solicitacao = requests.get(link)
print()
print(solicitacao.text)
print()

# 3. Usando a numbers API, faça um programa que receba a data (no formato mes/dia, como string) do seu aniversário e imprima um fato que 
# ocorreu nesse dia.

import requests
from random import randint

site = "http://numbersapi.com/{}/{}"
tipo = 'date'
data = input("\nDigite a data do seu aniversário (mm/dd)")
link = site.format(data, tipo)
solicitacao = requests.get(link)
print()
print(solicitacao.text)
print()


## https://www.exchangerate-api.com/ ## - Para os exercícios 4 ao 8

# 4. Usando a Exchange Rate API, faça um programa que imprima a taxa de conversão de reais para dólares americanos em tempo real. 
# Seu programa deve imprimir também a data da última atualização da API. 

import requests

site = "https://v6.exchangerate-api.com/v6/39807538a80ad93509c9fcaf/latest/{}"
moeda = 'BRL'
link = site.format(moeda)
solicitacao = requests.get(link)
data = solicitacao.json()
taxa = data['conversion_rates']
print()
print("Taxa de conversão de reais para dólares =", taxa["USD"])
print("Data da última atualização = ", data['time_last_update_utc'])
print()


# 5. Usando a Exchange Rate API, faça um programa que receba um valor em reais e o converta para dólares americanos. Seu programa deve 
# imprimir também a data da última atualização da taxa. 

import requests

site = "https://v6.exchangerate-api.com/v6/39807538a80ad93509c9fcaf/latest/{}"
moeda = 'BRL'
link = site.format(moeda)
solicitacao = requests.get(link)
data = solicitacao.json()
taxa = data['conversion_rates']

valor = float(input("\nDigite um valor para ser convertido em dólar: "))
conversao = taxa['USD']*valor

print("\nR${:.2f} = US${:.2f} na data de {}.".format(valor, conversao, data['time_last_update_utc']))
print()


# 6.  Usando a Exchange Rate API, faça um programa que receba a sigla de duas moedas, ORIGEM e DESTINO, e um valor X. Seu programa deve 
# converter o valor X da moeda ORIGEM para a moeda DESTINO. Obs: A lista de todas as siglas de moedas pode ser encontrada em
# https://www.exchangerate-api.com/docs/supported-currencies

import requests

site = "https://v6.exchangerate-api.com/v6/39807538a80ad93509c9fcaf/latest/{}"

print("\nEXEMPLO DE MOEDAS: USD - AUD - BRL - CAD")
origem = input('Digite a moeda de origem: ')
destino = input("Digite a moeda de destino: ")

link = site.format(origem)
solicitacao = requests.get(link)
data = solicitacao.json()
taxa = data['conversion_rates']

valor = float(input("Digite um valor para ser convertido: "))
conversao = taxa[destino]*valor
print()
print("{} {:.2f} = {} {:.2f} na data de {}.".format(origem, valor, destino, conversao, data['time_last_update_utc']))
print()


# 7. Refaça o exercício 6 orientado a funções. Isto é, faça uma função que recebe duas moedas, ORIGEM e DESTINO, e um valor X. 
# Sua função deve retornar o valor X convertido da moeda ORIGEM para a moeda DESTINO.

import requests

def cambio(origem, destino, valor):
    site = "https://v6.exchangerate-api.com/v6/39807538a80ad93509c9fcaf/latest/{}"
    link = site.format(origem)
    solicitacao = requests.get(link)
    data = solicitacao.json()
    taxa = data['conversion_rates']
    conversao = taxa[destino]*valor
    return conversao

#?Chama a função:
valor = float(input("\nDigite um valor para ser convertido: "))
print("\nEXEMPLO DE MOEDAS: USD - AUD - BRL - CAD")
origem = input('Digite a moeda de origem: ')
destino = input("Digite a moeda de destino: ")
print()
print("{} {:.2f} = {} {:.2f}.".format(origem, cambio(origem, destino, valor), destino, valor))
print()

#! Continua aqui.
# 8. Refaça o exercício 6 orientado a objeto. Você deve construir uma classe Moeda. Essa classe deve ter como atributo a sigla da moeda e 
# o dicionário de conversão. Faça um método para requisitar os dados. Faça também um método que receba uma outra moeda e um valor X, 
# e retorne o valor X convertido para essa moeda recebida.

import requests

class Moeda:
    site = "https://v6.exchangerate-api.com/v6/39807538a80ad93509c9fcaf/latest/{}"
    def __init__(self, sigla):
        self.sigla = sigla
        self.taxas = None
        self.ultima_data = None
    def pega_dados(self):
        # método que requisita os dados da Exchange Rate API
        link = self.site.format(self.sigla)
        resposta = requests.get(link)
        dicio_dados = resposta.json()
        self.ultima_data = dicio_dados.get('time_last_updated', None) # em timestamp
        self.taxas = dicio_dados.get('conversion_rates', None)
    def converte_valor(self, other, valor):
        self.pega_dados()
        taxa = self.taxas.get(other.sigla, None)
        if taxa:
            valor_convertido = valor * taxa
            return valor_convertido


# 9. Usando a Open Weather API, faça uma função que receba um nome de uma cidade e imprima a temperatura máxima, a mínima, a umidade, a 
# descrição do tempo e o horário da última atualização.

# http://api.openweathermap.org/data/2.5/weather?q={NOME_DA_CIDADE}&appid={CHAVE_DE_ACESSO}&units=metric 

import requests
from datetime import datetime as dt

key = "cb926da04c58d12e68807544e9a35f6c"
link_base = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
cidade = input('Digite uma cidade: ')
link = link_base.format(cidade, key)
resposta = requests.get(link)
dicionario_resposta = resposta.json()
print(dicionario_resposta)

temp_min = dicionario_resposta.get('main',{}).get('temp_min', None)
temp_max = dicionario_resposta.get('main',{}).get('temp_max', None)
umidade = dicionario_resposta.get('main',{}).get('humidity', None)
tempo = dicionario_resposta.get('weather', {})[0].get('description', None)
ultima_atualizacao = dt.fromtimestamp(dicionario_resposta.get('dt'))
print(temp_min, temp_max, umidade, tempo, ultima_atualizacao)


# 10. Refaça o exercício 9 utilizando orientação a objetos. Isto é, faça uma classe Cidade cujos atributos são: nome, temp_min, temp_max,
# umidade, descrição do tempo e última atualização. Construa métodos para pegar os dados e, com o método mágico `__repr__` para exibir os 
# dados.

import requests
from datetime import datetime as dt
class Cidade:
    link_base = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
    key = "cb926da04c58d12e68807544e9a35f6c"
    def __init__(self, nome):
        self.nome = nome
        self.temp_min = None
        self.temp_max = None
        self.umidade = None
        self.tempo = None
        self.ultima_atualizacao = None
    def pegar_dados(self):
        link = self.link_base.format(self.nome,self.key)
        resposta = requests.get(link)
        dicionario_resposta = resposta.json()
        self.temp_min = dicionario_resposta.get('main',{}).get('temp_min', None)
        self.temp_max = dicionario_resposta.get('main',{}).get('temp_max', None)
        self.umidade = dicionario_resposta.get('main',{}).get('humidity', None)
        self.tempo = dicionario_resposta.get('weather', {})[0].get('description', None)
        self.ultima_atualizacao = dt.fromtimestamp(dicionario_resposta.get('dt'))
    def __repr__(self):
        self.pegar_dados()
        texto = "\n====Previsao do Tempo para {}===\n".format(self.nome)+\
        '\tTemperatura Máx: {}\n\tTemperatura_min: {}\n'.format(self.temp_max, self.temp_min) + \
        '\tUmidade: {}\n'.format(self.umidade) + \
        'Tempo: {}\n'.format(self.tempo)
        'Última atualização: {}'.format(self.ultima_atualizacao)
        return texto

#Exemplo de uso

cidade = input('Digite uma cidade: ')
previsao = Cidade(cidade)

print(previsao)




######### DESAFIOS #########

# Para os desafios 1 ao 3 vamos utilizar uma API do Star Wars, chamada de SWAPI. Entre no site deles para se informar sobre as respostas e requisições: https://swapi.co/
# 1.  Faça um programa que imprima o nome e o ano de nascimento dos 50 primeiros personagens listados no site.
# 2.  Agora implemente o seu programa, adicionando o nome do planeta de origem de cada personagem.
# Obs: você precisará fazer uma nova requisição para o planeta, caso ele não seja desconhecido.

import requests

enderecoBase = 'https://swapi.co/api/people/'
contador = 1

while contador <= 50:
    endereco = enderecoBase + str(contador)
    resposta = requests.get(endereco)
    if resposta.status_code == 200:
        personagem = resposta.json()
        nome = personagem['name']
        data = personagem['birth_year']

        # exercício 2
        enderecoPlaneta = personagem['homeworld']
        respostaPlaneta = requests.get(enderecoPlaneta)
        if respostaPlaneta.status_code == 200:
            planeta = respostaPlaneta.json()
            nomePlaneta = planeta['name']
        else:
            nomePlaneta = 'planeta desconhecido'

        print(nome, '-', data, '-', nomePlaneta)
    else:
        print('<ERRO> Personagem', contador, 'não encontrado!')

    contador = contador + 1

 
# 3.  Faça um programa que imprima o nome dos personagens que apareceram no filme 4: "The Phantom Menace".

import requests

resposta = requests.get('https://swapi.co/api/films/4')

if resposta.status_code == 200:
    filme = resposta.json()
    personagens = filme['characters']

    for endereco in personagens:
        respostaPersonagem = requests.get(endereco)
        if respostaPersonagem.status_code == 200:
            personagem = respostaPersonagem.json()
            print(personagem['name'])


# Para os desafios 4 e 5,  vamos utilizar uma API do Governo Federal para analisar os gastos por meio de cartão de pagamento. O link da API é:
# “http://www.transparencia.gov.br/api-de-dados/cartoes?mesExtratoInicio={}%2F{}&mesExtratoFim={}%2F{}&pagina={}”.format(mes_ini, ano_ini, mes_fim, ano_fim, pagina)
# onde os dados retornados correspondem a um intervalo definido por um mês e ano inicial (mes_ini e ano_ini) e um mês e ano final (mes_fim, ano_fim) e são apresentados 14 dados por página, com a primeira página sendo definida por pagina = 1.
# 4.  Faça uma requisição da API para obter os dados entre 06/2018 e 07/2018 e responda:
# a.  Quantos pagamentos foram realizados por meio de cartão de pagamento nesse intervalo?
# Obs: lembre-se de olhar todas as páginas possíveis. Você pode usar um loop infinito para isso, e sair do loop quando a requisição não retornar 200;
# b.  Qual foi o maior valor de transação?
# c.  Qual o nome do portador do cartão responsável por esse gasto?

import requests

mes_ini = '06'
ano_ini = '2018'
mes_fim = '07'
ano_fim = '2018'
pagina = 1

enderecoBase = 'http://www.transparencia.gov.br/api-de-dados/cartoes?mesExtratoInicio={}%2F{}&mesExtratoFim={}%2F{}&pagina={}'

contagem = 0

maior = 0
pessoa = ''

while True:
    resposta = requests.get(enderecoBase.format(mes_ini, ano_ini, mes_fim, ano_fim, pagina))

    if resposta.status_code == 200:
        transacoes = resposta.json()
        # item a
        contagem = contagem + len(transacoes)

        # item b
        for transacao in transacoes:
            valor = transacao['valorTransacao']
            # tirando os pontos de casa de milhar: 1.000,00 vira 1000,00
            valor = valor.replace('.', '')
            # trocando a vírgula por ponto decimal: 1000,00 vira 1000.00
            valor = valor.replace(',','.')
            valor = float(valor)
            if valor > maior:
                # item c
                pessoa = transacao['portador']['nome']
                maior = valor

        pagina = pagina + 1
        
    else:
        print('Última página:', pagina)
        break

    # O programa demora MUITO para executar (são mais de 3 mil páginas).
    # Descomentar o bloco abaixo fará rodar um número baixo de páginas só
    # para verificar se funciona.
    '''
    if pagina > 3:
        break
    '''
    
print('Maior gasto:', maior)
print('Portador:', pessoa)
print('Total de transações:', contagem)



# 5.  Imprima uma tabela com nome do portador e valor da transação para todos os pagamentos por meio de cartão realizados entre 11/2017 e 12/2017.

import requests

mes_ini = '11'
ano_ini = '2017'
mes_fim = '12'
ano_fim = '2017'
pagina = 1

enderecoBase = 'http://www.transparencia.gov.br/api-de-dados/cartoes?mesExtratoInicio={}%2F{}&mesExtratoFim={}%2F{}&pagina={}'

while True:
    resposta = requests.get(enderecoBase.format(mes_ini, ano_ini, mes_fim, ano_fim, pagina))

    if resposta.status_code == 200:
        transacoes = resposta.json()

        for transacao in transacoes:
            valor = transacao['valorTransacao']
            pessoa = transacao['portador']['nome']
            print(pessoa + '\t' + valor)
            
        pagina = pagina + 1
    else:
        print('Última página:', pagina)
        break
    

    # O programa demora MUITO para executar (são mais de 3 mil páginas).
    # Descomentar o bloco abaixo fará rodar um número baixo de páginas só
    # para verificar se funciona.
    '''
    if pagina > 3:
        break
    '''
    

    
