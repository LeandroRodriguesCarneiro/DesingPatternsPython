class Instalador:
    def __init__(self, fonte, destino):
        self.opcoes = []
        self.destino = destino
        self.fonte = fonte

    def preferecias(self, escolha):
        self.opcoes.append(escolha)

    def executar(self):
        for opcao in self.opcoes:
            if list(opcao.values())[0]:
                print(f'Copiando os binários de {self.fonte} para {self.destino}')
            else:
                print('opção finalizada')

if __name__ == '__main__':
    #Inicia o instalador
    instalador = Instalador('python3.9.1.gzip', './usr/bin/')

    #O usuario escolhe intalar apenas o python
    instalador.preferecias({'python': True})
    instalador.preferecias({'java': False})

    #execute
    instalador.executar()