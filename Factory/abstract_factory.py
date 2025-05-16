from abc import ABCMeta, abstractmethod

# Abstract Factory
class PizzaFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def criar_pizza_veg(self):
        pass
    
    @abstractmethod
    def criar_pizza(self):
        pass

# Concrete Factory A: PizzaBrasileira
class PizzaBrasileira(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaMandioca()  # Return the concrete PizzaVeg (Mandioca)
    
    def criar_pizza(self):
        return PizzaCamarao()  # Return the concrete Pizza (Camarao)

# Concrete Factory B: PizzaItaliana
class PizzaItaliana(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaBrocolis()  # Return the concrete PizzaVeg (Brocolis)
    
    def criar_pizza(self):
        return PizzaBolonha()  # Return the concrete Pizza (Bolonha)

# Abstract Product A: PizzaVeg
class PizzaVeg(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self):
        pass

# Abstract Product B: Pizza
class Pizza(metaclass=ABCMeta):

    @abstractmethod
    def servir(self, pizza_veg):
        pass

# Concrete Product A: PizzaMandioca
class PizzaMandioca(PizzaVeg):
    def preparar(self):
        print(f'Preparando {type(self).__name__}')

# Concrete Product A: PizzaBrocolis
class PizzaBrocolis(PizzaVeg):
    def preparar(self):
        print(f'Preparando {type(self).__name__}')

# Concrete Product B: PizzaCamarao
class PizzaCamarao(Pizza):
    def servir(self, pizza_veg):
        print(f'{type(self).__name__} é servida com camarão na {type(pizza_veg).__name__}')

# Concrete Product B: PizzaBolonha
class PizzaBolonha(Pizza):
    def servir(self, pizza_veg):
        print(f'{type(self).__name__} é servida com bolonha na {type(pizza_veg).__name__}')

# Client
class Pizzaria:

    def fazer_pizzas(self):
        for factory in [PizzaBrasileira(), PizzaItaliana()]:
            self.factory = factory
            self.pizza = self.factory.criar_pizza()  # Create the regular pizza
            self.pizza_veg = self.factory.criar_pizza_veg()  # Create the veg pizza
            self.pizza_veg.preparar()  # Prepare the veg pizza
            self.pizza.servir(self.pizza_veg)  # Serve the regular pizza with the veg pizza

# Test the code
pizzaria = Pizzaria()
pizzaria.fazer_pizzas()
