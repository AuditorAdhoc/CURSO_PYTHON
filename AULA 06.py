
### Exemplos de Aula ###

'''
E1) Crie um programa que recebe uma frase e, em seguida, uma letra do usuário. Seu objetivo será imprimir o número de vezes que aquele 
letra aparece na frase.
'''

frase = input ('Informe um texto: ')
letra = input ('Informe uma letra: ')
contador = 0
for l in frase:
    if (l == letra):
        contador += 1

print (contador)


'''
E2) João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, e não tem certeza se conseguirá montar o 
número desejado. Considerando a configuração dos leds dos números abaixo, faça um algoritmo que ajude João a descobrir a quantidade de 
leds necessário para montar o valor.
'''

qtd_leds = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]
numero = input ('Informe o número desejado: ')
n_leds = 0

for i in range(len(numero)):
    inteiro = int(numero[i]) # 1 1 5 3 8 0

    n_leds += qtd_leds[inteiro - 1]
print(n_leds)

'''
E3) Crie um programa que recebe um horário informado pelo usuário e retorna os minutos e os segundos. Para isso, considere que o usuário 
pode informar o horário em diferentes formatos, como mostra a tabela abaixo:
'''

'''
E4) DESAFIO! Júlio César usava um sistema de criptografia, agora conhecido como Cifra de César, que trocava cada letra pelo equivalente 
em duas posições à Direita no alfabeto (por exemplo, 'A' vira 'C', 'R' vira 'T', etc.). Ao começo do alfabeto nós voltamos para o fim, 
isto é 'Y' vira 'A'. Nós podemos, é claro, tentar trocar as letras com quaisquer número de posições.
Crie um programa em Python que imprima o texto decodificado (transformado novamente para o texto original) conforme o exemplo abaixo.
'''


### STRINGS ###

# 1. Faça um programa que pede para o usuário digitar uma palavra e imprima cada letra em uma linha.

string = input("\nDigite uma palavra: ")
for letra in string:
    print(letra)
print()

# 2. Faça um programa que pede para o usuário digitar uma palavra e cria uma nova string igual, copiando letra por letra a palavra 
# digitada, depois imprima a nova string.

string = input("\nDigite uma palavra: ")
new_string = ""
for letra in string:
    new_string += letra
print()
print(new_string, "\n")


# 3. Altere o exercício anterior para que a string copiada alterne entre letras maiúsculas e minúsculas
# Exemplo: se o usuário digitar "latex" o programa deve imprimir "LaTeX".

string = input("\nDigite uma palavra: ")
intercalado = ""
for letra in range(len(string)):
    caracter = string[letra]
    if letra % 2 == 0:
        intercalado += caracter.upper()
    else:
        intercalado += caracter.lower()
print()
print(intercalado, "\n")


# 4. Faça um programa que pede para o usuário digitar uma palavra e cria uma nova string igual, porém com espaço entre cada letra, 
# depois imprima a nova string:
# Exemplo: se o usuário digitar "python" o programa deve imprimir "p y t h o n "

string = input("\nDigite uma palavra: ")
new = ""
for letra in string:
    new += letra + " "
print()
print(new, "\n")


# 5. Faça uma função que receba uma string e retorne uma nova string substituindo:
# 'a' por '4'
# 'e' por '3'
# 'I' por '1'
# 't' por '7'

def Trocas(new):
    letras = {"a":"4", "e":"3", "i":"1", "t":"7"}
    for i in letras:
        new = new.replace(i, letras[i])
    return new

# Programa:
string = input("\nDigite uma palavra: ")
print()
print (Trocas(string), "\n")


# 6. Faça uma função que recebe uma string e retorna ela ao contrário. Exemplo: Recebe "teste" e retorna "etset".

def Invertida(s):
    s.reverse()
    return ''.join(s)

# Programa: 
string = list(input("\nDigite uma palavra: "))
print()
print (Invertida(string), "\n")

# Outra solução:

def Invertida_Dois(s):
    return ''.join(reversed(s))

# Programa:
string = input("\nDigite uma palavra: ")
print()
print (Invertida_Dois(string), "\n")

# Outra solução:

def Invertida_Tres(s):
    return s[::-1] # string [inicio:fim:passo]

# Programa:
string = input("\nDigite uma palavra: ")
print()
print (Invertida_Tres(string), "\n")


# 7. Agora faça uma função que recebe uma palavra e diz se ela é um palíndromo, ou seja, se ela é igual a ela mesma ao contrário.
# Dica: Use a função do exercício 5.

def palindromo(palavra):
    new = palavra.lower().strip().replace(' ', '')
    if new == new[::-1]:
        print("\nÉ palíndromo!")
    else:
        print("\nNão é palídromo!")

# Programa:
string = input("\nDigite uma palavra para verificar se é um palídromo? ")
print(palindromo(string), "\n")


# 8. Faça uma função que receba um texto e uma palavra, então verifique se a palavra está no texto, retornando True ou False.

def Procura(text, word):
    if text.find(word):
        return True
    else:
        return False

# Programa:
frase = input('\nDigite uma frase: ').strip()
palavra = input('\nDigite uma palavra: ')
print()
print(Procura(frase, palavra), "\n")


# 9. Faça uma função que receba uma string que contém tanto números quanto letras e caracteres especiais, e que separe as letras em uma
# variável e os números em outra (os caracteres especiais podem ser descartados). Ao final a função deve imprimir as duas variáveis.

import random
import string

def Separa(lista):
    letras = []
    numeros = []
    especiais = []
    
    for i in lista:
        if i.isdigit():
            numeros.append(i)
        elif i.isalpha():
            letras += i
        else:
            especiais += i

    print("\nLetras:", ' '.join(letras))
    print("\nNúmeros:", ' '.join(numeros), "\n")
    return letras, numeros, especiais

mix = list
let = list (string.ascii_lowercase)
num = list (random.sample(range(0, 101), 10))
esp = [':','?','!',';','@','#','$','%','&','*','<','>','+','-']

for i in range(len(num)): ## Transforma cada número em uma string
    num[i] = str(num[i])

mix = let + num + esp
random.shuffle(mix) ## Mistura as três listas

print(f"\nMistura: {mix}")

Separa(mix)

#! Refazer
# Desafio 1. Faça uma função que receba uma string e uma letra e:
#    a. imprima quantas vezes a letra aparece na string;
#    b. imprima todas as posições em que a letra aparece na string;
#    c. retorne a distância entre a primeira e a última aparição dessa letra na string.

import random

def String_Letter(string, letra):
    contador = 0
    posicao = []
    for i in range(len(string)):
        if string[i] == letra:
            contador += 1
            posicao.append(i)

    if posicao == []: 
        print(letra, "não está na String.")
        return -1 

    print(letra, "apareceu", contador, "vezes na String\n")
    print("As posições são", posicao, "\n")
    return posicao[-1] - posicao[0]


# Programa:
frase=''
for i in range(33):
    frase += '%c' % random.randint(97,122)

letter = random.choice(frase)
lista_string = list(frase)

print("\nLISTA: ", lista_string, "\n")
print("LETRA: ", letter, "\n")

String_Letter(lista_string, letter)


# 2. Super Desafio! - faça uma função que criptografa uma mensagem substituindo cada letra pela letra oposta do dicionário:
#    'a' por 'z'
#    'b' por 'y'
#    'c' por 'x'

import random

entrada = 'abcdefghijklmnopqrstuvwxyz'
saida   = 'zyxwvutsrqponmlkjihgfedcba'

def cifra(texto):
    tabela = str.maketrans(entrada,saida)
    return texto.translate(tabela)

# Programa:
string = ''
for i in range(20):
    string += '%c' % random.randint(97,122)  #- Cria uma string 
print()
print("STRING:", string, '\n')
print("CRIPTOGRAFIA:", cifra(string), '\n')






