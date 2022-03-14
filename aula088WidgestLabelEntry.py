from operator import contains
from tkinter import *

def calculaSoma():
    soma = 0
    str = entrada.get()
    str = str.replace(' ','')
    if '+' in str:
        str = str.split('+')
    
    for i in range(len(str)):
        soma += int(str[i])
    
    texto['text'] = soma
    

def inverteCores():
    
    botaobackground = botao['bg']
    botaoforeground = botao['fg']
    textobackground = texto['bg']
    textoforeground = texto['fg']
    botao['bg'] = botaoforeground
    botao['fg'] = botaobackground
    texto['bg'] = textoforeground
    texto['fg'] = textobackground
    
# Todos os elementos que fazem parte da interface gráfica são chamados de widgets

 #tudo que controla a tela
tela = Tk()
tela.geometry('800x600') # tamanho da tela
tela.title('Aula 088 - Widgets')


#Widgets
botao = Button(tela, text='Clique aqui para inverter as cores', bg='white', fg='black', command=inverteCores)
texto = Label(tela, text="Texto em tela", bg= 'red', fg='blue')
entrada = Entry(tela, bg='white', fg='black')
botaoCalcula = Button(tela, text='Calcule a soma', bg='blue', fg='white', command=calculaSoma)
botao.pack() # coloca na tela
texto.pack() # coloca na tela
entrada.pack()
botaoCalcula.pack()

tela.mainloop()

