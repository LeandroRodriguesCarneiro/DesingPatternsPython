from abc import ABCMeta, abstractmethod

class Secao(metaclass = ABCMeta):
    @abstractmethod
    def __repr__(self):
        pass

class SecaoPessoal(Secao):

    def __repr__(self):
        return 'Secao Pessoal'
    
class SecaoAlbum(Secao):

    def __repr__(self):
        return 'Secao Album'

class SecaoProjeto(Secao):

    def __repr__(self):
        return 'Secao Projeto'
    
class SecaoPublicacao(Secao):

    def __repr__(self):
        return 'Secao Publicacao'
    
class Perfil(metaclass= ABCMeta):

    def __init__(self):
        self.secoes = []
        self.criar_perfil()
        
    @abstractmethod
    def criar_perfil(self):
        pass

    def get_secoes(self):
        return self.secoes
    
    def add_secoes(self, secao):
        self.secoes.append(secao)

class Linkedin(Perfil):

    def criar_perfil(self):#factory method
        self.add_secoes(SecaoPessoal())
        self.add_secoes(SecaoProjeto())
        self.add_secoes(SecaoPublicacao())

class Facebook(Perfil):

    def criar_perfil(self):#factory method
        self.add_secoes(SecaoPessoal())
        self.add_secoes(SecaoAlbum())

if  __name__ == '__main__':
    rede = input('Qual rede social quer criar o perfil? [Linkedin, Facebook]').capitalize()
    perfil = eval(rede)()

    print(f'Criando perfil no {type(perfil).__name__}')
    print(f'O perfil tem as secoes {perfil.get_secoes()}')