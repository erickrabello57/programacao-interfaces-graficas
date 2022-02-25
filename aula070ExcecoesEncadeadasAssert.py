class ForaDoIntervaloErro(Exception):
    def __init__(self, numero):
        self.numero = numero
    def __str__(self):
        return "O número digitado , %i, está fora do intervalo estipulado!"%self.numero

def exemplo1():
    try:
        num = 1/0 #ZeroDivisionError
        int(num) #ValueError
    except Exception as e:
        raise ValueError from e


def exemploAssert1():
    while True:
        try:
            numero = int(input("Digite um número ente 1 e 20: "))
            
        except ValueError:
            print("Digite apenas números!")
        else:
            break

    teste = True

    if not  1 <=numero<= 20:
        teste = False

    assert teste, numero #verifica se teste é True, caso não seja um exceção é levantada, AssertionError

    if __debug__: #atributo dos módulos, setado por padrão como True
        if not teste:
            raise AssertionError(numero)

def exemploAssert2(numero):
#Nesta função verifico com assert se o numero passado é positivo, caso seja calculo a raiz quadrada desse numero
    assert numero > 0, 'número precisa ser maior que zero'
    return numero**(1/2)

print(exemploAssert2(-1))
