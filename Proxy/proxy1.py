
class Ator:
    def __init__(self):
        self.ocupado = False

    def indisponivel(self):
        self.ocupado = True
        print(f'{type(self).__name__} está ocupado em uma atuação.')
    
    def disponivel(self):
        self.ocupado = False
        print(f'{type(self).__name__} está disponível para uma atuação.')
    
    def ver_disponibilidade(self):
        return self.ocupado

#Proxy    
class Agente:

    def trabalhar(self):
        ator = Ator()
        if ator.ver_disponibilidade():
            ator.indisponivel()
        else:
            ator.disponivel()

# Cliente
if __name__ == '__main__':
    agente = Agente()
    agente.trabalhar()