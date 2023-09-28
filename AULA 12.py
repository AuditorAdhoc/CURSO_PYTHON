
## Exercícios Web Scraping ##

#? Para os próximos exercícios, utilize html.parser quando estiver analisando códigos HTML, ou lxml para códigos XML.

#  1) Faça um programa que pegue os próximos cursos e as respectivas datas em https://letscodeacademy.com/.

import requests
from bs4 import BeautifulSoup

link = requests.get('https://letscodeacademy.com/')
resposta = link.text
soup = BeautifulSoup(resposta, 'html.parser')
for curso in soup.find_all("a", class_='card__curso__text'):
    nome = curso.text

    print(f"Curso: {nome}")


#  2) Faça um programa que busca o valor atual de um ativo da bolsa. Para isso, use a url https://finance.yahoo.com/ (procure por um ativo em particular, como PETR4.SA, VALE, ou BTC, e veja as semelhanças e diferenças de cada um no link e no código).

import requests
from bs4 import BeautifulSoup

ativo = 'NASDAQ'

link = requests.get(f'https://finance.yahoo.com/quote/{ativo}')
resposta = link.text
soup = BeautifulSoup(resposta, 'html.parser')
valor = soup.find('span', class_=["Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)"])
print(f'\nValor do ativo {ativo}: {valor}\n')


#  3) Use o link: http://servicos.cptec.inpe.br/XML/cidade/codigo/previsao.xml para obter a previsão do tempo para as seguintes cidades:
# a. São Paulo, código 244;
# b. Rio de Janeiro, código 241;
# c. Belo Horizonte, código 222; e
# d. Barueri, código 797

import requests
from bs4 import BeautifulSoup

codigos_cidades = [244, 241, 222, 797]

for codigo in codigos_cidades:
    url = f'http://servicos.cptec.inpe.br/XML/cidade/{codigo}/previsao.xml'

    try:
        result = requests.get(url)
    except Exception as err:
        print('Something went wrong', err)
    else:
        response = result.text
        soup = BeautifulSoup(response, 'lxml')
        cidade = soup.nome.text
        print(cidade)
        for previsao in soup.find_all("previsao"):
            dia = previsao.dia.text
            tempo = previsao.tempo.text
            maxima = previsao.maxima.text
            minima = previsao.minima.text
            iuv = previsao.iuv.text
            print(f'\t-Dia: {dia}\tTempo: {tempo}\tMáxima: {maxima}\tMínima: {minima}\tIUV: {iuv}')


#  4) Faça um programa que busca os valores de um produto no mercado livre.
#     Salve o nome e o respectivo valor desses produtos em um arquivo csv.
#     Seu programa deve imprimir o produto mais caro, o mais barato e a média de preços 
#     (procure por um produto em particular e veja como se comporta o link e os objetos 
#     web que contém as informações de nome e preço do produto).


import csv
import requests as r
from bs4 import BeautifulSoup

produto = 'celular-lg-k12-prime'
try:
    result = r.get(f'https://celulares.mercadolivre.com.br/{produto}')
except Exception as err:
    print('Something went wrong', err)
else:
    response = result.text
    soup = BeautifulSoup(response, 'html.parser')


    tabela_produtos = []
    lista_precos = []
    for produto in soup.find_all('div', class_='item__info'):
        nome = produto.a.text
        nome = nome.replace('  ', '')  # Remove espaços excessivos

        #  Parte do preço que corresponde à parte inteira
        preco_inteiro = produto.find('span', class_='price__fraction').text
        preco_inteiro = int(preco_inteiro.replace('.', ''))

        #  Parte do preço que corresponde aos centavos
        preco_decimal = produto.find('span', class_='price__decimals')
        if preco_decimal: # Verifica se o produto tem centavos no preço
            preco_decimal  = preco_decimal.text
        else:
            preco_decimal = 0

        #  Preço com a parte inteira e decimal juntos
        preco = f'{preco_inteiro}.{preco_decimal}'
        preco = float(preco)

        # Adciona o produto/preço na tabela de produtos
        tabela_produtos.append([nome, preco])

        # Adciona o preço na lista de preços
        lista_precos.append(preco)

    indice_menor_valor = lista_precos.index(min(lista_precos))
    menor_valor = tabela_produtos[indice_menor_valor]
    print('Produto mais em conta: {}\tValor: {:.2f}'.format(menor_valor[0], menor_valor[1]))

    indice_maior_valor = lista_precos.index(max(lista_precos))
    maior_valor = tabela_produtos[indice_maior_valor]
    print('Produto mais caro: {}\tValor: {:.2f}'.format(maior_valor[0], maior_valor[1]))

    media = sum(lista_precos)/len(lista_precos)
    print('Média dos preços: {:.2f}'.format(media))
    
    # Gera o arquivo csv com a cotação dos produtos
    with open('cotacao.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(tabela_produtos)
