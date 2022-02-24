class Conta(object):
    cod = 0
    def __init__(self):
        self.ID = Conta.cod
        self.saldo = 500
        Conta.cod += 1
    
    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def __str__(self):
        return "========\nID: %i \nSaldo: %d \n========"%(self.ID, self.saldo)

    # less than or equal
    def __le__(self, outro):
        if self.ID <= outro.ID:
            return True
        return False
    #equal
    def __eq__(self, outro):
        if self.ID == outro.ID:
            return True
        return False
    # greater than or equal
    def __ge__(self, outro):
        if self.ID >= outro.ID:
            return True
        return False
    # less than
    def __lt__(self, outro):
        if self.ID < outro.ID:
            return True
        return False
    #greater than
    def __gt__(self, outro):
        if self.ID > outro.ID:
            return True
        return False
    #not equal
    def __ne__(self, outro):
        if self.ID != outro.ID:
            return True
        return False

class Banco:
    def __init__(self):
        self.contas = Contas()

class Contas(list):
    '''Classe que armazena uma lista de objetos do tipo Conta'''
    def sort(self):
        copiaContas = self.copy()
        numeroDeContas = len(self)
        self.clear()
        while len(self) < numeroDeContas:
            contaMenorID = copiaContas[0]
            for conta in copiaContas:
                if conta.ID < contaMenorID.ID:
                    contaMenorID = conta
            self.append(contaMenorID)
            copiaContas.remove(contaMenorID)



    

#aula pausada em 17:29



conta = Conta()
conta1 = Conta()
print(conta)
print(conta1)
banco = Banco()
banco.contas.append(conta1)
banco.contas.append(conta)
banco.contas.sort()
print(banco.contas[0].ID)
print(banco.contas[1].ID)

