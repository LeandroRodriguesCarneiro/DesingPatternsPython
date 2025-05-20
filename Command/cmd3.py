from abc import ABCMeta, abstractmethod

#Comand
class Ordem(metaclass=ABCMeta):
    
    @abstractmethod
    def executar(self):
        pass

#ComandoConcreto
class OrdemCompra(Ordem):

    def __init__(self, acao):
        self.acao = acao

    def executar(self):
        self.acao.comprar()

#ComandoConcreto
class OrdemVenda(Ordem):

    def __init__(self, acao):
        self.acao = acao

    def executar(self):
        self.acao.vender()

#Receiver
class Acao:
    def comprar(self):
        print('Voce ira comprar acoes...')

    def vender(self):
        print('Voce ira vender acoes...')


#Invoker
class Agente:
    def __init__(self):
        self.__fila_ordens = []

    def adicionar_ordem_na_fila(self, ordem):
        self.__fila_ordens.append(ordem)
        ordem.executar()


if __name__ == '__main__':
    #Cliente
    acao = Acao()
    ordem_compra = OrdemCompra(acao)
    oredem_venda = OrdemVenda(acao)

    #Chamador/Invoker
    agente = Agente()
    agente.adicionar_ordem_na_fila(ordem_compra)
    agente.adicionar_ordem_na_fila(oredem_venda)