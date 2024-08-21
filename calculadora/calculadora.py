def soma(a,b):
    '''
    retorna a + b.
    :param a: int.
    :param b: int.
    :return int soma de a e b.
    '''
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

print(__name__)

if __name__=='__main__':
    '''
    TYeste
    '''
    print("Estou dentro da MAIN")
    print("Resultado", soma(100, 15))
    print(__name__)
    #print(soma.__doc__)