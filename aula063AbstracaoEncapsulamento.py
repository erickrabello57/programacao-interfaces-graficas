#Em python temos apenas dois modificadores de acesso, public ou private


class ObjetoGrafico(object):
    def __init__(self, cor):
        self.cor = cor
    def area(self): #definição de método abstrato
        pass 
    def perimetro(self):#definição de método abstrato
        pass
    def info(self):
        print("%f metros² serão preenchidos com a cor %s"*(self.area(), self.cor))

class Cachorro:
    nome = "Rex" #atributo estático
    cor = "marrom" #atributo estático

print(Cachorro.nome)
Scooby = Cachorro() # >> Rex 
print(Scooby.nome) # >> Rex

class Conta(object):
    __total = 10000 # método/atributo privado deve ter dois underlines antes de ser declarado
    reserva = 0.1
    def __init__(self, ID, saldo):
        self.__ID = ID # método/atributo privado deve ter dois underlines antes de ser declarado
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
    def imprimeReserva(): # métodos estáticos não possuem o argumento self
        print(Conta.__total * Conta.reserva)
     

banco = Conta(123, 5000)
banco.deposito(1000)
banco.saque(5000)
print(banco.saldo)
Conta.imprimeReserva()


