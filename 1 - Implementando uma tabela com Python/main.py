''' Com base nos conceitos iniciais de banco de dados apresentados em sala, crie um código python que atenda aos seguintes requisitos:

Implemente uma tabela Aluno com os atributos id, nome e idade;
Implemente a operação de inserção de dados e popule a tabela com 10 registros; e
Implemente a recuperação de informação por meio do id do aluno.
Envie o código executável Python em zip para esse exercícios. Adicione um arquivo README.md com a descrição do projeto. '''

# Classe aluno com id, nome e idade usando construtor

class Aluno:
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

# lista com nome Turma, onde será armezada os alunos

Turma1 = []

# inserindo 10 variaveis fixas do tipo classe Aluno, utilizando .append

Turma1.append(Aluno(id=1, nome="Amaral", idade=20))
Turma1.append(Aluno(id=2, nome="Bryan", idade=21))
Turma1.append(Aluno(id=3, nome="Edward", idade=22))
Turma1.append(Aluno(id=4, nome="Fernando", idade=25))
Turma1.append(Aluno(id=5, nome="Luiz", idade=24))
Turma1.append(Aluno(id=6, nome="João", idade=23))
Turma1.append(Aluno(id=7, nome="Hugo", idade=22))
Turma1.append(Aluno(id=8, nome="Isabela", idade=24))
Turma1.append(Aluno(id=9, nome="Ana", idade=32))
Turma1.append(Aluno(id=10, nome="Maria", idade=30))

def display_menu():
    print("1 - Mostre a tabela pré definida")
    print("2 - Adicionar Aluno")
    print("3 - Pesquisa pelo ID")
    print("4 - Fechar programa")

def opcao1():
# printando para cada Aluno dentro da lista Turma
    for Aluno in Turma1:
        print(f"ID: {Aluno.id}, Nome: {Aluno.nome}, Idade: {Aluno.idade}")
    print('\n\n')

def opcao2():
    Turma1.append(Aluno(int(input('ID:')),input('NOME:'),int(input('IDADE:'))))
    print('\n\n')
    print('ALUNO INSERIDO COM SUCESSO. TABELA ATUALIZADA: ')
    opcao1()

def opcao3():
    print('\n\n')
    entrada_id = int(input('Digite o ID do aluno procurado: '))

    for i in range(len(Turma1)):
        if Turma1[i].id == entrada_id:
            print(f"ID: {Turma1[i].id}, Nome: {Turma1[i].nome}, Idade: {Turma1[i].idade}")

    
while True:
    display_menu()
    entrada_usuario = input("Insira um número (1-4): ")

    if entrada_usuario == '1':
        opcao1()
    elif entrada_usuario == '2':
        opcao2()
    elif entrada_usuario == '3':
        opcao3()
    elif entrada_usuario == '4':
        print("Programa fechado com sucesso")
        break
    else:
        print("Número inválido. Insira um número de 1 a 4.")