
## Estruturas Condicionais ##

# 1. Faça um programa que peça a idade do usuário e imprima se ele é maior ou menor de 18 anos.

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade!\n")
else:
    print("Você é menor de idade!\n")


# 2. Faça um programa que peça um número e mostre se ele é positivo ou negativo.

num = int(input("Digite um número: "))
if num > 0:
    print("Número positivo!\n")
elif num == 0:
    print("ZERO")
else:
    print("Número negativo!\n")


# 3. Faça um programa que dado um número digitado, mostre se ele é Par ou Ímpar.

num = int(input("Digite um número: "))
if num % 2 == 0: #* Se o resto da divisão for igual a zero, então é par.
    print(f"O número {num} é Par!\n")
else:
    print(f"O número {num} é Ímpar\n")
    

# 4. Faça um programa que peça dois números e mostre o maior deles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
if num1 > num2:
    print(f"O maior entre {num1} e {num2} é:" , num1, "\n")
elif num2 > num1:
    print(f"O maior entre {num2} e {num1} é:" , num2, "\n")
else:
    print(f"Os números {num2} e {num1} são iguais!", "\n")


# 5. Faça um programa que leia a validade das informações:

# a.Idade: entre 0 e 150:

idade = int(input("Digite uma idade: "))
if idade >= 0 and idade <= 150:
    print("A idade entre 0 e 150 está OK!", "\n")
else:
    print("Digite uma idade entre 0 e 150", "\n")

# b.Salario: maior que 0:

salario = float(input("Digite um salário: "))
if salario > 0:
    print("Valor correto!", "\n")
else:
    print("O salário deve ser maior que ZERO!", "\n")

# c.Sexo: M ou F:

sexo = input("Digite um sexo (F/M): ")
if sexo == 'F' or sexo == 'M':
    print("Sexo correto!", "\n")
else:
    print("O sexo deve ser F ou M!", "\n")


# 6. Escreva um programa que peça a nota de 3 provas de um aluno e verifique se ele passou ou não de ano.

nota1 = int(input("Digite a 1° Nota: "))
nota2 = int(input("Digite a 2° Nota: "))
nota3 = int(input("Digite a 3° Nota: "))

media = (nota1 + nota2 + nota3)/3

if media >= 6:
    print("O Aluno foi aprovado!\n")
else:
    print("O Aluno foi reprovado!\n")


# 7. Faça um programa que mostre uma questão de múltipla escolha com 5 opções (letras a, b, c, d, e e).

print("A linguagem Python:\n")
print("a. foi criada em 1991 por Guido Van Rossum.")
print("b. é uma das linguagens de programação mais difíceis de aprender.")
print("c. é uma linguagem de programação de baixo nível.")
print("d. tem uma sintaxe de programação pouco intuitiva e muito confusa para o programador.")
print("e. a maioria das bibliotecas disponibilizadas não são open source.\n")

opcao = input("Digite a opção correta: ")
if opcao == 'A' or opcao == 'a':
    print("Resposta Correta!\n")
else:
    print("Resposta Incorreta!\n")


# 8. Vamos fazer um programa para verificar quem é o assassino de um crime.

print("\nDigite Sim ou Não: \n")
q1 = input("Mora perto da vítima? ")
q2 = input("Já trabalhou com a vítima? ")
q3 = input("Telefonou para a vítima? ")
q4 = input("Esteve no local do crime? ")
q5 = input("Devia para a vítima? ")

pontos = 0

if q1 == "Sim" or q1 == "SIM":
    pontos = pontos + 1
if q2 == "Sim" or q2 == "SIM":
    pontos = pontos + 1
if q3 == "Sim" or q3 == "SIM":
    pontos = pontos + 1
if q4 == "Sim" or q4 == "SIM":
    pontos = pontos + 1
if q5 == "Sim" or q5 == "SIM":
    pontos = pontos + 1


if pontos == 5:
    print("Você é o assassino!\n")
elif 3 <= pontos <= 4:
    print("Você é cúmplice!\n")
elif pontos == 2:
    print("Você é suspeito!\n")
else:
    print("Você está liberado!\n")


# 9. Um produto vai sofrer aumento de acordo com as tabelas na lista de exercicios.

preco = float(input("Digite o valor do produto de acordo com o preço antigo: "))

if preco < 50:
    preco_novo = preco * 1.05
elif 50 <= preco < 100:
    preco_novo = preco * 1.1
elif 100 <= preco < 150:
    preco_novo = preco * 1.13
else:
    preco_novo = preco * 1.15

if preco_novo <= 80:
    print("Barato")
elif preco_novo <= 115:
    print("Razoável")
elif preco_novo <= 150:
    print("Normal")
elif preco_novo <= 170:
    print("Caro")
else:
    print("Muito caro")


# Desafio 1. Faça um programa que leia 3 números e informe o maior deles.

num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))
num3 = int(input("Digite o 3° número: "))

if num1 > num2:
    if num1 > num3:
        print(num1, "é o maior dos três!\n")
    else:
        print(num3, "é o maior dos três!\n")
else:
    if num2 > num3:
        print(num2, "é o maior dos três!\n")
    else:
        print(num3, "é o maior dos três!\n")


# Desafio 2. Faça o mesmo programa do exercício anterior, porém com 4 números.

num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))
num3 = int(input("Digite o 3° número: "))
num4 = int(input("Digite o 4° número: "))

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num4 > maior:
    maior = num4

print("\nO maior é dos quatro é:", maior)


# Desafio 3. Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um questionário de sintomas.

a = input("Sente dor no corpo? ")
b = input("Você tem febre? ")
c = input("Você tem tosse? ")
d = input("Está com congestão nasal? ")
e = input("Tem manchas pelo corpo? ")

if b == 'Não' and c == 'Não' and d == 'Não' and e == 'Não':
    print("Sem doenças")
elif b == 'Sim' and c == 'Sim' and d == 'Sim' and e == 'Não':
    print("Gripe")
elif a == 'Sim' and b == 'Sim' and c == 'Não' and d == 'Não' and e == 'Sim':
    print("Dengue")
else:
    print("VIROSE! rs")

