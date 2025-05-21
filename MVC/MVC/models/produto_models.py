from db import _executar

class Produto:
    def __init__(self, nome, preco, id = None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.status = 1

        query = "CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco REAL, status NUMERIC)"
        _executar(query)

    def salvar(self):
        query = f"INSERT INTO produtos (nome, preco, status) VALUES ('{self.nome}', '{float(self.preco)}', '{self.status}')"
        _executar(query)

    def atualizar(self):
        query = f"UPDATE produtos SET status SET status = '{self.status}', WHERE id={(int(self.id))}"
        _executar(query)