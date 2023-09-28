class Aluno:
    def __init__(self, nome, email, curso):
        self.nome = nome
        self.email = email
        self.curso = curso
        self.presenca = 0
        self.notas = []
        self.media = 0

    def saudacao(self):
        print("Olá, {}! Seja bem-vindo ao curso de {}!". format(self.nome, self.curso))
    
    def adicionarNota(self, nota):
        self.notas.append(nota)

    def calcularMedia(self):
        if len(self.notas) != 0:
            self.media = sum(self.notas) / len(self.notas)
    
    def adicionarPresenca(self):
        self.presenca = self.presenca + 1

#* Instanciando um objeto
aluno1 = Aluno("W", "W", "A")

print(aluno1.presenca)

aluno1.adicionarPresenca()
print(aluno1.presenca)

alunos = []

for i in range(3):
    print("CADASTRO DO ALUNO {}:\n".format(i + 1))

    nome = input("Nome: ")
    email = input("E-mail: ")

