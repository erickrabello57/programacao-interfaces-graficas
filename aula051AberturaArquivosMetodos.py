from random import randint

arquivo = open('arq1.txt', 'w+') #open recebe o nome do arquivo e o modo de abertura w = write, r = read, a = append
for i in range(3):
    arquivo.write('Olá arquivo! \n') #metodo que recebe uma string

arquivo.writelines(['Fórmula 1\n', 'Fórmula 2\n', 'Fórmula 3\n']) #método que espera receber uma lista de strings

'''No modo write, caso o arquivo não exista ele será criado'''

for i in range(4):
    arquivo.write('[ ')
    for j in range(4):
        numero = randint(10, 99)
        arquivo.write(str(numero))
        arquivo.write(' ')
    arquivo.write(']\n')
arquivo.close()


arquivo = open('arq1.txt','r')
print(arquivo.readline()) # le cada linha do arquivo por vez e coloca seu conteúdo em uma string
print('='*20)
print(arquivo.read()) # le todo o arquivo e coloca tudo em uma string
arquivo.close()

arquivo = open('arq1.txt','r')
print(arquivo.readlines()) #le todas as linhas do arquivo e as coloca num vetor/lista de strings 
print(arquivo.readlines()) #retorna uma lista vazia pois não há mais nada no arquivo a ser lido
arquivo.close()

arquivo = open('arq1.txt','a') #modo append abre o arquivo e procura pelo ultimo caractere não nulo, tornando possível a escrita a partir desse ponto
arquivo.write('Modo append')
arquivo.close()

arquivo = open('arq1.txt','r')
print(arquivo.readlines())
arquivo.close()


