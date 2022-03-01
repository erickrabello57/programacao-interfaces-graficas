
arquivo = open('aula052.txt','w')
arquivo.write('Ola\nmeu\nnome\ne\nPedro')
arquivo.close()

arquivo = open('aula052.txt','rb') #modo rb, readbytes modo wb, writebytes
#print(arquivo.readline()) #imprime a linha lida em formato de byte
arquivo.close()

arquivo = open('aula052.txt', 'r')
print(arquivo.read(6)) # passo como argumento a quantidade de bytes a ser lida >> Ola \n me 
print(arquivo.tell()) # retorna o byte da posição da cabeça de leitura >> 6
print(arquivo.seek(8))# ando 8 bytes com a cabeça de leitura a partir do inicio do arquivo
print(arquivo.read(2)) # >> no
print(arquivo.tell()) # >> 10
print(arquivo.readlines(1))
print(arquivo.readlines())
arquivo.close()

arquivo = open('aula052.txt', 'r')
#leitura com for
for i in arquivo:
    print(i)
arquivo.close()
print('='*20)
arquivo = open('aula052.txt', 'r')
for i in arquivo.readline():
    print(i)
arquivo.close()

#como passar uma lista para um arquivo txt?
list = eval('[1, 2, 3]')
print(list)