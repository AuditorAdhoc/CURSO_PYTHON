
## While ##

# 1. Faça um programa que peça ao usuário um número e imprima todos os números de um até o número dado.

num = int(input("\nDigite um número: "))
i = 0
while i < num:
    i += 1
    print(i)


# 2. Peça ao usuário para digitar um número n e some todos os números de 1 a n.

num = int(input("\nDigite um número: "))
i = 0
soma = 0
while i < num:
    i += 1
    soma += i

print(f"A soma de 1 a {num} é {soma}\n")


# 3. Peça ao usuário para digitar um número e imprima o fatorial de n.

num = int(input("\nDigite um número: "))
i = 0
fat = 1

while i < num:
    i += 1
    fat *= i

print(f"O fatorial de {num} é {fat}\n")


# 4. Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.

print("\n# TABUADA DO NOVE #\n")
i = 0
while i < 10:
    i += 1
    print(f"9 x {i} = " + str(i*9))
print("\n")


# 5. 5. Faça um programa que recebe um número inteiro do usuário e imprime na tela a quantidade de divisores desse número e quais são eles.

num = int(input("\nDigite um número: "))
qtd_div = 0
div = 1
while div <= num:
    if num % div == 0:
        print(div, f"é divisor do número {num}")
        qtd_div += 1
    div += 1
print(f"\nO número {num} possui {qtd_div} divisores.\n")


# 6. Faça um programa, usando loops, que peça para um usuário digitar um número e que só finaliza quando o usuário digitar 0. Ao final 
# imprima a soma de todos os números digitados.

num = int(input("\nDigite um número. Se quiser finalizar digite 0: "))
soma = 0
while num != 0:
    soma += num
    num = int(input("Digite um número. Se quiser finalizar digite 0: "))
print(f"A soma é {soma}\n")


# 7. Faça um programa que sorteia um número N e peça para o usuário adivinhar o número sorteado. A cada resposta errada, o seu programa 
# deve imprimir um aviso dizendo que a resposta está errada e pedir novamente uma resposta ao usuário.

import random
sort = random.randint(0, 10) 

num = int(input("\nDigite um número: "))
while num != sort:
    print("Você errou!")
    num = int(input("\nDigite um número: "))
print(f"Você errou! O número sorteado foi {sort}\n")


# 8. Faça um programa que peça para o usuário digitar a idade, o salário e o sexo até que as entradas digitadas sejam válidas

idade = int(input("\nDigite uma idade: "))
while idade < 0 or idade >= 150:
    print("Digite uma idade entre 1 e 150")
    idade = int(input("Digite uma idade: "))

salario = int(input("\nDigite um salário: "))
while salario < 0:
    print("Digite uma idade maior que zero")
    salario = int(input("Digite um salário: "))

sexo = input("\nDigite o sexo (F/M/Outro): ")
while sexo != 'M' and sexo != 'F' and sexo != 'Outro':
    print("Digite F ou M ou Outro")
    sexo = input("Digite o sexo: ")


## Desafios ##

# Desafio 1. Calcule a soma de até mil termos da série 1 + 1/2 + 1/4 + 1/8 + 1/16 + ... 

contador = 0
termo = 1
soma = 1 


while contador < 1000:
    termo /= 2   
    soma += termo 
    contador += 1

print(f"\nA soma é: {soma}\n")


# Desafio 2. Calcule a soma de mil termos dos inversos dos fatoriais: 1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...

# cont == cont
# termo == cont * temo
# cont == 1 -> termo == 1 * 1 = 1 = 1!
# cont == 2 -> termo == 2 * 1! = 2!
# cont == 3 -> termo == 3 * 2! = 3!
# cont == 4 -> termo == 4 * 3! = 4!

contador = 1 
soma = 0
termo = 1

while contador < 1000:
    termo /= contador #> Se dividirmos pelo contador, formamos o fatorial até aquele termo
    soma += termo 
    contador += 1

print(f"A soma é: {soma}\n")

#* A solução do desafio 2 é mais eficiente, porém é possível usar uma função do math

from math import factorial


print(factorial(4))

