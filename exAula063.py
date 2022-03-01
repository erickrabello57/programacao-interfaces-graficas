"""
Escreva um progama de banco que possua:

Uma classe Banco com os atributos
* private total
* public taxaReserva
* private reservaExigida

Que possua os métodos
* private calculaReserva
* public podefazerEmprestimo(valor) - boolean


Uma classe conta com os atributos

* private saldo
* private ID
* private senha

Que possua métodos

public deposito
public saque(senha valor)
public podeReceberEmprestimo (valor) bool
public saldo 
"""

class Banco(object):
    def __init__(self, total, taxaReserva, reservaExigida):
        self.__total = total
        self.taxaReserva = taxaReserva
        self.__reservaExigida = reservaExigida
    
    def __calculaReserva(self):
        return round(self.getTotal() * self.taxaReserva, 2)
        
    def getTotal(self):
        return self.__total

    def getReservaExigida(self):
        return self.__reservaExigida
    
    def getReserva(self):
        return self.__calculaReserva()
    
    def podeFazerEmprestimo(self):
        if self.__calculaReserva() >= self.__reservaExigida:
            return True
        return False


class Conta(object):
    
    def __init__(self, saldo, ID, senha):
        self.__saldo = saldo
        self.__ID = ID
        self.__senha = senha

    def deposito(self, senha, valor):
        if senha == self.__senha:
            self.__saldo += valor
    
    def saque(self, senha, valor):
        
        if self.__senha == senha:
            if self.__saldo >= valor:
                self.__saldo -= valor
    
    def podeReceberEmprestimo(self, valor):
        if valor < self.__saldo * 1.5:
            return True
        return False

    def saldo(self):
        print("O saldo da conta é:",self.__saldo)

        
        

Banco = Banco(555, 0.1, 60)
#print(Banco.getReserva())
#print(Banco.podeFazerEmprestimo())

Conta = Conta(500,1, 123 )
Conta.deposito(333, 1000) # depósito não é realizado pois a senha está errada >> 500
Conta.saldo()
Conta.deposito(123, 1000) 
Conta.saldo() # >> 1500
print(Conta.podeReceberEmprestimo(200)) # >> True
print(Conta.podeReceberEmprestimo(20000)) # >> False