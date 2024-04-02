'''Considere as relações abaixo:

Pessoa (id_pessoa, nome, id_cidade)
Cidade (id_cidade, nome, estado)
Defina também as relações Telefone e Email. Com base nisso, crie um código python que implemente essas relações e define uma função que retorne uma pessoa por linha com todos os seus dados associados.

Considere os conceitos de dict, list e def para elaborar sua solução.

! IMPORTANTE: Não utilize LLM para auxiliar com esse código. O exercício é focado no desenvolvimento da sua capacidade lógica e construtiva para elaborar a solução.'''

class Pessoa:
    def __init__(self, id_pessoa, nome, id_cidade):
        self.id_pessoa = id_pessoa
        self.nome = nome
        self.id_cidade = id_cidade

    def printar_pessoa(self):
        print(self.id_pessoa, self.nome, self.id_cidade)

class Cidade:
    def __init__(self, id_cidade, nome, estado):
        self.id_cidade = id_cidade
        self.nome = nome
        self.estado = estado

class Telefone:
    def __init__(self, id_pessoa, numero):
        self.id_pessoa = id_pessoa
        self.numero = numero

class Email:
    def __init__(self, id_pessoa, email):
        self.id_pessoa = id_pessoa
        self.email = email

banco_pessoas = []

lista_temp = [Pessoa(1, 'Amaral', 1), Cidade(1, 'Jacareí', 'SP'), Telefone(1, '991992993994'), Email(1, 'marra@gmail.com')]
banco_pessoas.append(lista_temp)

lista_temp = [Pessoa(2, 'Bryan', 1), Cidade(2, 'São Paulo', 'SP'), Telefone(2, '3333333'), Email(2, 'teste@gmail.com')]
banco_pessoas.append(lista_temp)

lista_temp = [Pessoa(3, 'Kevin', 2), Cidade(3, 'São José dos Campos', 'SP'), Telefone(3, '9444444'), Email(3, 'mtes@gmail.com')]
banco_pessoas.append(lista_temp)

lista_temp = [Pessoa(4, 'Edward', 1), Cidade(4, 'Santa Branca', 'SP'), Telefone(4, '99155555993994'), Email(4, 'medwar@gmail.com')]
banco_pessoas.append(lista_temp)

nomeUsuario = input('Digite o nome para a busca: ')
for Pessoa in range(len(banco_pessoas)):
    if (banco_pessoas[Pessoa][0].nome == nomeUsuario):
        temp_cidade = banco_pessoas[Pessoa][0].id_cidade
        temp_pessoa = banco_pessoas[Pessoa][0].id_pessoa
        print("foi")

for Pessoa in range(len(banco_pessoas)):
    if (banco_pessoas[Pessoa][1].id_cidade == temp_cidade):
        atual_cidade = banco_pessoas[Pessoa][1].nome
        atual_estado = banco_pessoas[Pessoa][1].estado
    if (banco_pessoas[Pessoa][2].id_pessoa == temp_pessoa):
        atual_telefone = banco_pessoas[Pessoa][2].numero
    if (banco_pessoas[Pessoa][3].id_pessoa == temp_pessoa):
        atual_email = banco_pessoas[Pessoa][3].email

print(f'A pessoa {nomeUsuario}, reside em {atual_cidade} - {atual_estado}, possui o telefone {atual_telefone} e seu email é {atual_email}')