from abc import ABCMeta, abstractmethod

#Interface
class Carteira(metaclass = ABCMeta):

    @abstractmethod
    def pagar(self):
        pass

#ObjetoReal
class Banco(Carteira):

    def __init__(self):
        self.carteira = None
        self.conta = None

    def __get_conta(self):
        self.conta = self.cartao

        return self.conta
    
    def __tem_saldo(self):
        print(f'Banco :: Checando se a conta {self.__get_conta()} tem saldo')
        return True
    
    def set_cartao(self, cartao):
        self.cartao = cartao

    def pagar(self):
        if self.__tem_saldo():
            print('Banco :: Pagando bar...')
            return True
        else:
            print('Banco :: Desculpe, voce não tem saldo suficiente...')
            return False
        
#Proxy
class CartaoDebito(Carteira):

    def __init__(self):
        self.banco = Banco()

    def pagar(self):
        cartao = input('Proxy:: Informe o número do cartão: ')
        self.banco.set_cartao(cartao)
        return self.banco.pagar()
    

class Cliente:

    def __init__(self):
        print('Cliente:: Quero quero comprar uma cerveja')
        self.cartao_debito = CartaoDebito()
        self.comprei = None

    def fazer_pagamento(self):
        self.comprei = self.cartao_debito.pagar()

    def __del__(self):
        if self.comprei:
            print('Cliente:: Finalmente vou tomar uma cerveja')
        else:
            print('Cliente:: Gostaria de ter mais dinheiro...')

if __name__ == '__main__':
    cliente = Cliente()
    cliente.fazer_pagamento()