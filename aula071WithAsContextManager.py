#O with as statement funciona como equivalente à alguns blocos de try/except fazendo uso do context manager

#open possui context manager
with open('arquivo.txt') as meuArquivo:
    for linha in meuArquivo:
        print(linha)


#De maneira equivalente teríamos:
arquivo = open('arquivo.txt')

try:
    for linha in arquivo:
        print(linha)
finally:
    arquivo.close()

#   Context manager é uma classe que possui dois atributos especiais, __enter__ e __exit__

class NossoContextManager:
    def imprime(self, msg):
        print(msg)
    def __enter__(self):
        print("Entrando no bloco with")
        return self
    def __exit__(self, tipo, valor, traceback):
        print(tipo)
        print("===")
        print(valor)
        print("===")
        print(traceback)
        print("===")

with NossoContextManager() as teste:
    teste.imprime('Olá mundo!')
    raise ValueError #força a entrada em __exit__

