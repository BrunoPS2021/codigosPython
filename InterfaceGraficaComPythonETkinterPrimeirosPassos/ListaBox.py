# %%
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

janela = Tk()
janela.geometry("500x600")
janela.title("Listbox")

textoDiaSemana = Label(janela,text="Dia da Semana",font="Arial 40")
textoDiaSemana.pack()

listaNomes = ("Ana","Amanda","Cesar")

variavelNomes = Variable(value=listaNomes)

listboxExemplo = Listbox(janela,
                         listvariable=variavelNomes, 
                         height=6,
                         font="Arial 40",
                         selectmode=MULTIPLE)#Determina o numero de itens que podem ser selecionados(BROWSE/SINGLE/MULTIPLE/EXTENDED)

listboxExemplo.pack(expand=True,fill=BOTH)#Expande -> centraliza, Fill -> Expande(ocupa tela inteira)

def itemSelecionado(evento):
    indiceSelecionado = listboxExemplo.curselection()
    item = ",".join([listboxExemplo.get(posicao) for posicao in indiceSelecionado])
    mensagem = "Você selecionou: " + item
    messagebox.showinfo(title="Atenção!",message=mensagem)

listboxExemplo.bind("<<ListboxSelect>>", itemSelecionado)

textoParaAdicionar = Entry(font="Arial 40")
textoParaAdicionar.pack()

def addItem():
    listboxExemplo.insert(END,str(textoParaAdicionar.get()))

botaoAdicionar = Button(text="Adicionar Item Na Lista",font="Arial 20",command=addItem)
botaoAdicionar.pack()

janela.mainloop()


