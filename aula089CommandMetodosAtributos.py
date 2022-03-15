from tkinter import *

loginSenhas = {
    'alberto@gmail.com':'1234', 
    'bruno@gmail.com': '5678',
    'carlos@gmail.com':'9101112',
    'daniel@gmail.com':'senha'}

def autenticaLoginSenha():
    
    login = entradaLogin.get()
    senha = entradaSenha.get()

    if login not in loginSenhas:
        status['text'] = 'Usuário inválido'
        status['bg'] = 'red'
        status['fg'] = 'white'

    if login in loginSenhas and loginSenhas.get(login) == senha:
        status['text'] = 'Login efetuado com sucesso!'
        status['bg'] = 'green'
        status['fg'] = 'white'
    
    if login in loginSenhas and loginSenhas.get(login) != senha:
        status['text'] = 'Senha inválida'
        status['bg'] = 'red'
        status['fg'] = 'white'



#definição dos elementos da tela
tela = Tk()
tela.title('Exercicio aula 89')
login = Label(tela, text='Login', fg='white')
entradaLogin = Entry(tela, bg='white', fg='black')
senha = Label(tela, text='Senha', fg='white')
entradaSenha = Entry(tela, bg='white', fg='black')
botao = Button(tela, text='Entrar', command=autenticaLoginSenha)
status = Label(tela)

#exibição dos elementos na tela

login.pack()
entradaLogin.pack()
senha.pack()
entradaSenha.pack()
botao.pack()
status.pack()


tela.mainloop()

#aula089 11:24