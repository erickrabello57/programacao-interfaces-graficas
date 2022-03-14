from tkinter import *



tela = Tk() #cria a janela

tela.geometry('800x600') #tamanho da tela em pixels
tela.title('Olá mundo!') # Dá um titulo à tela
#tela.wm_iconbitmap('icone.ico') Dá um ícone ao aplicativo
texto = Label(tela, text = 'Olá mundo! Estou na tela!', bg = 'red', fg='white') #label que aparece em tela
#label é apenas um texto
texto.pack() # joga na tela o que foi definido em texto

entradaDeTexto = Entry(tela, text='Digite algo aqui', fg='white')
entradaDeTexto.pack()

botao = Button(tela, text = 'Clique aqui!', justify= 'left')
botao.pack()

#A ordem que empacotamos os widgets será a ordem que eles aparecerão em tela



tela.mainloop() #roda o programa
