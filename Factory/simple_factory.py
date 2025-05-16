from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print('Au! Au!')

class Gato(Animal):
    def falar(self):
        print('Miau')

#factory
class Factory:
    def criate_animal_falante(self, tipo):
        return eval(tipo)().falar()
    
#cliente
if __name__ == '__main__':
    fac = Factory()
    animal = input('Qual animal que vai falar: [Cachorro, Gato] ')
    fac.criate_animal_falante(animal.capitalize())