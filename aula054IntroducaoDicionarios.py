contato = {'Nome':'Alberto' , 'Telefone': 998877550,'email':'alberto@gmail.com'}
print(contato['Nome']) # >> Alberto
print(contato['Telefone']) # >> 998877550
print(contato.get('email')) #retorna o valor da chave passada como argumento >> alberto@gmail.com
DicionarioContatos = {'Contato1': contato}
print(DicionarioContatos['Contato1']) #retorna o valor da chave 'Contato1', ou seja,temos um dicionário embutido em outro dicionário
contato['Endereço'] = 'Rua da Caixa' #Um par chave-valor não existente pode ser adicionado à um dicionário existente
print(contato)
contato['Endereço'] = 'Rua do Substituto' #Qualquer par chave-valor pode ser alterado
print(contato)