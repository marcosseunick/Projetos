from tkinter import *
from tkinter import ttk

#cores
cor_1 = "#474747" #cinza claro
cor_2 = "#FFFFFF" #branco
cor_3 = "#202020" #cinza escuro
cor_4 = "#F38064" #salmão
cor_5 = "1e1e1f" #preto

#configurações da janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("470x668")

#configurações do frame
frame_tela = Frame(janela, width=470, height=100, bg=cor_3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=470, height=668, bg=cor_1)
frame_corpo.grid(row=1, column=0)


#variavel todos valores
todos_valores = ""

#label função
valor_texto = StringVar()

#função para mostrar na tela
def entrar_valores(evento):

    global todos_valores

    todos_valores = todos_valores + str(evento)
    
    #valor na tela
    valor_texto.set(todos_valores)


#função para calcular
def  calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))


#função limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


#configurações label
app_label = Label(frame_tela, textvariable=valor_texto, width=32, height=4, padx=14, relief=FLAT, anchor="e", justify=RIGHT, font=("Jetbrains 18"), bg=cor_3, fg=cor_2)
app_label.place(x =0, y=0)


#configuração dos botões

#primeira linha
botao_1 = Button(frame_corpo, command=limpar_tela , text="C", width=18, height=4, bg=cor_3, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_1.place(x=0, y=0)
botao_2 = Button(frame_corpo, command = lambda: entrar_valores("%"), text="%", width=8, height=4, bg=cor_3, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_2.place(x=243, y=0)
botao_3 = Button(frame_corpo, command = lambda: entrar_valores("/"), text="/", width=8, height=4, bg=cor_3, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_3.place(x=357, y=0)

#segunda linha
botao_2 = Button(frame_corpo, command = lambda: entrar_valores("7"),  text="7", width=9, height=4, bg=cor_1, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_2.place(x=1, y=114)
botao_3 = Button(frame_corpo, command = lambda: entrar_valores("8"), text="8", width=9, height=4, bg=cor_1, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_3.place(x=118, y=114)
botao_4 = Button(frame_corpo, command = lambda: entrar_valores("9"),  text="9", width=8, height=4, bg=cor_1, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_4.place(x=243, y=114)
botao_5 = Button(frame_corpo, command = lambda: entrar_valores("*"),  text="X", width=8, height=4, bg=cor_3, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_5.place(x=357, y=114)

#terceira linha
botao_6 = Button(frame_corpo, command = lambda: entrar_valores("4"),  text="4", width=9, height=4, bg=cor_1, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_6.place(x=1, y=228)
botao_7 = Button(frame_corpo, command = lambda: entrar_valores("5"),  text="5", width=9, height=4, bg=cor_1, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_7.place(x=118, y=228)
botao_8 = Button(frame_corpo, command = lambda: entrar_valores("6"), text="6", width=8, height=4, bg=cor_1, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_8.place(x=243, y=228)
botao_9 = Button(frame_corpo, command = lambda: entrar_valores("-"), text="-", width=8, height=4, bg=cor_3, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_9.place(x=357, y=228)

#quarta linha
botao_10 = Button(frame_corpo, command = lambda: entrar_valores("1"),  text="1", width=9, height=4, bg=cor_1, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_10.place(x=1, y=342)
botao_11 = Button(frame_corpo, command = lambda: entrar_valores("2"), text="2", width=9, height=4, bg=cor_1, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_11.place(x=118, y=342)
botao_12 = Button(frame_corpo, command = lambda: entrar_valores("3"), text="3", width=8, height=4, bg=cor_1, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_12.place(x=243, y=342)
botao_13 = Button(frame_corpo, command = lambda: entrar_valores("+"), text="+", width=8, height=4, bg=cor_3, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_13.place(x=357, y=342)

#quinta linha
botao_1 = Button(frame_corpo, command = lambda: entrar_valores("0"), text="0", width=18, height=4, bg=cor_1, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_1.place(x=0, y=456)
botao_2 = Button(frame_corpo, command = lambda: entrar_valores("."), text=".", width=8, height=4, bg=cor_1, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_2.place(x=243, y=456)
botao_3 = Button(frame_corpo, command = calcular,  text="=", width=8, height=4, bg=cor_4, fg=cor_2, font=("JetBrains 16 bold"), relief=RAISED, overrelief=RIDGE)
botao_3.place(x=357, y=456)



janela.mainloop()