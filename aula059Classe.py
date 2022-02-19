class Caneta:
   
    #construtor
    def __init__(self):
        
        self.marca ="compactor"
        self.cor ="preta"
        self.carga = 5
        
        

    #método
    def escrever(self):
        print("A caneta de marca %s e de cor %s está escrevendo"%(self.marca, self.cor))
        print("A carga da caneta é %d"%(self.carga))
        self.carga = self.carga - 1

    def trocaDecor(self, novaCor):
        self.cor = novaCor;

    def trocaDeMarca(self, novaMarca):
        self.marca = novaMarca
    


Caneta = Caneta()
Caneta.escrever()
Caneta.trocaDecor("azul")
Caneta.escrever()
Caneta.trocaDeMarca("bic")
Caneta.escrever()


