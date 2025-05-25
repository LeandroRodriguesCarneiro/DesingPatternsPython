# def calcular(v1, v2):
#     soma = v1 + v2
#     return soma

def calcular(v1, v2):
    return v1 + v2

if __name__ == '__main__':
    n1 = int(input('Informe o valor 1: '))
    n2 = int(input('Informe o valor 2: '))

    print(f'A soma de {n1} com {n2} e {calcular(n1, n2)}')  