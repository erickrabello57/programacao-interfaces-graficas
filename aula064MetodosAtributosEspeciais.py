class Conta(object):
    '''Objeto que representa uma conta de banco'''
    codigo = -1 #atributo estático
    def __init__(self, saldo):
        '''Construtor da classe Conta'''
        Conta.codigo += 1
        self.numeroConta = str(Conta.codigo)
        self.saldo = saldo
    
    def __str__(self):
        '''Devolve a representação do objeto em string, parecido com o toString de java'''
        
        return "Nº da conta: %s \nSaldo da conta: %d "%(self.numeroConta, self.saldo) 
        
    def __add__(self, outraConta):

        '''Soma os saldos das contas'''
        self.saldo += outraConta.saldo

    def __sub__(self, outraConta):
        '''Subtrai os saldos das contas'''
        self.saldo -= outraConta.saldo
    
    def __truediv__(self, outraConta):
        '''Divide os saldos das contas'''
        self.saldo /= outraConta.saldo
    
    def __mul__(self, outraConta):
        '''Multiplica os saldos das contas'''
        self.saldo *= outraConta.saldo


class Pai:
    pass
class Filha(Pai):
    pass
class Neta(Filha):
    pass

conta = Conta(100)
conta1 = Conta(200)

print(issubclass(Pai, Filha)) # >> False
print(issubclass(Filha, Pai)) # >> True
print(issubclass(Neta, Pai)) # >> True
print(Filha.__bases__) # >> mostra a superclasse direta de Filha que é Pai
print(callable(Pai)) # >> True, pai é chamável
print(callable(conta)) # >> False pois não há implementação do método __call__
print(conta)
print("="*20)
print(conta1)
conta + conta1 #realiza a soma de saldo e guarda o valor no atributo saldo do objeto conta
print(conta) # >> saldo = 300
conta1 + conta #realiza a soma entre os saldos de conta1 e conta e depois guarda o resultado no atributo saldo do objeto conta1
print(conta1) # >> saldo = 500
conta1 - conta
print(conta1) # >> saldo = 200
conta - conta1
print(conta) # >> saldo = 100
conta * conta1
print(conta) # >> 20000
conta1 * conta
print(conta1) # >> saldo = 4000000
conta1 / conta
print(conta1) # >> saldo = 200
conta / conta1
print(conta) # >> saldo = 100
print(Conta.__init__.__doc__)
print(conta.__doc__)
print(conta.__add__.__doc__)


#pausado em 6:36