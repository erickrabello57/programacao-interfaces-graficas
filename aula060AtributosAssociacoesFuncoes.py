class Pessoa:
    def __init__(self, nome, peso, cao):
        self.nome = nome
        self.peso = peso
        self.cao = cao
    
    def treinar(self):
        self.cao.daAPatinha()
        self.cao.latir()
    
class Cachorro:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    
    def daAPatinha(self):
        print("%s estendeu a patinha"%(self.nome))
    
    def latir(self):
        print("%s latiu"%(self.nome))

cachorro = Cachorro("Totó", "branco")
pessoa = Pessoa("Alberto", 80, cachorro)
pessoa.cao.daAPatinha()
print(pessoa.cao.cor)
