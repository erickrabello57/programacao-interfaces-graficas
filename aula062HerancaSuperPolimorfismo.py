class Mamifero(object):
    def __init__(self, corDePelo, genero, qtdPernas):
        self.corDePelo = corDePelo
        self.genero = genero
        self.qtdPernas = qtdPernas
    
    def falar(self):
        print("Olá, eu sou um mamífero que possui %i pernas"%(self.qtdPernas))
    
    def andar(self):
        print("Ando com %i pernas"%(self.qtdPernas))
    
    def amamentar(self):
        if self.genero.lower()[0] == "m":
            print("Machos não amamentam")
            return
        else:
            print("Amamentando o filhote")
    
    
Scooby= Mamifero("Caramelo", "Macho", 4)
print(Scooby.__dict__)
Scooby.amamentar()

class Pessoa(Mamifero): #Aqui declaramos que Pessoa é uma subclasse de mamífero, herdando assim seus atributos e métodos
    def __init__(self,corDePelo, genero, qtdPernas, cabelo): #construtor da subclasse pessoa com os argumentos tanto da classe Pessoa quanto da superclasse mamifero
        super(Pessoa, self).__init__(corDePelo, genero, qtdPernas) #chamada do construtor da superClasse Mamifero passando os argumentos recebidos pela subclasse Pessoa
        self.cabelo = cabelo #atributo da subclasse Pessoa
    
    def falar(self): #método da classe Pessoa
        super(Pessoa, self).falar() #chamada ao método falar da superclasse de Pessoa, Mamifero
        print("Olá sou uma pessoa e estou falando") 

Laura = Pessoa("Preto", "Feminino", 2, "Preto")
Laura.amamentar()
Laura.andar()
Laura.falar()







        