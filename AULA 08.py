
## TUPLAS E DICIONÁRIOS

# 1. Crie uma tupla com todos os números de 0 a 9. Explore a sintaxe: use e depois não use parênteses.

#* com parênteses:
tuplaA = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

#* sem parênteses:
tuplaB = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

#* de uma lista:
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tuplaC = tuple(lista)

print("\n",tuplaA)
print("\n",tuplaB)
print("\n",tuplaC)
print()

# 2. Crie uma tupla com todos os pares entre 0 e 100 (inclusive).

lista = []
for i in range(0, 101, 2):
    lista.append(i)

tupla = tuple(lista)
print(tupla)

#> Outra solução:

lista = []
lista = [i for i in range(0, 101, 2)]

tupla = tuple(lista)
print(tupla)


# 3. Crie uma função que recebe uma lista de números e devolve, nesta ordem, o mínimo, a média, o desvio padrão e o máximo.

import statistics
import random

def ListaNumeros (numbers):
    maior = max(numbers) #* Maior
    menor = min(numbers) #* Menor

    soma = 0
    for n in numbers:
        soma = soma + n
    media = soma/len(numbers) #* Média

    desvio = statistics.stdev(numbers) #* Desvio Padrão

    return menor, media, desvio, maior

lista_aleatoria = random.sample(range(0, 20), 5) 

minimo, media, desvio, maximo = ListaNumeros(lista_aleatoria)

print('\nLista = ', lista_aleatoria)
print('\nMínimo = ', minimo)
print('\nMédia = ', media)
print('\nDesvio padrão = ', desvio)
print('\nMáximo = ', maximo, "\n")


# 4. Crie uma função que recebe uma lista e retorna True se todos os seus elementos forem numéricos (int, float ou string contendo um 
# int ou float) ou False do contrário. A função deve também retornar a lista tratada: transformar todas as entradas não numéricas em 
# numéricas ou, no melhor caso, devolver a lista apenas.


# Exemplo de 2 resoluções: 2 interpretações diferentes para o exercício


#> Solução 1: Converte strings que contém apenas dígitos em números e não converte strings que contém letras. 
#! Tratar a string
def trataLista(list):
    numericos = True
    nova = []
    for i in lista:
        tipo = type(i)
        if not(type(i) == float or type(i) == int):
            if ((i.isdigit() and type(i) == str)):  #* É string mas é possível tratar
                nova.append(float(i))
            else: #* Não é possível tratar
                nova.append(i)
                numericos = False
        else: #* É numérico
            nova.append(i)
    return numericos, nova

lista = [90, "12", 42, "Python", 16, "sete", 6.3]
print()
print(trataLista(lista), "\n")


#> Solução 2: Não converte strings que contém apenas dígitos (considera como entrada numérica) mas converte strings que contém 
#> letras em uma entrada numérica, no caso 0 (zero). 

def listaNumerica(lista):
    tratada = []
    saoNumericos = True

    for elemento in lista:
        string = str(elemento)
        string = string.replace('-', '') #* tratando sinal negativo
        string = string.replace('.', '') #* tratando ponto decimal
        numerica = string.isdigit()   #* retorna False se uma string contém qualquer coisa diferente de número
        if numerica:
            tratada.append(elemento)
        else:
            #* o enunciado pediu para transformar entradas não-numéricas em numéricas
            #* como não especificaram COMO, vamos trocar não-numéricas por 0
            tratada.append(0)
            saoNumericos = False

    return (saoNumericos, tratada)

numerica = [-1, 2.7, '3.14']
naoNumerica = [1, 'dois', 3.0]

print(numerica)
resp, lista = listaNumerica(numerica)
print('É numérica?', resp)
print('Tratada: ', lista)

print(naoNumerica)
resp, lista = listaNumerica(naoNumerica)
print('É numérica?', resp)
print('Tratada: ', lista)

# 5. Faça uma função que recebe valores a, b e c, resolve a equação quadrática ax^2+ bx + c = 0 e retorna:
# a. o valor de Δ onde Δ=b^2- 4ac
# b. uma tupla com o valor do ponto de mínimo ou máximo, onde, x_m=-b/2a e y_m  = -Δ/4a;
# c. uma lista contendo as raízes (a lista pode ser vazia, caso Δ<0;  pode conter apenas um elemento, caso Δ = 0; ou conter duas raízes, 
# caso Δ> 0).

import math

def eq_Quadratica(a, b, c):
    delta = b**2 - 4*a*c

    x_m = -b/(2*a)
    y_m = -delta/(4*a)

    raizes = []
    if delta == 0:
        raizes.append(x_m)
    elif delta > 0:
        raiz = math.sqrt(delta)
        x1 = (-b + raiz) / (2*a)
        x2 = (-b - raiz) / (2*a)
        raizes = [x1, x2]
    return (delta, (x_m, y_m), raizes)

delta, ponto, raizes = eq_Quadratica(1, -4, 5)
print('\nDelta Negativo = x² - 4x + 5 = 0')
print('DELTA (∆) = ', delta)
print('Ponto Min = ', ponto)
print('Raizes: ', raizes)

delta, ponto, raizes = eq_Quadratica(4, -4, 1)
print('\nDelta Nulo = 4x² - 4x + 1 = 0')
print('DELTA (∆) =', delta)
print('Ponto Min = ', ponto)
print('Raizes = ', raizes)

delta, ponto, raizes = eq_Quadratica(1, -5, 6)
print('\nDelta Positivo = x² - 5x + 6 = 0')
print('DELTA (∆) = ', delta)
print('Ponto Max = ', ponto)
print('Raizes = ', raizes)
print()


#> Outra solução:


import math
    
print("Vamos calcular uma equação do 2° grau da forma: ax² + bx + c:", "\n")
    
a = int( input("Digite o coeficiente a: ") )

if(a==0):
    print("\n","Se a for igual a zero não é equação do segundo grau!", "\n")
else:
    b = int( input("Digite o coeficiente b: "))
    c = int( input("Digite o coeficiente c: "))
    delta = b*b - (4*a*c)

    if delta<0:
        print("\n","Delta menor que 0. Raízes imaginárias!", "\n")
    elif delta==0:
        raiz = -b / (2*a)
        print("Delta=0 , raiz = ",raiz)
    else:
        raiz1 = (-b + math.sqrt(delta) ) / (2*a)
        raiz2 = (-b - math.sqrt(delta) ) / (2*a)
        print("Raizes: ",raiz1," e ",raiz2, "\n")

#> Outra solução:

def raizess(a, b, c):
    D = (b**2 - 4*a*c)
    x1 = (-b + D**(1/2)) / (2*a)
    x2 = (-b - D**(1/2)) / (2*a)

    print('\nValor de x1: {0q}'.format(x1))
    print('Valor de x2: {0}'.format(x2))

if __name__ == '__main__':
    while True:
        print('Calculando as raízes de uma equação de 2º grau\n')
        a = float(input('Entre com o valor de a: '))
        b = float(input('Entre com o valor de b: '))
        c = float(input('Entre com o valor de c: '))
        raizess(a,b,c)

        continua = input('Deseja sair? Digite q ou Enter para novo cálculo:')
        if (continua == 'q'):
            break


## DICIONÁRIOS

# 1. Crie um dicionário cujas chaves são os meses do ano e os valores são a duração (em dias) de cada mês.

meses = {'Janeiro': 31, 'Fevereiro': 28, 'Março': 31, 'Abril': 30, 'Maio':31, 'Junho':30, 'Agosto':31, 'Setembro':30, 'Outubro':31, 'Novembro':30, 'Dezembro':31}


# 2. Imprima as chaves seguidas dos seus valores para o dicionário criado no exercício 1. 

meses = {'Janeiro': 31, 'Fevereiro': 28, 'Março': 31, 'Abril': 30, 'Maio':31, 'Junho':30, 'Agosto':31, 'Setembro':30, 'Outubro':31, 'Novembro':30, 'Dezembro':31}

print()
for chaves, valores in meses.items():
    print("%s - %d" %(chaves, valores), "dias")
print()

'''
for chave in meses:
	print("O mês {} tem {} dias".format(chave, meses[chave]))
'''


# 3. Crie um dicionário para as seguintes relações:
# 	‘Banana’: 3.0
# 	‘Cebola’: 4.0
# 	‘Maçã’: 5.7
# 	‘Abacaxi’: 8.0

dic_frutas = {'Banana': 3.0, 'Cebola': 4.0, 'Maçã': 5.7, 'Abacaxi': 8.0}


# 4. Altere o valor da chave ‘Maçã’ no dicionário do exercício anterior para 8.6.

dic_frutas = {'Banana': 3.0, 'Cebola': 4.0, 'Maçã': 5.7, 'Abacaxi': 8.0}

print()
dic_frutas['Maçã'] = 8.6
print(dic_frutas)
print()


# 5. Crie uma função que receba os valores do nome, idade e e-mail de uma pessoa e guarde-os em um dicionário com as chaves ‘nome’, ‘idade’ e ‘email’, respectivamente. Sua função deve retornar esse dicionário.

def usuario(nome, idade, email):
    return { "Nome": nome, "Idade": idade, "e-mail": email }

nome = input("\nDigite o seu nome: ")
idade = input("Digite sua idade: ")
email = input("Digite seu e-mail: ")

dicionario = usuario(nome, idade, email)

print("\nUsuário = ", dicionario, "\n")


# 6. Como você armazenaria a seguinte tabela usando apenas dicionários? Tente imprimir o valor correspondente da linha Pedro x Coluna B.

tab = {}
tab["Maria"] = { "Coluna A": 1, "Coluna B": 5 }
tab["Pedro"] = { "Coluna A": 0.5, "Coluna B": 3 }
tab["João"] = { "Coluna A": 3.2, "Coluna B": 1 }
print("\nPedro x Coluna B = ", tab["Pedro"]["Coluna B"], "\n")


# 7. Faça uma função que receba uma lista e conte quantas vezes cada elemento apareceu nessa lista. Essa função deverá guardar os dados 
# em um dicionário no qual as chaves são os elementos da lista e os valores são a contagem de quantas vezes esse elemento aparece.

import random

def contador(lista):
    contador = {}
    for i in lista:
        if i not in contador.keys():
            contador[i] = 1
        else:
            contador[i] += 1
    return contador

frase=''
for i in range(33):
    frase += '%c' % random.randint(97,122)
lista_string = list(frase)

print("\nLISTA: ", lista_string, "\n")

print(contador(lista_string), "\n")


# 8. Faça um programa que fique pedindo uma resposta do usuário, entre 1, 2 e 3. Se o usuário digitar 1, o programa deve cadastrar um novo 
# usuário nos moldes do exercício 5 e guardar esse cadastro num dicionário cuja chave será o CPF da pessoa. Quando o usuário digitar 2, o 
# programa deve imprimir os usuários cadastrados; e se o usuário digitar 3, o programa deve fechar.

# e 9. Implemente um sistema de busca para o programa do exercício 7, isso é, se o usuário digitar 4, procure um determinado usuário pelo 
# seu CPF.

def cadastra(nome, idade, email):
    return { "Nome": nome, "Idade": idade, "e-mail": email }

usuarios = {}
digito = 0 
while digito != 3: #* finaliza a função
    print("\n   === ESCOLHA ===\n")
    print("1 - Cadastrar Usuário")
    print("2 - Exibir Usuários")
    print("3 - Finalizar Programa")
    print("4 - Pesquisar Usuário")
    digito = int(input("\nEscolha uma opção: "))

    if digito == 1:
        print("\n=== Cadastrar Usuários ===\n")
        CPF = input("CPF: ")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        email = input("Email: ")
        usuarios[CPF] = cadastra(nome, idade, email)
        print("\nUsuário Cadastrado!")

    elif digito == 2:
        if len(usuarios) == 0:
            print("Não há usuários cadastrados!")
        else:
            print("\n     === Usuários cadastrados ===\n")
            for i in usuarios.items():
                print(i)
    
    elif digito == 4:
        print("\n=== Pesquisar Usuários ===\n")
        CPF = input("CPF: ")
        if CPF in usuarios.keys():
            print(usuarios[CPF])
        else:
            print("\nUsuário inexistente!")


# 10. Faça o análogo do exercício 6 para strings: conte quantas vezes cada caracter apareceu nessa string e retorne um dicionário com essa contagem.

import random

def contaLetras(texto):
    contador = {}
    for i in texto:
        if i not in contador.keys():
            contador[i] = 1
        else:
            contador[i] += 1
    return contador

texto=''
for i in range(10):
    texto += '%c' % random.randint(97,122)
print()
print(texto)
print()
print(contaLetras(texto))
print()