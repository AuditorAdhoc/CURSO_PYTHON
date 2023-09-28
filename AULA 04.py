
## LISTAS E FOR ##

# 1. Crie uma lista qualquer e faça um programa que imprima cada elemento da lista usando o for.

import random

lista = random.sample(range(0, 100), 5) # Gerando uma lista com 5 números aleatórios, com valores entre 0 e 99:
print(lista)

for i in range(len(lista)): 
    print(lista[i])

# 1. Outra Solução:

import random

lista_aleatoria = random.sample(range(0, 100), 10) #* Gera uma lista com 10 números aleatórios, com valores entre 0 e 99:
print(lista_aleatoria)

for i in lista_aleatoria: 
    print(i)

'''
random.sample(seq, k). Ela retornará uma lista de k elementos ÚNICOS da sequência em questão. 
A original será mantida intacta. Os elementos da lista resultante estarão na ordem selecionada. 
'''

# 2. Faça um programa que imprima todos os itens de uma lista usando while e compare com o exercício 1.

import random

lista = random.sample(range(0, 100), 5) #* Gera uma lista com 10 números aleatórios, com valores entre 0 e 99:
print(lista)

x = 0
while ( x < len(lista)): 
    print(lista[x])
    x+=1

# 3. Faça um programa que peça para o usúario digitar um número n e imprima uma lista com todos os números de 0 a n-1.

n = int(input("\nDigite um número: "))
print(list(range(0, n)), "\n")


# 4. Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares. 

import random

lista = random.sample(range(0, 100), 10) # Gerando uma lista com 10 números aleatórios, com valores entre 0 e 99:
print(lista, '\n')

lista_pares = []
pares = 0
for i in lista:
    if i % 2 == 0 and i != 0:
        lista_pares.append(i)
        pares += 1
print(lista_pares, '\n')
print(pares, "são pares.\n")


# 5. Faça um programa que imprima o maior número de uma lista, sem usar o método max(). 

import random

lista = random.sample(range(0, 100), 10)
print(lista, '\n')

if len(lista) <= 1:
    maior = lista[0]
else:
    maior = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
print ('O maior valor da lista é: ', maior, '\n')


# 6. Agora usando o método max() faça um programa que imprima os três maiores números de uma lista.
# Dica: Use o método próprio de lista .remove().

import random

lista = random.sample(range(0, 100), 5) # Gerando uma lista com 5 números aleatórios, com valores entre 0 e 99:
print(lista, '\n')

maior = []
while len(maior) < 3:
    maior.append(max(lista))
    lista.remove(max(lista))
print(maior, '\n')


# Outra solução

import random

lista = random.sample(range(0, 100), 10) # Gerando uma lista com 10 números aleatórios, com valores entre 0 e 99:
print(lista, '\n')

maiores = []
lista.sort() #* Ordena a lista
maiores = lista[-3:] #* Percorrendo uma lista de trás pra frente (retornando os três útimos)
print(maiores, '\n')


# 7. Faça um programa que, dadas duas listas de mesmo tamanho, crie uma nova lista com cada elemento igual a soma
# dos elementos da lista 1 com os da lista 2, na mesma posição.
# Exemplo: dadas lista 1 = [1, 4, 5] e lista 2 = [2, 2, 3], então lista 3 = [1+2, 4+2, 5+3] = [3, 6, 8]

import random

a = random.sample(range(0, 10), 3)
print(a, '\n')

b = random.sample(range(0, 10), 3)
print(b, '\n')

soma = [a[i] + b[i] for i in range(len(a))]
print(soma, '\n')


# 8. Faça uma programa que dadas duas listas de mesmo tamanho, imprima o produto escalar entre elas.
# OBS: produto escalar é a soma do resultado da multiplicação entre o número na posição i da lista1
# pelo número na posição i da lista2 com i variando de 0 ao tamanho da lista

import random

a = random.sample(range(0, 10), 3) # Gerando uma lista 'a' com 3 números aleatórios, com valores entre 0 e 9:
print(a, '\n')

b = random.sample(range(0, 10), 3) # Gerando uma lista 'b' com 3 números aleatórios, com valores entre 0 e 9:
print(b, '\n')

soma = [a[i] * b[i] for i in range(len(a))]
print(soma, '\n')
print("Produto escalar: ", sum(soma), '\n')

# Outra solução:

import random

a = random.sample(range(0, 10), 3) # Gerando uma lista 'a' com 3 números aleatórios, com valores entre 0 e 9:
print(a, '\n')

b = random.sample(range(0, 10), 3) # Gerando uma lista 'b' com 3 números aleatórios, com valores entre 0 e 9:
print(b, '\n')

lista = [a,b]

valores = []
pe = 0

for coluna in range(len(lista[0])):
    mult = 1

    for linha in range(len(lista)):
        if(lista[linha][coluna] >= 0):
            mult *= lista[linha][coluna]
            
    valores.append(mult)
    pe += mult
    
print(valores, '\n') 
print('Produto escalar:', pe, '\n')

# 9. Faça um programa que pede para o usuário digitar 5 números e, ao final, imprime uma lista com os 5 números 
# digitados pelo usuário (sem converter os números para int ou float).
# Exemplo: Se o usuário digitar 1, 5, 2, 3, 6, o programa deve imprimir a lista ['1','5','2','3','6']

lista = []
qtn = input('\nInforme a qtd de números: ')

for n in range(0, int(qtn)): 
    lista.append((input('Digite um número: ')))

print(lista, '\n')


# 10. Pegue a lista gerada no exercício anterior e transforme cada um dos itens dessa lista em float.
# OBS: Não é para alterar o programa anterior, mas sim a lista gerada por ele.

lista = []
qtn = input('\nInforme a qtd de números: ')

for n in range(0, int(qtn)): 
    lista.append((input('Digite um número: ')))

print(lista, '\n')

for i in range(len(lista)):
    lista[i] = float(lista[i])
print(lista, '\n')


# 11. Faça um Programa que peça as 4 notas bimestrais e mostre a média aritmética delas, usando listas

n1 = float(input("Informe sua nota do 1º Bimestre "))
n2 = float(input("Informe sua nota do 2º Bimestre "))
n3 = float(input("Informe sua nota do 3º Bimestre "))
n4 = float(input("Informe sua nota do 4º Bimestre "))

media = (n1 + n2 + n3 + n4) / 4
print("A média é",media, '\n')


# 11. Outra solução:

Notas = []

while len(Notas) < 4:
    Notas.append(float(input("Digite uma nota: ")))

media = sum(Notas) / 4
print("A média é: ",media, '\n')


# 11. Outra solução:

qtd_notas = int(input("Digite a quantidade de notas: "))
notas = 0
for i in range(0, qtd_notas):
    notas += int(input("Digite a nota " + str(i + 1) + ": "))

media = notas / qtd_notas
print("\nA média é: ",media, '\n')


# 12. Sortei uma lista de 10 números e imprima:
# a. uma lista com os 4 primeiros números;
# b. uma lista com os 5 últimos números;
# c. uma lista contendo apenas os elementos das posições pares;
# d. uma lista contendo apenas os elementos das posições impares;
# e. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da lista sorteada e termina com o primeiro);
# f. uma lista inversa dos 5 primeiros números;
# g. uma lista inversa dos 5 últimos números;

import random

sorteio = random.sample(range(0, 100), 10)
print("Lista: ", sorteio, '\n')
print("Os 4 primeiros: ", sorteio [0:4], '\n') 
print("Os 5 últimos: ", sorteio [5:], '\n') 
print("Os elementos de posições pares: ", sorteio[::2], '\n') 
print("Os elementos de posições ímpares: ", sorteio[1::2], '\n') 
print("Lista investida: ", sorteio [::-1], '\n') 
print("Lista inversa dos 5 primeiros: ", sorteio [4::-1], '\n')
print("Lista inversa dos 5 últimos: ", sorteio [:-6:-1], '\n') 
 

# 13. Faça um programa que sorteia 10 números entre 0 e 100 e conte quantos números soteados são maiores que 50.

import random

sorteio = random.sample(range(0, 101), 10) # Gerando uma lista 'a' com 10 números aleatórios, com valores entre 0 e 100:
print(sorteio, '\n')

maior = 50
filtro_lista = [i for i in sorteio if i > maior]
print(filtro_lista, '\n')
print('Quantidade de números maior que 50: ', len(filtro_lista), '\n')


# 13. Outra solução:

import random

sorteio = random.sample(range(0, 101), 10) # Gerando uma lista 'a' com 10 números aleatórios, com valores entre 0 e 100:
print(sorteio, '\n')

print('Quantidade de números maior que 50:', sum( i > 50 for i in sorteio), '\n')


# 14. Faça um programa que sorteie 10 números entre 0 e 100 e imprima:
# a. o maior número sorteado;
# b. o menor número sorteado;
# c. a média dos números sorteados;
# d. a soma dos números sorteados.

import random

sorteio = random.sample(range(0, 101), 10)
print(sorteio, '\n')
print ('Maior número da lista: ', max(sorteio))  
print ('Menor número da lista: ', min(sorteio))  
print ('Média da lista: ', sum(sorteio) / len(sorteio))
print ('Soma da lista: ', sum(sorteio), '\n')



# Desafio 1. Faça um programa que peça para o usuário digitar o nome e a idade de um aluno e o número de provas que esse
# aluno fez. Depois, o programa deve pedir para o usuário digitar as notas de cada prova do aluno. Ao final o programa
# deve imprimir uma lista contendo:

# a. Nome do aluno na posição 0
# b. Idade do aluno na posição 1
# c. Uma LISTA com todas as notas na posição 2
# d. A média do aluno na posição 3
# e. True ou False, caso a média seja maior que 5 ou não, na posição 4

# Dica: Use o que voçê fez nos exercícios anteriores para criar esse programa.

lista = []
lista.insert(0, input('\nDigite o nome do Aluno: '))
lista.insert(1, int(input('Digite a idade do Aluno: ')))
n_provas = int(input('Digite o número de provas: '))

Notas = []
while len(Notas) < n_provas:
    Notas.append(float(input("Digite uma nota: ")))

lista.insert(2, Notas)
media = sum(Notas) / len(Notas)
lista.insert(3, media)

if media > 5:
    lista.insert(4, True)
else:
     lista.insert(4, False)

print(lista, '\n')

# Desafio 2. Faça um programa como o do intem anterior, porém que imprima a média sem considerar a maior e menor nota do aluno (nesse caso o número de provas precisa ser obrigatoriamente maior que dois).
# Dica: crie uma cópia com a lista de todos as notas antes de fazer a média.


qtd_notas = int(input("\nDigite um número de provas (> 2): ")) 

while qtd_notas < 3:
    print('\nO número deve ser maior que 2!\n')
    qtd_notas = int(input("Digite o número de provas: ")) 
    break

Notas = []
for i in range(0, qtd_notas):
   Notas.append(int(input("Digite a nota " + str(i + 1) + ": ")))

print(Notas, '\n')

Notas.sort() # ordenando a lista 
del Notas[0] # exclui a menor nota
del Notas[-1] # exclui a maior nota

media = sum(Notas) / len(Notas)

print(Notas, '\n')
print('Média das Notas:',media, '\n') # Média sem a maior e menor nota.


# Outra solução:




# Desafio 3.Faça um programa que pede para o usuário digitar o CPF e verificar se ele é válido. Para isso, 
# primeiramente o programa deve multiplicar cada um dos 9 primeiros dígitos do CPF pelos números de 10 a 2 e 
# somar todas as respostas. O resultado deve ser multiplicado por 10 e dividido por 11. O resto dessa divisão 
# deve ser igual ao primeiro dígito verificado (10° dígito). Em seguida, o programa deve mutiplicar cada um dos 
# 10 primeiros dígitos do CPF pelos números de 11 a 2 e repetir o procedimento anterior para verificar o segundo 
# dígito verificador.

from random import randint


def cpf_validate(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


def cpf_generate():
    #  Gera os primeiros nove dígitos (e certifica-se de que não são todos iguais)
    while True:
        cpf = [randint(0, 9) for i in range(9)]
        if cpf != cpf[::-1]:
            break

    #  Gera os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        cpf.append(digit)

    #  Retorna o CPF como string
    result = ''.join(map(str, cpf))
    return result


opcao = int(input('''[1] Validar um CPF 
[2] Gerar um CPF válido
Opção: '''))
if opcao == 1:
    cpf = input('Digite o CPF: ')
    if cpf_validate(cpf):
        print('CPF válido.')
    else:
        print('CPF inválido.')
elif opcao == 2:
    cpf = cpf_generate()
    if cpf_validate(cpf):
        print(f'CPF gerado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
else:
    print('Inválido.')


# Outra solução:

from random import randint

def validaCPF(numeros):
    cpf = [int(char) for char in numeros if char.isdigit()] #> Obtém os números e despreza os outros caracteres

    if len(cpf) != 11: ## Verifica se tem 11 dígitos
        return print("O números de CPF deve ter 11 dígitos!")

    if cpf == cpf[::-1]: #? Verifica se tem todos os números iguais.
        return print("Os números devem ser diferentes!")

    for i in range(9, 11): #- Valida os dois dígitos verificadores
        soma = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digito_verificador = ((soma * 10) % 11) % 10
        if digito_verificador != cpf[i]:
            return False
    return True

#### Chama a função ####

cpf = input('\nDigite um CPF: ')
if validaCPF(cpf):
    print('\nCPF válido!\n')
else:
    print('\nCPF inválido!\n')


# Outra solução:

from random import randint

def validaCPF(numeros):
    cpf = [int(char) for char in numeros if char.isdigit()] #> Obtém os números e despreza os outros caracteres

    if len(cpf) != 11: ## Verifica se tem 11 dígitos
        return print("\nO números de CPF deve ter 11 dígitos!")

    if cpf == cpf[::-1]: #? Verifica se tem todos os números iguais.
        return print("\nOs números devem ser diferentes!")

    soma = 0
    for i in range(9): 
        soma += (10 - i) * cpf[i]
    if soma * 10 % 11 == cpf[9]: #- Verifica o primeiro dígito verificador
        soma = 0
        for i in range(10): 
            soma += (11 - i) * cpf[i]
        if soma * 10 % 11 == cpf[10]: #- Verifica o segundo dígito verificador
            return True
    return False

#### Chama a função ####

cpf = input('\nDigite um CPF: ')
if validaCPF(cpf):
    print('\nCPF válido!\n')
else:
    print('\nCPF inválido!\n')