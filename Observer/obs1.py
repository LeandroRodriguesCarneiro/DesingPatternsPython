

class Objeto:
    def __init__(self):
        self.__observadores = []

    def __repr__(self):
        return '::Objeto::'
    
    def registrar(self, observador):
        self.__observadores.append(observador)

    def notificar_todos(self, *args, **kwargs):
        for observador in self.__observadores:
            observador.notificar(self, *args, **kwargs)

class ObservdorA:

    def __init__(self, objeto):
        objeto.registrar(self)

    def notificar(self, objeto, *args):
        print(f'{type(self).__name__} recebeu uma {args[0]} de {objeto}')

class ObservdorB:

    def __init__(self, objeto):
        objeto.registrar(self)

    def notificar(self, objeto, *args):
        print(f'{type(self).__name__} recebeu uma {args[0]} de {objeto}')


obj = Objeto()

obs_a = ObservdorA(obj)
obs_b = ObservdorB(obj)

obj.notificar_todos('notificação')