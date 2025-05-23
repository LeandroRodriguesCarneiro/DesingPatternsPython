from abc import ABCMeta, abstractmethod

class Compilador(metaclass=ABCMeta):

    @abstractmethod
    def coletar_fonte(self):
        pass
    
    @abstractmethod
    def compilar_objeto(self):
        pass

    @abstractmethod
    def excutar(self):
        pass
    
    def compilar_e_executar(self):
        self.coletar_fonte()
        self.compilar_objeto()
        self.excutar()

class CompiladorIOS(Compilador):

    def coletar_fonte(self):
        print('Coletando código fonte swift')

    def compilar_objeto(self):
        print('Compilando código swift para bytecode LLVM')

    def excutar(self):
        print('Programa executando no ambiente de execução')

class CompiladorAndroid(Compilador):

    def coletar_fonte(self):
        print('Coletando código fonte kotlin')

    def compilar_objeto(self):
        print('Compilando código kotlin para bytecode JVM')

    def excutar(self):
        print('Programa executando no ambiente de execução')


ios = CompiladorIOS()
ios.compilar_e_executar()

android = CompiladorAndroid()
android.compilar_e_executar()