
## CLASSES E OBJETOS ##

# 1. Crie uma classe Bola cujos atributos são cor e raio. Crie um método para calcular a área dessa bola (obs. a área de uma esfera é 
# 4*3.14*r*r/3). Crie um método que imprime a cor da bola.. Crie um método para calcular o volume da bola (obs. o volume de uma esfera 
# é 4*3.14*r*r*r). Crie um objeto dessa classe e calcule a área e o volume, imprimindo ambos em seguida.

class Bola: 
    def __init__(self, raio, cor): #? Método construtor
        self.raio = raio #? Criando um atributo
        self.cor = cor

    #? Métodos
    def area(self): #? Criando um método para calcular a área
        return (4/3)*3.14*self.raio**2

    def imprime(self): #? Criando um método para imprimir a cor
        return self.cor

    def volume(self): #? Criando um método para calcular o volume
        return 4*3.14*self.raio**3

#? Usando a classe Bola:
radius = int(input("\nEntre com o valor do raio da bola: "))
color = input("Entre com a cor da bola: ")

bola = Bola(radius,color)

print("\nÁrea: ", bola.area())
print("Volume: ", bola.volume())
print("Cor: ", bola.imprime(), "\n")


# 2. Crie uma classe Retangulo cujos atributos são lado_a e lado_b. Crie um método para calcular a área desse retângulo. Crie um objeto 
# dessa classe e calcule a área e a imprima em seguida.

import random

class Retangulo:
    def __init__(self, a, b):
        self.lado_a = a #? Criando um atributo
        self.lado_b = b #? Criando um atributo
    def area(self):
        return self.lado_a*self.lado_b

#? Usando a classe Retangulo:
la = random.randint(1, 10)
lb = random.randint(1, 10)

retangulo = Retangulo(la,lb)

print("\nLado a: ", la)
print("Lado b: ", lb)
print("\nÁrea do retângulo: ", retangulo.area(), "\n")


# 3. Crie uma classe Cliente cujos atributos são nome, idade e e-mail. Construa um método que imprima as informações tal como abaixo:
# Nome: Fulano de Tal
# Idade: 40
# E-mail: fulano@mail.com

class Cliente:
    def __init__(self, name, age, email):
        self.nome = name
        self.idade = age
        self.email = email

    def imprime_cadastro(self):
        print("\nNome:", self.nome, "\nIdade:", self.idade, "\nE-mail:", self.email, "\n")

#? Usando a classe Cliente:
n = input("\nDigite o nome do Cliente: ")
i = input("Digite a idade do Cliente: ")
e = input("Digite a e-mail do Cliente: ")

cliente = Cliente(n, i, e)
cliente.imprime_cadastro()


# 4. Com base no exercício anterior, crie um sistema de cadastro com dicionários e a classe Cliente; cada cliente deve ter como chave o 
# seu CPF. Seu programa deve perguntar se o usuário quer cadastrar um novo cliente, alterar um cadastro ou sair.
# Dica: Você pode fazer esse exercício criando uma classe Sistema, que irá controlar o sistema de cadastros. Essa classe deve ter o 
# atributo cadastro e os métodos para imprimir os cadastrados, cadastrar um novo cliente, alterar um cadastro ou sair.

class Cliente:
    def __init__(self, name, age, email, cpf):
        self.nome = name
        self.idade = age
        self.email = email
        self.cpf = cpf
        
    def imprime_cadastro(self):
          print("\nNome:", self.nome, "\nIdade:", self.idade, "\nE-mail:", self.email, "\n", "\nCPF:", self.cpf)

class Sistema:
    def __init__(self):
        self.cadastrados = {}

    def cadastrar_novo(self):
        n = input("Digite o nome do Cliente: ")
        i = int(input("Digite a idade do Cliente: "))
        e = input("Digite o email do Cliente: ")
        cpf = input("Digite o CPF do Cliente: ")
        novo_cliente = Cliente(n, i, e, cpf)
        self.cadastrados[cpf] = novo_cliente

    def visualizar_cadastros(self):
        for cpf_cliente in self.cadastrados:
            self.cadastrados[cpf_cliente].imprime_cadastro()
            print('=========================')

    def alterar_cadastro(self, cpf):
        cliente = self.cadastrados.pop(cpf) # obtém o valor da chave e remove o valor do dicionário
        alteracao = input('O que deseja alterar?')

        while alteracao not in ('nome', 'idade', 'email','cpf'):
             input('Erro. Digite novamente o que deseja alterar?')
        if alteracao == 'nome':
            novo_nome = input("Digite um novo nome: ")
            cliente.nome = novo_nome
        if alteracao == 'idade':
            nova_idade = int(input("Digite uma nova idade: "))
            cliente.idade = nova_idade
        if alteracao == 'email':
            novo_email = input("Digite um novo e-mail: ")
            cliente.email = novo_email
        if alteracao == 'cpf':
            novo_cpf = input("Digite um novo CPF: ")
            cliente.cpf = novo_cpf
        self.cadastrados[cliente.cpf] = cliente

    def run(self):
        o_que_fazer = 1
        while o_que_fazer != 0:
            if o_que_fazer == 1:
                print("\n===Novo Cadastro===\n")
                self.cadastrar_novo()
                print('\n===Fim do cadastro===\n')
            elif o_que_fazer == 2:
                print('===Visualização dos Cadastrados===')
                self.visualizar_cadastros()
                print('\n===Fim da visualização===\n')
            elif o_que_fazer == 3:
                print('===Alteração de Cadastro===\n') 
                cpf_a_alterar = input("Digite o CPF a ser alterado: ")
                while cpf_a_alterar not in self.cadastrados:
                    cpf_a_alterar = input("CPF não encontrado. Digite novamente: ")
                self.alterar_cadastro(cpf_a_alterar)
                print('\n===Fim da alteração===\n')
            o_que_fazer = int(input(
                "===O que deseja fazer?===\n" "\n Digite 0 para Sair!" "\n Digite 1 para Novo Cadastro!" "\n Digite 2 para Visualização dos Cadastrados!" "\n Digite 3 para Alteração de Cadastro!\n"))
        print('===Fim===')    

#? Usando a classe Sistema e rodando:
sistema = Sistema()
sistema.run()


# 5.  Crie uma classe Funcionario cujos atributos são nome e e-mail. Guarde as horas trabalhadas em um dicionário cujas chaves são o mês 
# em questão e, em outro dicionário, guarde o salário por hora relativo ao mês em questão. Crie um método que retorna o salário mensal do 
# funcionário.

class Funcionario:
    def __init__(self, name, email):
        self.nome = name
        self.email = email
        self.horas = {}
        self.salario_hora = {}

    def salario_func(self, mes):
        return self.horas[mes]*self.salario_hora[mes]

#? Usando a classe Funcionário:
n = input("\nDigite o nome do Funcionário: ")
e = input("Digite o e-mail do Funcionário: ")
mes = input("Digite o mês trabalhado (XX/2020): ")
func = Funcionario(n, e)
func.horas[mes] = float(input("Digite a qtd de horas trabalhadas no mês: "))
func.salario_hora[mes] = float(input("Digite o valor do salário por hora: "))
print(f"\nO salário do mês {mes} do funcionário {n} foi:", func.salario_func(mes), "\n")


# 6. Crie uma classe ContaCorrente com os atributos cliente (que deve ser um objeto da classe Cliente) e saldo. Crie métodos para depósito, 
# saque e transferência. Os métodos de saque e transferência devem verificar se é possível realizar a transação.

class Cliente:
    def __init__(self, name, age, email, cpf):
        self.nome = name
        self.idade = age
        self.email = email
        self.cpf = cpf

    def imprime_cadastro(self):
        print("\nNome:", self.nome, "\nIdade:", self.idade, "\nE-mail:", self.email, "\nCPF:", self.cpf)

class ContaCorrente:
    def __init__(self, client, balance = 0):
        self.cliente = client
        self.saldo = balance

    def deposito(self, value):
        self.saldo += value

    def saque(self, value):
        if self.saldo - value >= 0:
            self.saldo -= value
        else:
            print('Saldo insuficiente!')

    def transferencia(self, other, value):
        if self.saldo - value >= 0:
            self.saldo -= value
            other.saldo += value
        else:
            print('Saldo insuficiente!')

#* Usando a classe Cliente:
n = input("\nDigite o nome do Cliente: ")
i = input("Digite a idade do Cliente: ")
e = input("Digite a e-mail do Cliente: ")
cpf = input("Digite a cpf do Cliente: ")

#* Criando e imprimindo dois Clientes:
clienteA = Cliente(n, i, e, cpf)
clienteA.imprime_cadastro()

clienteB = Cliente(n, i, e, cpf) #! O cliente B foi criando assim apenas para testar a classe ContaCorrente
clienteB.imprime_cadastro()

#* Creditando na conta corrente dos Clientes:
conta_clienteA = ContaCorrente(clienteA, 5000)
conta_clienteB = ContaCorrente(clienteB, 3000) #? Conta crianda apenas para transfência entre contas.

#* Saldo
print(f"\n===Conta do {n}===")
print("Saldo:",conta_clienteA.saldo)

#* Sacar
conta_clienteA.saque(300)
print("\n===Saque====")
print("Saldo:",conta_clienteA.saldo)

#* Depositar
conta_clienteA.deposito(1000)
print("\n===Depósito===")
print("Saldo:",conta_clienteA.saldo)

#* Transferir
conta_clienteB.transferencia(conta_clienteA, 300) #? Transfere 300 reais da conta do cliente B para cliente A
print("\n===Transferência===")
print("Saldo:",conta_clienteA.saldo)

#* Saldo da conta B
print("\n===Conta do Cliente B===")
print("Saldo:",conta_clienteB.saldo, "\n")


# 7. Crie uma classe Televisor cujos atributos são:
# fabricante;
# modelo;
# canal atual
# lista de canais; e 
# volume.

# Faça métodos aumentar/diminuir volume, trocar o canal e sintonizar um novo canal, que adiciona um novo canal à lista de canais (somente 
# se esse canal não estiver nessa lista). No atributo lista de canais, devem estar armazenados todos os canais já sintonizados dessa TV. 
# Obs. o volume não pode ser menor que zero e maior que cem; só se pode trocar para um canal que já esteja na lista de canais.

# 8. Crie uma classe ControleRemoto cujo atributo é televisão (isso é, recebe um objeto da classe do exercício 7). Crie 
# métodos para aumentar/diminuir volume, trocar o canal e sintonizar um novo canal, que adiciona um novo canal à lista de canais 
# (somente se esse canal não estiver nessa lista).

class Televisor:
    def __init__(self, maker, model):
        self.fabricante = maker
        self.modelo = model
        self.canal_atual = None
        self.lista_de_canais = []
        self.volume = 50

    def aumentarVolume(self, sound):
        if self.volume + sound <= 100:
            self.volume += sound
        else:
            self.volume = 100

    def diminuirVolume(self, sound):
        if self.volume - sound >= 0:
            self.volume -= sound
        else:
            self.volume = 0
    
    def trocarCanal(self, channel):
        if channel in self.lista_de_canais:
            self.canal_atual = channel

    def sintonizarNovoCanal(self, channel):
        if channel not in self.lista_de_canais:
            self.lista_de_canais.append(channel)

class ControleRemoto:
    def __init__(self, tv):
        self.televisao = tv
    
    def aumentarVolume(self):
        self.televisao.aumentarVolume(15)

    def diminuirVolume(self):
        self.televisao.diminuirVolume(10)

    def trocarCanal(self, channel):
        self.televisao.trocarCanal(channel)

    def sintonizarCanal(self, channel):
        self.televisao.sintonizarNovoCanal(channel)

#* Usando a classe Televisor:
maker = input("\nDigite a fabricante da TV: ")
model = input("Digite o modelo da TV: ")

tv = Televisor(maker, model)
control = ControleRemoto(tv)

print("\nFabricante: ", maker, "\nModelo: ", model)
print("\nVolume atual da TV: ", tv.volume)
control.aumentarVolume()
print("\nApós aumentar o volume: ", tv.volume)
control.diminuirVolume()
print("Após diminuir o volume: ", tv.volume, "\n")
     

# 9. O módulo time possui a função time.sleep(x), que faz seu programa “dormir” por x segundos. Utilizando essa função, crie uma classe 
# Cronômetro e faça um programa que cronometre o tempo.

import time

class Cronometro:
    def __init__(self, second = 0, minutes = 0, hours = 0):
        self.segundos = second
        self.minutos = minutes
        self.horas = hours

    def __repr__(self):
        horas = "%.2d:%.2d:%.2d" %(self.horas, self.minutos, self.segundos)
        return horas

    def incremento(self):
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1
        self.segundos += 1

    def run(self):
        while True:
            print(100*'\n') # "limpar a shell". Não funciona no Jupyter!
            print(self)
            self.incremento()
            time.sleep(1)

cronometro1 = Cronometro()
cronometro1.run()

# Outra solução:

import time

class Cronometro:
    def __init__(self):
        self.segundos = 0
        self.minutos = 0
        self.horas = 0
    
    def __repr__(self):
        return f"Cronômetro: {self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}"

    def incremento(self):
        self.segundos += 1

        if self.segundos == 60:
            self.minutos += 1
            self.segundo += 0

        if self.minutos == 60:
            self.minutos += 0
            self.horas += 1
    
    def run(self):
        print("\nIniciando o Cronômetro:\n")
        while True:
            self.incremento()
            print(self, end="\r")
            time.sleep(1)
    
cron = Cronometro()
cron.run()


# 10. Crie uma modelagem orientada a objetos para uma agenda capaz de armazenar contatos. Através dessa agenda é possível incluir, remover, 
# buscar e listar contatos já cadastrados. Dica: siga o modelo do exercício 4.

class Contatos:
    def __init__(self, name, telefone):
        self.nome = name
        self.telefone = telefone

    def visualizar(self):
        print(
            "Nome:", self.nome,
            "\nTelefone:", self.telefone,
        )

class Agenda:
    def __init__(self):
        self.contatos = {}

    def cadastrar(self):
        name = input("Digite um nome: ")
        telefone = int(input("Digite um telefone: "))
        novo = Contatos(name, telefone)
        self.contatos[name] = novo

    def imprimir(self):
        for name in self.contatos:
            self.contatos[name].visualizar()
            print('---------------')

    def alterar(self, name):
        contato = self.contatos.pop(name)
        alteracao = input('O que deseja alterar? (nome, telefone)')
        while alteracao not in ('nome', 'telefone'):
             input('Erro. Digite novamente o que deseja alterar?')
        if alteracao == 'nome':
            novo_nome = input("Digite o novo nome: ")
            contato.nome = novo_nome
        if alteracao == 'telefone':
            novo_telefone = int(input("Digite o novo telefone: "))
            contato.telefone = novo_telefone
        self.contatos[contato.name] = contato

    def run(self):
        digito = 1
        while digito != 0:
            if digito == 1:
                print("===Novo Contato===\n")
                self.cadastrar()
                print('\n===Fim do cadastro===\n')
            elif digito == 2:
                print('===Visualização dos Contatos===\n')
                self.imprimir()
                print('\n===Fim da visualização===\n')
            elif digito == 3:
                print('===Alteração de Contato===\n') 
                email_a_alterar = input("Digite o e-mail do contato a ser alterado: ")
                while email_a_alterar not in self.contatos:
                    email_a_alterar = input("E-mail não encontrado. Digite novamente: ")
                self.alterar(email_a_alterar)
                print('\n===Fim da alteração===\n')
            digito = int(input(
            "O que deseja fazer?"
            "\n1 - Cadastrar Novo Contato"
            "\n2 - Visualizar Contatos "
            "\n3 - Alteração de Contato"
            "\n0 - Sair\n"
            ))
            
        print('===Fim===') 

# # Exemplo de Uso:

agenda = Agenda()
agenda.run()
 