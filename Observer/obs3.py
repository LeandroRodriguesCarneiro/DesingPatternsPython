from abc import ABCMeta, abstractmethod

#Assunto/Topico
class AgenciaNoticias:

    def __init__(self):
        self.__inscritos = []
        self.__ultima_noticia = None

    def inscrever(self, inscrito):
        self.__inscritos.append(inscrito)

    def desinscrever(self, inscrito=None):
        if not inscrito:
            return self.__inscritos.pop()
        else:
            return self.__inscritos.remove(inscrito)
        
    def notificar_todos(self):
        for ins in self.__inscritos:
            ins.notificar()
        
    def adicionar_noticia(self, noticia):
        self.__ultima_noticia = noticia

    def mostrar_notia(self):
        return f'Urgente: {self.__ultima_noticia}'
    
    def Inscritos(self):
        return [type(valor).__name__ for valor in self.__inscritos]
#interface Observer
class TipoInscricao(metaclass=ABCMeta):

    @abstractmethod
    def notificar(self):
        pass

# ObservadorA
class InscritosSMS(TipoInscricao):
    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_notia()}')

# ObservadorB
class InscritosEmail(TipoInscricao):
    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_notia()}')

# ObservadorN
class InscritosOutroMeio(TipoInscricao):
    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_notia()}')

#Cliente
if __name__ == '__main__':
    agencia_noticia = AgenciaNoticias()

    InscritosSMS(agencia_noticia)
    InscritosEmail(agencia_noticia)
    InscritosOutroMeio(agencia_noticia)

    print(f'Inscritos: {agencia_noticia.Inscritos()}')

    agencia_noticia.adicionar_noticia('Novo curso na Geek University')
    agencia_noticia.notificar_todos()

    print(f'Descadastrado: {type(agencia_noticia.desinscrever()).__name__}')
    print(f'Inscreitos: {agencia_noticia.Inscritos()}')

    agencia_noticia.adicionar_noticia('Desing patterns em python!')
    agencia_noticia.notificar_todos()