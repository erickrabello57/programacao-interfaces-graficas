#exceção própria

class ValorRepetidoErro(Exception):
    def __init__(self, numero):
        self.numero = numero
    def __str__(self):
        return "Número %i digitado anteriormente!"%(self.numero)

def main():
    lista = []
    for i in range(3):
        while True:
            try:
                numero = int(input("Escolha um número: "))
                break
            except ValueError:
                print("Digite apenas números!")
        if(numero not in lista):
            lista.append(numero)
        else:
            raise ValorRepetidoErro(numero)   
    for i in range(len(lista)):
        print(lista[i],end = ' ')


def teste():

    try:
        a = int(input("Escolha um número entre 1 e 20: "))
        if  a > 20 or a < 1:
            raise ValueError
        else:
            print("Obrigado por escolher ", a)
    except ValueError:
        print("Entrada inválida")

# teste()

main() 