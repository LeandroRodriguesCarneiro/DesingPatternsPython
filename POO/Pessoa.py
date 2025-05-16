from datetime import datetime

class Pessoa:
    def __init__(self: object, nome: str, nascimento: str) -> None:
        self.__nome = nome
        self.__nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

    def __str__(self: object) -> str:
        return self.__nome
    
    def __repr__(self: object) -> str:
        return f"Pessoa(nome='{self.__nome}', nascimento='{self.__nascimento.strftime('%d/%m/%Y')}')"

if __name__ == "__main__":
    pessoa = Pessoa('Leandro Rodrigues Carneiro', '16/04/2003')
    print(pessoa.__str__())  
    print(pessoa.__repr__()) 
