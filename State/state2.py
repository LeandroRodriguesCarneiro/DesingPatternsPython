from abc import ABCMeta

class EstadoComputador(metaclass=ABCMeta):
    nome = 'estado'
    permitido = []

    def mudar(self, estado):
        if estado.nome in self.permitido:
            print(f'Atual: {self} => mudado para um novo estado: {estado.nome}')
            self.__class__ = estado.__class__
        else:
            print(f'Atual: {self} => nao e possivel mudar para: {estado.nome}')

    def __str__(self):
        return self.nome
    
class Ligar(EstadoComputador):
    nome = 'Ligar'
    permitido = ['Desligar', 'Suspender', 'Hibernar']

class Desligar(EstadoComputador):
    nome = 'Desligar'
    permitido = ['Ligar']

class Suspender(EstadoComputador):
    nome = 'Suspender'
    permitido = ['Ligar']

class Hibernar(EstadoComputador):
    nome = 'Hibernar'
    permitido = ['Ligar']

class Computador:
    def __init__(self, modelo='Dell'):
        self.modelo = modelo
        self.estado = Desligar()

    def alterar(self, estado):
        self.estado.mudar(estado)

if __name__ == '__main__':
    computador = Computador()
    
    computador.alterar(Ligar())
    computador.alterar(Desligar())
    computador.alterar(Ligar())
    computador.alterar(Suspender())
    computador.alterar(Hibernar())
    computador.alterar(Ligar())
    computador.alterar(Desligar())
