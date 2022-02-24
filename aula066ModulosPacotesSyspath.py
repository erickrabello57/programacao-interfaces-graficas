import sys
print(sys.path)

'''
Em python, módulos são objetos que também possuem atributos

    Quando tentamos executar ou importar um arquivo, o atributo __name__ desse arquivo muda, esse atributo indica se 
o arquivo esta sendo importado ou executado. Quando um arquvio é executado o atributo __name__ receberá o valor '__main__', já
quando o arquivo for importado o atributo __name__ receberá outro valor

'''