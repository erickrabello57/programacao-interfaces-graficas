#Dicionario

pessoa = {'Nome':'Lucas', 'Emprego':'Advogado', 'Idade':20, 'Cor de cabelo':'Preto'}
pessoa['Nome'] = 'João'
print(pessoa['Emprego']) #imprime o emprego de pessoa
print(pessoa) #imprime todos os dados de pessoa
pessoa['Peso'] = 75 #adiciona 'peso' ao dicionário pessoa
print(pessoa) # imprime pessoa já com o peso adicionado

class Pessoa:
    pass

OutraPessoa = Pessoa()
OutraPessoa.nome = "Roberto"
OutraPessoa.emprego = "Professor"
OutraPessoa.corDeCabelo = "Loiro"
print(OutraPessoa.__dict__) #imprime o objetyo em forma de dicionário

dicionario = dict (nome = "Diego", emprego = "Engenheiro", idade = 35)
print(dicionario)


