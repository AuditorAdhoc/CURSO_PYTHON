
### FUNÇÕES ###

# 1. Faça uma função que recebe um número e imprime seu dobro.

def dobro(n):
    return num * 2

# Pograma: 
num = int(input("\nDigite um número: ")) 
print("Dobro =", dobro(num), '\n')


# 2. Faça uma função que recebe o valor do raio de um círculo e retorna o valor do comprimento de sua circunferência: C = 2*pi*r.

import math

def circ(r):
    circunf = (2 * math.pi * r)
    return circunf

# Progama:
raio = float(input('\nDigite o valor do raio do círculo: '))
print("O cumprimento da circunferência: {:.2f}".format(circ(raio)), '\n')


# 3. Faça uma função para CADA operação matemática básica (soma, subtração, multiplicação e divisão). As funções devem receber dois números e retornar o resultado da operação.

import random

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

# Programa:
num1 = random.randint(10, 20)
num2 = random.randint(2, 5)

print("\nSORTEIO:", num1, "e",  num2, '\n')
print(f"SOMA: {num1} + {num2} =",somar(num1,num2), '\n')
print(f"SUBTAÇÃO: {num1} - {num2} =",subtrair(num1,num2), '\n')
print(f"MULTIPLICAÇÃO: {num1} * {num2} =",multiplicar(num1,num2), '\n')
print(f"DIVISÃO: {num1} / {num2} =",dividir(num1,num2), '\n')


# 4. Faça uma função que recebe um nome e imprime "olá,[nome]".

def saudacao(nome):
    print('\nOlá,',nome,'\n')
    return nome

# Programa:
name = input('\nDigite um nome:')
saudacao(name)


# 5. Faça uma função que recebe um nome e um horário e imprime "Bom dia, [nome]", caso seja antes de 12h, "Boa tarde, [nome]", caso seja entre 12h e 18h e "Boa noite, [nome]" se for após às 18h.

def saudacoes(nome, horario):
        
    if (horario < 12):
        print("\nBom dia,",nome,'\n')
    elif (horario < 18):
        print("\nBoa tarde,",nome,'\n')
    else:
        print("\nBoa noite,",nome,'\n')

#Programa:
name = (input("\nQual seu nome:")) 
hour = int(input("Digite uma hora:"))
saudacoes(name, hour)


# 6. Faça uma função que recebe um número e retorna True se ele é par ou False, se ele é impar.

def par(num):
    if numero % 2 == 0:
        return True
    else:
        return False

# Programa:
numero = float(input('\nDigite um número para saber se é par ou impar:'))
print(f"\nO {numero} é PAR?", par(numero),'\n')


# 7. Faça uma função que sorteia 10 números aleatórios entre 0 e 100 e retorna o maior entre eles.

import random

def sorteio():
    sorteio = random.sample(range(0, 101), 10)
    maior = max(sorteio)
    print()
    print(sorteio, '\n')
    return maior

#Programa:
print ('Maior número da lista:', sorteio(), '\n')  


# 8. Faça uma função que receba um número n de entrada, sorteia n números aleatórios entre 0 e 100 e retorna a média deles.

import random

def sorteio1(n):
    sorteio = random.sample(range(0, 101), n)
    print()
    print("SORTEIO:", sorteio, '\n')
    return sum(sorteio)/len(sorteio)

#Programa:
n = int(input('\nDigite a qtd de números para sorteio:'))
print ('A média é:', sorteio1(n), '\n')  

#! Dúvida:
# 9. Faça uma função que recebe uma lista de palavras e retorna uma lista contendo as mesmas palavras da lista anterior, pórem escritas em caixa alta.
# retorna a lista com as palavras em caixa alta

def caixa_alta(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].upper()
    return lista

# Programa:
lista_de_palavras = ['Python', 'Tiago', 'Letscode']
lista_caixa_alta = caixa_alta(lista_de_palavras)
print(lista_caixa_alta)

#- Outra solução:

import random

def upper(letras):
    caixa_alta = []
    for i in letras:
        caixa_alta.append(i.upper())
    return caixa_alta

# Programa:
lista = []
string = ''
for i in range(5):
    string += '%c' % random.randint(97,122)  #- Cria uma string 
    lista.append(string)
print()
print("STRING:", string, '\n')
print("LISTA DE PALAVRAS:", lista, '\n')
print("LISTA CAIXA_ALTA: ", upper(lista), '\n')


# 10. Faça uma função que recebe duas listas e retorna a soma item a item dessas listas.
# Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar [1+3, 4+5, 3+1] = [4,9,4]

import random

def soma_lista(listaA, listaB):
    soma = [listaA[i] + listaB[i] for i in range(len(listaA))]
    return soma

# Programa:
a = random.sample(range(0, 10), 3)
print("\nLISTA A:", a, '\n')
b = random.sample(range(0, 10), 3)
print("LISTA B:", b, '\n')
print("SOMA:   ", soma_lista(a, b),'\n')


# 11. Faça uma função que receba duas listas e retone o produto item a item dessas listas.
# Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar [1x3, 4x5, 3x1] = [3,20,3]

import random

def multiplicacao(listaA, listaB):
    mult = [listaA[i] * listaB[i] for i in range(len(listaA))]
    return mult

a = random.sample(range(0, 10), 3)
print("\nLISTA A:   ", a, '\n')
b = random.sample(range(0, 10), 3)
print("LISTA B:   ", b, '\n')
print("MULTIPLIC.:", multiplicacao(a, b),'\n')


# 12. Faça uma função que recebe um número x e uma lista numérica e retorna uma lista cujos elementos são os itens da lista de 
# entrada multiplicado por x.

import random

def mult_lista(num, lista):
    r = [lista[i] * num for i in range(len(lista))]
    return r

num = int(input('\nDigite um número para multiplicar a lista: '))
lista = random.sample(range(0, 10), 3)
print()
print(lista, "x", num, "=", mult_lista(num, lista), '\n')


# 13. Faça uma função que recebe uma lista de números e retorna a soma dos elementos dessa lista.

import random

def soma_lista(lista):
    soma = sum(lista[i] for i in range(len(lista)))
    return soma

# Programa:
a = random.sample(range(0, 10), 5)
print()
print(a)
print("\nSoma dos elementos da lista:", soma_lista(a), "\n")

# 14. Faça uma função que recebe uma lista de números e retorna a média aritmética dos elementos dessa lista.

import random

def media_lista(lista):
    media = sum(lista[i] for i in range(len(lista))) / len(lista)
    return media

# Programa:
a = random.sample(range(0, 10), 5)
print()
print(a, '\n')
print("Média dos elementos da lista: ", media_lista(a),'\n')


# Desafio 1. Faça uma função que receba um número e calcule seu fatorial.

def fatorial(n):
    fat = 1
    for i in range(n):
        fat = fat * (i+1)
    return fat

# Programa:
num = int(input("\nDigite o valor de n: "))
print(f"\nFatorial de {num} é:", fatorial(num),'\n')


# Desafio 2. Super Desafio!. Repita o exercício anterior usando recursão, ou seja, uma função que chame ela mesma, lembrando que 3! = 3*2!, que 2! = 2*1! = 1*0! e 0!=1.

def fatorial_recursivo(n):
    if (n == 0 or n == 1):
        return 1
    if (n > 1):
        return n * fatorial_recursivo(n -1) # recursividade - chama a própria função dentro da função

# Programa:
num = int(input("\nDigite o valor de n: "))
print(f"\nFatorial de {num} é:", fatorial_recursivo(num),'\n')

#! Dúvida:
# Desafio 3. Faça uma função que recebe duas entradas: um input dado pelo usuário e um string que informa o tipo de dado ("idade", 
# "salario" ou "sexo"), e verifica se os dados digitados foram válidos, usando os seguintes critérios:
# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, F ou Outro.

def validacao(entrada, string):
    if (string == "idade" or string == "Idade") and entrada >= 0 and entrada <= 150:
        return True
    if (string == "salário" or string == "Salário") and entrada > 0:
        return True
    if (string == "sexo" or string == "Sexo") and (entrada == 'M' or entrada == 'F' or entrada == 'Outro'):
        return True
    return False

# Programa:
string = input("\nDigite qual dado pretende verificar (idade/salário/sexo)?")
entry = input(f"\nDigite {string} correspondente:")
print(validacao(entry, string),'\n')

# Desafio 4. A sequência Fibonacci é a sequência cujos dois primeiros termos são 1 e os demais são obtidos através da soma de seus dois 
# antecessores, isso é:
# a. Fibonacci(1) = 1 e Fibonacci(2) = 2;
# b. dado qualquer número n >= 3, Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2) 
# Assim, os 10 primeiros termos da sequência Fibonacci são: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
# Faça uma função que receba um número n e calcule o termo de número n da sequência Fibonacci.

def fibonacci(n):
    if (n == 1 or n == 2):
        return 1

    sequencia = [1,1]

    for i in range(2, n): # range inicia em 2, pois sequencia já tem os dois primeiros termos
        sequencia.append(sequencia[i - 1] + sequencia[i - 2])
    print()
    print(sequencia)
    return sequencia[-1] # retorna o último termo da sequencia

# Programa:
num = int(input("\nDigite o valor de n: "))
print(f"\nFibonacci de {num} é:", fibonacci(num),'\n')


# 5. Super Desafio! Refaça o desafio 4 usando recursão.

def fibonacci_recursao(n):
    if n <= 2:
        return 1
    return fibonacci_recursao(n-1) + fibonacci_recursao(n-2)

# Programa:
n = int(input("\nDigite o valor de n: "))
print(f"\nFibonacci de {n} é:", fibonacci_recursao(n),'\n')


# 6. Super Desafio! - Faça um jogo de BlackJack usando funções: o BlackJack, ou Vinte e Um, é um jogo em que os jogadores podem comprar 
# cartas livremente, enquanto tiverem menos de 21 pontos. No nosso jogo, o Ás vale um ponto; as cartas de 2 a 10 valem o número de pontos 
# que elas representam; e Valete, Dama e Rei valem 10 pontos cada. Ganha o jogador que tiver o maior número de pontos, desde que este seja 
# menor ou igual a 21. Nosso jogo deve ter as seguintes funções:

# a. Função principal: a função que vamos chamar para iniciar o jogo. Essa função não irá receber nem retornar nenhuma variável. Ela deve 
# perguntar o número de jogadores participantes e o nome de cada um. Em seguida ela chama as outras funções do jogo.
# b. Função para criar o baralho: essa função deve criar um baralho (uma lista) com as cartas do baralho. 
# c. Função para a jogada: essa função deve receber o nome do jogador que irá realizar a jogada e, caso ele ainda esteja ativo (tenha 
# menos de 21 pontos e ainda não tenha desistido de comprar cartas) deve perguntar se ele quer comprar uma carta. Se ele responder que 
# sim, a função deve chamar a próxima função para sortear uma carta e somar o valor retornado na pontuação do jogador; se ele responder 
# que não, a função deve desativar o jogador para que ele não possa mais comprar cartas; Essa função só deve ser chamada enquanto houver 
# jogadores ativos. 
# d. Função para o sorteio: essa função retira uma carta aleatória do baralho e retorna o número de pontos que essa carta vale. 
# e. Função verificação: verifica e indica qual/quais jogador/jogadores tem o maior número de pontos, que seja menor ou igual a 21.

import random

def criarBaralho():
    baralho = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Q", "J", "K"]*4
    print("\nBaralho criado!")
    return baralho

def jogo(jogadores, baralho):
    existem_ativos = True # Variável que controla o fluxo do jogo. Começa em true para entrar no loop
    while existem_ativos:
        existem_ativos = False # Em cada iteração do loop, começa como falsa,
                               # e se encontrar qualquer jogador ativo, é atualizada
        for jogador in jogadores:
            jogada(jogador, baralho)
            if jogador[2] == True:  # Verifica após a jogada se ele ainda está ativo
                existem_ativos = True

def jogada(jogador, baralho):
    if jogador[2] == True: # Jogador está ativo
        print("\nJogada de", jogador[0], "com", jogador[1], "pontos.")
        pergunta = input("Você que comprar 1 carta? ")
        if pergunta == "sim" or pergunta == "Sim" or pergunta == "SIM":
            carta = sorteio(baralho)
            jogador[1] += carta
            print("\nVocê agora tem", jogador[1], "pontos.")
            if jogador[1] > 21:
                print("Que azar!")
                jogador[2] = False # Desativa o jogador
        else:
            print("\nOk, você parou de comprar.")
            jogador[2] = False
    print()

def sorteio(baralho):
    carta = random.choice(baralho)
    baralho.remove(carta)
    if carta == 'A':
        pontos = 1
    elif carta == 'Q' or carta == 'J' or carta == 'K':
        pontos = 10
    else:
        pontos = int(carta)
    print("\nVocê comprou um", carta, "que vale", pontos, "pontos")
    return pontos

def verificacao(jogadores):
    vencedor = None
    empate = False
    maximo_pontos = 0
    for jogador in jogadores:
        pontos = jogador[1]
        if pontos <= 21:
            if pontos > maximo_pontos:
                vencedor = jogador
                maximo_pontos = pontos
                empate = False
            elif pontos == maximo_pontos:
                vencedor = None
                empate = True

    if empate:
        print("\nTemos um empate!")
    elif vencedor == None:
        print("\nTodos estouraram 21!")
    else:
        print("\nO vencedor foi", jogador[0], "com", jogador[1], "pontos.\n")

def main():
    print("\nBem Vindo ao BlackJack em Python!!\n")
    n_jogadores = int(input("Quantos jogadores participarão da partida? "))
    jogadores = []
    for i in range(n_jogadores):
        nome = input(f"Digite o nome do {i}° jogador? ")
        pontos = 0
        ativo = True
        jogador = [nome, pontos, ativo]
        jogadores.append(jogador)

    baralho = criarBaralho()
    jogo(jogadores, baralho)
    verificacao(jogadores)

main()



# 7. Super desafio! Faça um sistema de cadastro de clientes. Modele cada cliente como uma lista de três elementos: nome, CPF e e-mail. 

# a. Faça uma função que peça o nome, o CPF e o e-mail da pessoa e retorne uma lista contendo esses elementos nessa ordem. 
# b. Os clientes cadastrados devem ser armazenados em uma lista (uma lista de listas, já que cada cliente será uma lista tal como 
# produzido no item a). 
# c. Faça uma função que recebe a lista do item b) e um CPF e, se esse cliente estiver na lista de cadastro, sua função deve devolver a 
# lista de dados desse cliente; caso contrário, sua função deve imprimir “não encontrado”.
# d. Enquanto não for digitado 0, o seu programa deve continuar rodando. Se digitado 1, seu programa deve cadastrar um novo cliente; se 
# digitado 2, seu programa deve pedir um CPF e procurá-lo na lista de clientes (item c); se digitado 3, seu programa deve imprimir todos 
# os clientes cadastrados.

def cadastrarCliente():
    nome = input("\nDigite o nome do Cliente: ")
    cpf = input("Digite o CPF: ")
    email = input("Digite o email: ")
    return [nome, cpf, email]

def digito():
    print()
    print("# Digite um número #\n")
    print("0 - Sair do programa")
    print("1 - Cadastrar Cliente")
    print("2 - Encontrar Cliente")
    print("3 - Imprimir Clientes")
    digit = int(input())
    return digit

def procurarCliente(lista, cpf):
    for cliente in lista:
        if cliente[1] == cpf:
            return cliente
    print("Não encontrado!")

def imprimirClientes(lista):
    print("\n# Lista de clientes #\n")
    for cliente in lista:
        print(cliente)

# Programa:
clientes = [] 
digit = digito()

while digit != 0:
    if digit == 1:
        clientes.append(cadastrarCliente())
        print("\nCadastrado com sucesso!")
    elif digit == 2:
        cpf = input("\nDigite o CPF do Cliente: ")
        cliente = procurarCliente(clientes, cpf)
        if cliente != None:
            print("\n As informações do cliente são:\n")
            print(cliente)
    elif digit == 3:
        imprimirClientes(clientes)
    else:
        print("Digite outra vez.")

    digit = digito()

print("\nVocê saiu do programa. Até mais\n")
