from db import _executar

class Produto:
    def __init__(self, nome, preco, id = None, status = 1):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.status = status

        query = "CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco REAL, status NUMERIC)"
        _executar(query)

    def salvar(self):
        query = f"INSERT INTO produtos (nome, preco, status) VALUES ('{self.nome}', '{float(self.preco)}', '{self.status}')"
        _executar(query)

    def atualizar(self):
        query = f"UPDATE produtos SET status = {self.status} WHERE id={(int(self.id))}"
        _executar(query)

    def deletar(self):
        query = f"DELETE FROM produtos WHERE id={(int(self.id))}"
        _executar(query)

    @staticmethod
    def get_produtos():
        query = "SELECT id, nome, preco, status FROM produtos"
        produtos_db = _executar(query)

        if not produtos_db:
            return []

        produtos = []
        for produto in produtos_db:
            produtos.append(Produto(id=produto[0], nome=produto[1], preco=produto[2], status=produto[3]))

        return produtos

    
    @staticmethod
    def get_produto(id):
        query = f"SELECT id, nome, preco, status FROM produtos WHERE id = {id}"
        produtos = _executar(query)
        if not produtos:
            return None

        produto_db = produtos[0]
        return Produto(id=produto_db[0], nome=produto_db[1], preco=produto_db[2], status=produto_db[3])