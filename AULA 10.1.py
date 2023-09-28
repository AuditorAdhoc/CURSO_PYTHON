
### MÉTODOS MÁGICOS ##

# 1. Nos exercícios 1,2,3,4 e 6, implemente o método __repr__ para exibir as informações desejadas de cada uma das classes.

### exercício 1

class Bola:
    def __init__(self, raio, cor):
        self.raio = raio
        self.cor = cor
    def __repr__(self):
        texto = "Raio: {}\nCor: {}".format(
            self.raio,
            self.cor
        )
        return texto
    def area(self):
        return (4/3)*pi*self.raio**2
    def volume(self):
        return 4*pi*self.raio**3


### exercício 2

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
    def __repr__(self):
        texto = "Lado A: {}\nLado B: {}".format(
            self.lado_a,
            self.lado_b
        )
        return texto
    def area(self):
        return self.lado_a*self.lado_b

### exercicio 3
#### Já que aprendemos sobre a __repr__, o método visualizar da classe Cliente fica obsoleto.

class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
    def __repr__(self):
        texto  = "Nome: {}\nIdade: {}\nE-mail: {}".format(
            self.nome,
            self.idade,
            self.email
        )
        return texto

### exercicio 4
#### Mudaremos o método visualizar da classe SistemaCadastro também

class SistemaCadastro:
    def __init__(self):
        self.cadastrados = {}
    def cadastrar_novo(self):
        nome = input("Digite o nome do cliente: ")
        idade = int(input("Digite a idade do cliente: "))
        email = input("Digite o email do cliente: ")
        cpf = input("Digite o cpf: ")
        novo_cliente = Cliente(nome, idade, email, cpf)
        self.cadastrados[cpf] = novo_cliente

    def visualizar_cadastros(self):
        for cpf_cliente in self.cadastrados:
            print(self.cadastrados[cpf_cliente])
            print('---------------')
    def alterar_cadastro(self, cpf):
        cliente = self.cadastrados.pop(cpf)
        alteracao = input('O que deseja alterar?')
        while alteracao not in ('nome', 'idade', 'email','cpf'):
             input('Erro. Digite novamente o que deseja alterar?')
        if alteracao == 'nome':
            novo_nome = input("Digite o novo nome: ")
            cliente.nome = novo_nome
        if alteracao == 'idade':
            nova_idade = int(input("Digite a nova idade: "))
            cliente.idade = nova_idade
        if alteracao == 'email':
            novo_email = input("Digite o novo e-mail: ")
            cliente.email = novo_email
        if alteracao == 'cpf':
            novo_cpf = input("Digite o novo CPF: ")
            cliente.cpf[cliente.cpf] = cliente
    def run(self):
        o_que_fazer = 1
        while o_que_fazer != 0:
            if o_que_fazer == 1:
                print("===Novo Cadastro===\n")
                self.cadastrar_novo()
                print('\n===Fim do cadastro===\n')
            elif o_que_fazer == 2:
                print('===Visualização dos Cadastrados===\n')
                self.visualizar_cadastros()
                print('\n===Fim da visualização===\n')
            elif o_que_fazer == 3:
                print('===Alteração de Cadastro===\n') 
                cpf_a_alterar = input("Digite o CPF a ser alterado: ")
                while cpf_a_alterar not in self.cadastrados:
                    cpf_a_alterar = input("CPF não encontrado. Digite novamente: ")
                self.alterar_cadastro(cpf_a_alterar)
                print('\n===Fim da alteração===\n')
            o_que_fazer = int(input("O que deseja fazer?"))
        print('===Fim===')  

### exercício 6
     
class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
    def __repr__(self):
        texto  = "Nome: {}\nIdade: {}\nE-mail: {}".format(
            self.nome,
            self.idade,
            self.email
        )
        return texto
    
class ContaBancaria:
    def __init__(self, cliente, saldo = 0):
        self.cliente = cliente
        self.saldo = saldo
    def __repr__(self):
        texto = self.cliente.__repr__() + "Saldo: {}".format(
            self.saldo
        )
    def saque(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
        else:
            print('Saldo insuficiente.')
    def deposito(self, valor):
        self.saldo += valor
    def transferencia(self, other, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
            other.saldo += valor
        else:
            print('Saldo insuficiente.')


# 2. Crie uma classe Fração cujos atributos são numerador (número de cima) e denominador (número de baixo). Implemente os métodos de 
# adição, subtração, multiplicação, divisão que retornam objetos do tipo Fração. Implemente também o método __repr__. Implemente métodos 
# para comparação: igualdade (==) e desigualdades (!=, <=, >=, < e >).

import random

class Fracao:

    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("O denominador não pode ser 0!")
        self.numerador = numerador
        self.denominador = denominador

    def __repr__(self):
        texto = "{}/{}".format(
            self.numerador,
            self.denominador
        )
        return texto

    def __add__(self, other):
        num = self.numerador*other.denominador +\
        self.denominador*other.numerador
        den = self.denominador*other.denominador
        return Fracao(num, den)

    def __sub__(self, other):
        num = self.numerador*other.denominador -\
        self.denominador*other.numerador
        den = self.denominador*other.denominador 
        return Fracao(num, den)

    def __mul__(self, other):
        num = self.numerador*other.numerador
        den = self.denominador*other.denominador
        return Fracao(num, den)

    def __truediv__(self, other):
        num = self.numerador*other.denominador
        den = self.denominador*other.numerador
        return Fracao(num, den)

    def valor(self):
        return self.numerador/self.denominador

    def __lt__(self,other):
        return self.valor() < other.valor()

    def __le__(self,other):
        return self.valor() <= other.valor()

    def __eq__(self, other):
        return self.valor() == other.valor()

    def __gt__(self, other):
        return self.valor() > other.valor()
        
    def __ge__(self, other):
        return self.valor() >= other.valor()


#? Usando a classe
a = random.randint(1, 10)
b = random.randint(1, 10)

fracaoA = Fracao(a,b)
fracaoB = Fracao(b,a)

print("\nSOMA: {} + {} = {}". format(fracaoA, fracaoB, fracaoA + fracaoB))
print("\nSUBTRAÇÃO: {} - {} = {}". format(fracaoA, fracaoB, fracaoA - fracaoB))
print("\nMULTIPLICAÇÃO: {} * {} = {}". format(fracaoA, fracaoB, fracaoA * fracaoB))
print("\nDIVISÃO: {} / {} = {}". format(fracaoA, fracaoB, fracaoA / fracaoB))
print("\n{} = {}? {}".format(fracaoA, fracaoB, fracaoA == fracaoB))
print("\n{} > {}? {}".format(fracaoA, fracaoB, fracaoA > fracaoB))
print("\n{} > {}? {}".format(fracaoA, fracaoB, fracaoA < fracaoB), "\n")

#3. Crie uma classe Data cujos atributos são dia, mês e ano. Implemente métodos __repr__ e para comparação: igualdade (==) e desigualdades 
# (!=, <=, >=, < e >).

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def __repr__(self):
        return "{}/{}/{}".format(
            self.dia,
            self.mes,
            self.ano
        )
    def __eq__(self, other):
        return self.dia == other.dia and \
                self.mes == other.mes and \
                self.ano == other.ano
    def __neq__(self, other):
        return not self == other
    def __lt__(self, other):
        if self.ano == other.ano:
            if self.mes == other.mes:
                if self.dia == other.dia:
                    return False
                else:
                    return self.dia < other.dia
            else:
                return self.mes < other.mes
        else:
            return self.ano < other.ano
    def __le__(self, other):
        return self < other or self == other
    def __gt__(self, other):
        return not self <= other
    def __ge__(self, other):
        return not self < other


# Exemplo de uso

data1 = Data(25,6,1989)
data2 = Data(1,1,2000)

print(data1 <= data2)


############# HERANÇA #############

# 1. Crie uma classe Quadrado, filha da classe Retângulo do exercício 2

import random

class Retangulo:
    def __init__(self, a, b):
        self.lado_a = a 
        self.lado_b = b
    def area(self):
        return self.lado_a*self.lado_b

class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

#? Usando a classe Quadrado:
lado = random.randint(1, 10)
print("\nLado: ", lado)
quadrado = Quadrado(lado)
print("\nÁrea do Quadrado: ", quadrado.area(), "\n")

    
# 2. Faça uma classe ContaVip que difere da ContaCorrente por ter cheque especial (novo atributo) e é filha da classe ContaCorrente. 
# Você precisa implementar os métodos para saque, transferência ou depósito?

class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
    def __repr__(self):
        texto  = "Nome: {}\nIdade: {}\nE-mail: {}".format(
            self.nome,
            self.idade,
            self.email
        )
        return texto
    
class ContaCorrente:
    def __init__(self, cliente, saldo = 0):
        self.cliente = cliente
        self.saldo = saldo
    def __repr__(self):
        texto = self.cliente.__repr__() + "Saldo: {}".format(
            self.saldo
        )
    def saque(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
        else:
            print('Saldo insuficiente.')
    def deposito(self, valor):
        self.saldo += valor
    def transferencia(self, other, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
            other.saldo += valor
        else:
            print('Saldo insuficiente.')
class ContaVip(ContaCorrente):
    def __init__(self, cliente, saldo, cheque_esp=100):
        super().__init__(cliente, saldo)
        self.cheque_esp = cheque_esp
    def saque(self, valor):
        if self.saldo + limite - valor >= 0:
            self.saldo -= valor
        else:
            print('Saldo insuficiente.')
    def transferencia(self, other, valor):
        if self.saldo + limite - valor >= 0:
            self.saldo -= valor
            other.saldo += valor
        else:
            print("Saldo insuficiente.")
    # não há a necessidade de implementar o depósito