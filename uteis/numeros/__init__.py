def fatorial(numero):
    if numero < 0:
        raise ValueError
    
    if numero == 0:
        return 1
    
    resultado = 1
    for i in range(1, numero +1):
        resultado *= i
    return resultado

def dobro(numero):
    return numero *2

def triplo(numero):
    return numero * 3