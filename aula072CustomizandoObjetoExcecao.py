class DeuErroArquivo(Exception):
    def __init__(self, linhaArquivo, nomeArquivo):
        self.linha = linhaArquivo
        self.arquivo = nomeArquivo
    
    def imprimeAlgo(self):
        print('Algo')

    def __str__(self):
        return "Deu erro no arquivo %s na linha %s"%(self.arquivo, self.linha)

try:
    raise DeuErroArquivo('50', 'arq.txt')
except DeuErroArquivo as e:
    e.imprimeAlgo()
    print(e)

