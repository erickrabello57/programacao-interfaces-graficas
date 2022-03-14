from tkinter import *

def calcular():
    resultado['text'] = entradaDeTexto.get()
    resultado['fg'] = 'red'

tela = Tk()
tela.geometry('800x600')
tela.title('Calculadora estatística')
botaol1c1 = Button(tela, text='Botão A')
botaol1c2 = Button(tela, text='Botão B')
botaol1c3 = Button(tela, text='Botão C')
botaoCentralCalcular = Button(tela,text='Calcular', command=calcular)
resultado = Label(tela, text='Resultado', fg='White')
entradaDeTexto = Entry(tela, fg='blue', bg='white')
entradaDeTexto.pack()
botaoCentralCalcular.pack()
resultado.pack()
botaol1c1.pack()
botaol1c2.pack()
botaol1c3.pack()

tela.mainloop()
#aula89 pausada em 1:57