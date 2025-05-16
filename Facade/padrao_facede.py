#Facade
class GerenciamentoEventos:
    def __init__(self):
        print('GerenciamentoEventos :: Vou organizar com todo mundo!\n\n')
    
    def organizar(self):
        self.salao = SalaoFestas()
        self.salao.agendar()

        self.florista = Florista()
        self.florista.arranjar_flores()

        self.comida = Restaurante()
        self.comida.preparar()

        self.musica = Banda()
        self.musica.montar_palco()

#Subsistema 1 
class SalaoFestas:

    def __init__(self):
        print('SalaoFestas :: Agendando o salao de festas para o casamento')
    
    def _esta_disponivel(self):
        print('SalaoFestas :: Este salão está disponivel?')
        return True
    
    def agendar(self):
        if self._esta_disponivel():
            print('SalaoFestas :: EAgendamento do salão realizado.\n')

#Subsistema 2 
class Florista:

    def __init__(self):
        print('Florista :: Flores para um evento?')
    
    def arranjar_flores(self):
        print('Florista :: Rosas, Margaridas e Lírios serão usados...\n')


#Subsistema 3 
class Restaurante:

    def __init__(self):
        print('Restaurante :: Comida para eventos...')
    
    def preparar(self):
        print('Restaurante :: Comida chinesa e brasileira serao servidas...\n')

#Subsistema 4 
class Banda:

    def __init__(self):
        print('SalaoFestas :: Arranjos musicais para o evneto...')
    
    def montar_palco(self):
        print('SalaoFestas :: Preparando o palco para tocar jazz e rock no evento.\n')
        return True
    
#Cliente
class Cliente:

    def __init__(self):
        print('Cliente :: Uau! preparacao para o casamento!')
    
    def contrata_gerente_eventos(self):
        print('Cliente :: Vou contratar uma empresa para gerenciar eventos\n')

        ge = GerenciamentoEventos()
        ge.organizar()

    def __del__(self):
        print('Cliente :: Foi muito simples organizar este evento com Façade\n')


if __name__ == '__main__':
    cliente = Cliente()
    cliente.contrata_gerente_eventos()
