dic = {'Lambda': lambda x: x+1 }
print(dic['Lambda']) # >> endereco de memória onde a função está
print()
print(dic['Lambda'](10)) # retonarna o resultado da função >> 11
contato = {'Nome':'Alberto' , 'Telefone': 998877550,'email':'alberto@gmail.com'}

#o loop for pode percorrer as chaves do dicionário quado usamos o operador in
for campo in contato:
    print(campo)
print()
#agora o loop percorre os valores do dicionário 
for campo in contato:
    print(contato[campo])
print()
print('Nome' in contato) # >> True
print()
print('Endereço' in contato) # False
print()
#Len em dicionário

print(len(dic)) # >> 1
print()
print(len(contato)) # >> 3