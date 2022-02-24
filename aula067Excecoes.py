'''Sintaxe'''

try:
    x = int(input("Digite um número: "))
except:
    print("Deu erro, valor digitado não é um número")
    x=0
finally:
    print(x)

try:
    a = open('arquivo.txt', 'r') #modo leitura, caso o arquivo não exista vai para o bloco except
    linha = a.readline()
    linha = linha.split('!')
    linha = linha[0]
    a.close()
    a = open('arquivo.txt', 'a')
    a.write(linha)
except FileNotFoundError: #só entra nesse except se encontrar FileNotFoundError
    print("Deu erro")
    a = open('arquivo.txt', 'w')# modo escrita, caso o arquivo não exista um arquivo é criado
    a.write("ERRO!!!")
finally:
    a.close()

