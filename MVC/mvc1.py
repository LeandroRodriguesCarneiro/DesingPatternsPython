class Model:
    def __init__(self):
        self.produtos = {
            'ps5': {'id': 1, 'nome': 'Playsstation 5', 'preco':1244},
            'xbox': {'id': 2, 'nome': 'Xbox 360', 'preco':1445},
            'Wii': {'id': 3, 'nome': 'NIntendo Wii', 'preco':1567},
        }

class Controller:
    def __init__(self):
        self.modelo = Model()

    def listar_produtos(self):
        produtos = self.modelo.produtos.keys()

        print('--------------PRODUTOS--------------')
        for chave in produtos:
            print(f'ID: {self.modelo.produtos[chave]["id"]}')
            print(f'NOME: {self.modelo.produtos[chave]["nome"]}')
            print(f'PREÇO: {self.modelo.produtos[chave]["preco"]}')
            print()

class View:
    def __init__(self):
        self.controlador = Controller()

    def produtos(self):
        self.controlador.listar_produtos()


if __name__ == '__main__':
    visao = View()
    visao.produtos()