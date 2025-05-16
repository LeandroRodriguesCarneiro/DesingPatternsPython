class SanidadeCheck:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(SanidadeCheck, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
    
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.__servidores = []
            self._initialized = True

    def checar_servidor(self, srv):
        if srv < len(self.__servidores):
            print(f'Checando o {self.__servidores[srv]}')
        else:
            print('Servidor não encontrado')

    def add_servidor(self):
        self.__servidores.append('Servidor 1')
        self.__servidores.append('Servidor 2')
        self.__servidores.append('Servidor 3')
        self.__servidores.append('Servidor 4')
    
    def mudar_servidor(self):
        if self.__servidores:
            self.__servidores.pop()
            self.__servidores.append('Servidor 5')
        else:
            print('Nenhum servidor para mudar')
    
    def listar_servidores(self):
        return self.__servidores


sc1 = SanidadeCheck()
sc2 = SanidadeCheck()

sc1.add_servidor()
print('Cronograma de checagem de sanidade dos servidores A...')
for svr in range(len(sc1.listar_servidores())):
    sc1.checar_servidor(svr)


sc2.mudar_servidor()
# Verificando se sc2 é realmente o mesmo que sc1 (singleton)
print(sc1 is sc2)  # Deve imprimir True
print('Cronograma de checagem de sanidade dos servidores B...')
for svr in range(len(sc1.listar_servidores())):
    sc2.checar_servidor(svr)

