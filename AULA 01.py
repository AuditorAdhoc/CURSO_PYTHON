
## VARIÁVEIS, INPUT/OUTPUT ##

# 1. Faça um Programa que mostre a mensagem "Olá, mundo!" na tela.

print("Olá, mundo!\n")


# 2. Faça um programa que peça um número e mostre a mensagem "O número informado foi [número]".

num = input("\nDigite um número: ")
print(f"O número informado foi {num}\n")


# 3. Faça um programa que peça um número para o usuário (string), converta-o para float e depois imprima-o na tela. 
# Você consegue fazer a mesma coisa, porém convertendo para int?

num = input("Digite um número: ")
num_float = float(num) #> Convertendo para float
print(f"O número informado é {num_float}\n")

num = input("Digite um número: ")
num_int = int(num) #> Convertendo para int
print(f"O número informado é {num_int}\n")


# 4. Faça um programa que peça dois números e imprima a soma deles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

print("Soma:", num1 + num2, "\n")


# 5. Faça um programa que peça as 4 notas bimestrais de um aluno e mostre a média aritmética delas.

nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))
nota3 = float(input("Digite a 3° nota: "))
nota4 = float(input("Digite a 4° nota: "))

media = (nota1+nota2+nota3+nota4)/4

print (f"A média é: {media}\n")


# 6. Faça um programa que converta um valor em metros para centímetros.

metros = float(input("Digite um número em metros: "))
print(f"{metros}m em centímetros é: ", metros*100,"cm\n")


# 7. Faça um programa que peça o raio de um círculo, calcule e mostre sua área. Obs: Formula da área de um círculo, A = 3.14*r²  

raio = float(input("Digite o raio de um círculo: "))
print("A área do círculo é:", 3.14*raio*raio, "\n")


# 8. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês e depois, calcule e mostre 
# o total do seu salário no referido mês.

salario = float(input("Quanto você ganha por hora: "))
horas = float(input("Quantas horas você trabalha por mês: "))
print("Seu salário é: ", salario*horas, "\n")


# 9. Faça um programa que peça a temperatura em graus Fahrenheit (F), transforme e mostre a temperatura em graus Celsius (°C). 
# C = (5 * (F-32) / 9).

#> Fahrenheit:
fahrenheit = float(input("Digite a temperatura em graus Farenheit(F): "))
celsius = 5*(fahrenheit-32)/9
print(f"A temperatura {fahrenheit}, em graus Celsius, é: {celsius} \n")

#> Celsius:
celsius = float(input("Digite a temperatura em graus Celsius(C): "))
fahrenheit = celsius*9/5 + 32
print(f"A temperatura {celsius}, em Fahrenheit, é: {fahrenheit} \n")


# 10. Faça um programa que peça o dia, o mês e o ano para o usuário e imprima a data completa no formato dd/mm/aaaa.

dia = int(input("Qual um dia? "))
mes = int(input("Qual um mês? "))
ano = int(input("Qual um ano? "))
print("Data:", dia, "/", mes, "/", ano, "\n")


# 11. Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))
num3 = float(input("Digite um número real: "))

# a)	o produto do dobro do primeiro com metade do segundo.

print("O produto do dobro do primeiro com metade do segundo: ", 2*num1*num2/2, "\n")

# b)	a soma do triplo do primeiro com o terceiro.

print("A soma do triplo do primeiro com o terceiro: ", 3*num1 + num3, "\n")

# c)	o terceiro elevado ao cubo.

print("O terceiro elevado ao cubo: ", num3**3, "\n")


# 12. Faça um programa que peça o peso e altura de uma pessoa e calcule seu IMC (Índice de Massa Corporal).

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em m: '))

print("Seu imc é: ", peso/(altura**2), "\n")


# 13. Faça um programa que peça um valor monetário e aumente-o em 15%. Seu programa deve imprimir a mensagem “O novo valor é R$[valor]”.

valor = float(input("Digite um valor? "))
print("O novo valor é R$",valor*1.15, "\n")

# 14. Faça um programa que peça um valor monetário e diminua-o em 15%. Seu programa deve imprimir a mensagem “O novo valor é R$[valor]”.

valor = float(input("Digite um valor? "))
print("O novo valor é R$",valor*0.85, "\n")


# Desafio 1. Peça para o usuário digitar uma velocidade inicial (em m/s), uma posição inicial (em m) e um instante de tempo (em s) e 
# imprima a posição de um projétil nesse instante de tempo.

v0 = float(input("Digite uma velocidade inicial (em m/s): "))
y0 = float(input("Digite a posição inicial (em m): "))
t = float(input("Digite um instante no tempo (em s): "))
g = -10

y = y0 + v0*t + 0.5*g*t**2

print(f"A posição no instante {t}", "é", y, "\n")

# Desafio 2. 2.	Faça um programa que informe a data e a hora para o usuário. Para isso use a função datetime.now() do módulo datetime.

from datetime import datetime 
agora = datetime.now() 

ano = agora.year
mes = agora.month
dia = agora.day
hora = agora.hour
minuto = agora.minute
segundo = agora.second

print(dia, "/", mes, "/", ano, " ", hora, ":", minuto, ":", segundo, sep="")
print("\n")

#> Outra solução:

agora = datetime.now()
formato = "%d/%m/%Y %H:%M:%S" 
agora_formatado = datetime.strftime(agora,formato) #* A função strftime() formata o texto
print(agora_formatado)
