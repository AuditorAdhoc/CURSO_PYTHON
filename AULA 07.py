
## ARQUIVO CSV ##

# 1. Para os exercícios 1 ao 3, você precisará do arquivo: alunos.csv. Clique aqui para baixá-lo (ao salvar, renomeie o arquivo).
# Faça um programa que imprima as linhas do arquivo alunos.csv.

import csv

arquivo = open('alunos.csv', 'r')
print('\nImprimindo as linhas do arquivo:\n')
planilha = arquivo.readlines()

for linha in planilha:
    print(linha)
print()
arquivo.close()

#> Outra solução:

import csv

arquivo = open('alunos.csv', 'r')
print('\nImprimindo as linhas do arquivo:\n')
planilha = csv.reader(arquivo, delimiter=',', lineterminator='\n')

for linha in planilha:
    print('{:9}{:18}{:13}{:10}{:10}{:10}{:10}'.format(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6]))
arquivo.close()

#> Outra solução:

with open("alunos.csv", encoding="utf-8") as file:
    dados = file.read()

linhas = dados.split("\n")

for linha in linhas:
    print(linha)


# 2. Faça um programa que imprima as linhas do arquivo alunos.csv como listas.

import csv

arquivo = open('alunos.csv', 'r')
print('\nImprimindo as linhas da tabela como listas:\n')
planilha = csv.reader(arquivo, delimiter=',', lineterminator='\n')

for linha in planilha:
    print(linha, "\n")
print()
arquivo.close()


#> Outra solução:

import csv

arquivo = open('alunos.csv', 'r')
print('\nImprimindo as linhas da tabela como listas:\n')
planilha = csv.reader(arquivo, delimiter=',', lineterminator='\n')

print(list(planilha))
print()
arquivo.close()

#> Outra solução:

with open("alunos.csv", encoding="utf-8") as file:
    dados = file.read()

linhas = dados.split("\n")

for linha in linhas:
    lista = linha.split(",")
    print(lista)


# 3. Faça um programa que imprima os elementos da coluna ‘Nome’ do arquivo alunos.csv.

import csv

arquivo = open('alunos.csv', 'r')
print("\nImprimindo os elementos da coluna Nome:\n")
planilha = csv.DictReader(arquivo, delimiter=',', lineterminator='\n')

for coluna in planilha:
    print(coluna['Nome'], "\n")

arquivo.close()

#> Outra solução:

with open("alunos.csv", encoding="utf-8") as file:
    dados = file.read()

linhas = dados.split("\n")

for linha in linhas[1:]:
    aluno = linha.split(",")
    print(aluno[1])
print()


# 4. Faça um programa que copie os dados do arquivo alunos.csv para um arquivo chamado alunos2.csv.

import csv

arquivo = open('alunos.csv', 'r')
planilha = csv.reader(arquivo, delimiter=',', lineterminator='\n')

arquivo2 = open('alunos2.csv', 'w')
planilha2 = csv.writer(arquivo2, delimiter=',', lineterminator='\n')

arquivo.close()


#> Outra solução:

with open("alunos.csv", "r") as file:
    dados = file.read()

with open("alunos2.csv", "w") as file:
    file.write(dados)


# 5. Faça um programa que imprima o nome e a média de cada um dos alunos do arquivo alunos.csv.

with open("alunos.csv", "r") as file:
    dados = file.read()

linhas = dados.split("\n")

for linha in linhas[1:]:
    aluno = linha.split(",")
    nome = aluno[1]
    soma = 0
    for nota in aluno[3:]:
        soma += float(nota)
    media = soma/4
    print(f"Nome: {nome} - Média: {media}")
print()


# 6. Faça um programa que crie um arquivo media.csv e guarde o RA (registro do aluno) junto com a respectiva média de cada um dos 
# alunos no arquivo alunos.csv.

with open("alunos.csv", "r") as file:
    dados = file.read()

linhas = dados.split("\n")

with open("media.csv", "w") as file:
    file.write("RA,Média\n")
    for linha in linhas[1:]:
        aluno = linha.split(",")
        ra = aluno[0]
        soma = 0
        for nota in aluno[3:]:
            soma += float(nota)
        media = soma/4
        file.write(f"{ra}, {media}\n")
print()