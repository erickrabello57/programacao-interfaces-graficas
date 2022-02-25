def exemplo1():

    try:
        lista = []
        lista.append(int("efg"))
        a = lista[0]
    except IndexError:
        print("Erro!")
    except ValueError:
        print("Erro de valor")
    finally:
        print("Chegamos ao final")

def exemplo2():
    try:
        lista = []
        lista.append(int("efg"))
        a = lista[0]
    except (IndexError, ValueError): # imprime 'Erro!' se ocorrer um IndexError ou um ValueError
        print("Erro!")
    finally:
        print("Chegamos ao final")

def exemplo3():
    try:
        lista = []
        a = lista[2]
    except (IndexError, ValueError) as e: # atribui a 'e' o valor da exceção ocorrida
        print(e)
    finally:
        print("FIM")

def exemplo4():
    try:
        lista = []
        #a = lista[2]
    except (IndexError, ValueError) as e: # atribui a 'e' o valor da exceção ocorrida
        print(e)
    else:   #Só entra no bloco else caso nenhuma exceção tenha ocorrido
        print("Nenhuma exceção ocorreu")
    finally:
        print("FIM")

#exemplo2()
#exemplo3()
exemplo4()