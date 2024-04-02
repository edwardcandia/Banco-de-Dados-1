class Cliente:
    def __init__(self, nome_cliente, endereco, telefone, sabor_favorito):
        self.nome_cliente = nome_cliente
        self.endereco = endereco
        self.telefone = telefone
        self.sabor_favorito = sabor_favorito

    def printar(self):
        print(f'A pessoa {self.nome_cliente}, reside em {self.endereco}, possui o telefone {self.telefone} e seu sabor favorito é {self.sabor_favorito}')

class Pedido:
    def __init__(self, nome_cliente, data_hora, endereco_entrega, avaliacao_cliente, sabores_pedidos):
        self.nome_cliente = nome_cliente
        self.data_hora = data_hora
        self.endereco_entrega = endereco_entrega
        self.avaliacao_cliente = avaliacao_cliente
        self.sabores_pedidos = sabores_pedidos
            
    def printar(self):
        print(f'Nome do cliente: {self.nome_cliente}, data e hora do pedido: {self.data_hora}, endereço de entrega: {self.endereco_entrega}, Sabores escolhidos: {self.sabores_pedidos}')
        

banco_pessoas = []
banco_pedidos = []

banco_pessoas.append(Cliente("João Silva","Rua das Flores, 123","(11)98765-4321","Chocolate"))
banco_pessoas.append(Cliente("Maria Oliveira","Avenida Central, 789","(22)12345-6789",'Baunilha'))
banco_pessoas.append(Cliente('Carlos Santos','Travessa das Palmeiras, 56','(33)55555-5555','Morango'))
banco_pessoas.append(Cliente('Ana Lima','Rua das Acácias, 789','(44)99999-9999','Limão'))
banco_pessoas.append(Cliente('José Santos','Praça da Liberdade, 10','(55) 11111-1111','Abacaxi'))

banco_pedidos.append(Pedido('João Silva','3/13/2024 10:00','Av. Principal, 456','4.5','Chocolate, Morango'))
banco_pedidos.append(Pedido('Maria Oliveira','3/13/2024 12:30','Rua dos Sonhos, 789','4.8','Baunilha, Caramelo'))
banco_pedidos.append(Pedido('Carlos Santos','3/13/2024 15:45','Rua da Praia, 10','4.2','Morango, Limão'))
banco_pedidos.append(Pedido('Ana Lima','3/13/2024 18:00','Av. das Árvores, 23','4.9','Limão, Abacaxi'))
banco_pedidos.append(Pedido('José Santos','3/13/2024 20:15','Rua das Flores, 1','4.6','Abacaxi, Caramelo'))
banco_pedidos.append(Pedido('João Silva','3/14/2024 9:30','Av. Principal, 456','4.7','Chocolate, Baunilha'))
banco_pedidos.append(Pedido('Maria Oliveira','3/14/2024 12:45','Rua dos Sonhos, 789','4.5','Baunilha, Chocolate'))
banco_pedidos.append(Pedido('Carlos Santos','3/14/2024 16:00','Rua da Praia, 10','4.3','Morango, Caramelo'))

while True:

    nomeUsuario = input('Digite o nome para a busca: ')

    for Cliente in banco_pessoas:
        if Cliente.nome_cliente == nomeUsuario:
            print('Foi encontrado:', Cliente.nome_cliente)
            print('Suas informações completas são: ')
            Cliente.printar()
            print('Seus pedidos foram:')
            for Pedido in banco_pedidos:
                if Pedido.nome_cliente == nomeUsuario:
                    Pedido.printar()