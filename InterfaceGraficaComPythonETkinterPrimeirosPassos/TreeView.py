# %%
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

janela = Tk()
janela.geometry("950x350")
janela.title("Treeview")

id = Label(text="ID",font="Arial 12")
id.grid(row=1,column=0,sticky="W")
campoDigitavelId = Entry(font="Arial 12")
campoDigitavelId.grid(row=1,column=1,sticky="W")

#----------------------------------------------

nome = Label(text="Nome",font="Arial 12")
nome.grid(row=1,column=2,sticky="W")
campoDigitavelNome = Entry(font="Arial 12")
campoDigitavelNome.grid(row=1,column=3,sticky="W")

#----------------------------------------------

idade = Label(text="Idade",font="Arial 12")
idade.grid(row=1,column=4,sticky="W")
campoDigitavelIdade = Entry(font="Arial 12")
campoDigitavelIdade.grid(row=1,column=5,sticky="W")

#----------------------------------------------

sexo = Label(text="Sexo",font="Arial 12")
sexo.grid(row=1,column=6,sticky="W")
campoDigitavelSexo = Entry(font="Arial 12")
campoDigitavelSexo.grid(row=1,column=7,sticky="W")

#----------------------------------------------

def addItemTreeview():
    if str(campoDigitavelId.get())=="":
        print("Digite algo no campo ID")
    elif str(campoDigitavelNome.get())=="":
        print("Digite algo no campo Nome")
    elif str(campoDigitavelIdade.get())=="":
        print("Digite algo no campo Idade")
    elif str(campoDigitavelSexo.get())=="":
        print("Digite algo no campo Sexo")
    else:    
        treeViewDados.insert("","end",
                             values=(str(campoDigitavelId.get()),
                                     str(campoDigitavelNome.get()),
                                     str(campoDigitavelIdade.get()),
                                     str(campoDigitavelSexo.get())))
    
        campoDigitavelNome.delete(0,"end")
        campoDigitavelIdade.delete(0,"end")
        campoDigitavelSexo.delete(0,"end")
        campoDigitavelId.delete(0,"end")

        contarNumeroLinhas()

botaoAdicionar = Button(text="Cadastrar",
                        font="Arial 20",
                        command=addItemTreeview)

botaoAdicionar.grid(row=2,column=0,columnspan=2,sticky="NSEW")

estiloDaTreeview = ttk.Style()
estiloDaTreeview.theme_use("alt")#alt, default, classic
estiloDaTreeview.configure(".",font="Arial 14")

treeViewDados = ttk.Treeview(janela, columns=(1,2,3,4),show="headings")

treeViewDados.column("1",anchor=CENTER)
treeViewDados.heading("1",text="ID")

treeViewDados.column("2",anchor=CENTER)
treeViewDados.heading("2",text="Nome")

treeViewDados.column("3",anchor=CENTER)
treeViewDados.heading("3",text="Idade")

treeViewDados.column("4",anchor=CENTER)
treeViewDados.heading("4",text="Sexo")

treeViewDados.insert("","end",text="1",values=("1","Bruno Pereira","36","Masculino"))
treeViewDados.insert("","end",text="2",values=("2","Chloé Silva","02","Feminino"))
treeViewDados.insert("","end",text="3",values=("3","Miguel Pereira","13","Masculino"))
treeViewDados.insert("","end",text="4",values=("4","Deyse Danielle","12","Feminino"))
treeViewDados.insert("","end",text="5",values=("5","Ana Vidal","65","Feminino"))

treeViewDados.grid(row=3, column=0, columnspan=8,sticky="NSEW")

labelNumeroLinhas = Label(text="Linhas:",font="Arial 20")
labelNumeroLinhas.grid(row=4, column=0, columnspan=8,sticky="W")

def contarNumeroLinhas(item=""):
    numeroDelinhas = 0
    linhas = treeViewDados.get_children(item)
    for linha in linhas:
        numeroDelinhas += 1

    labelNumeroLinhas.config(text="Linhas: "+str(numeroDelinhas))

contarNumeroLinhas()

def deletarItemTreeview():
    itensSelecionados = treeViewDados.selection()
    for item in itensSelecionados:
        treeViewDados.delete(item)
    
    contarNumeroLinhas()

botaoDeletar = Button(text="Deletar",
                        font="Arial 20",
                        command=deletarItemTreeview)

botaoDeletar.grid(row=2,column=2,columnspan=2,sticky="NSEW")

def alterarItemTreeview():
    if str(campoDigitavelId.get())=="":
        print("Digite algo no campo ID")
    elif str(campoDigitavelNome.get())=="":
        print("Digite algo no campo Nome")
    elif str(campoDigitavelIdade.get())=="":
        print("Digite algo no campo Idade")
    elif str(campoDigitavelSexo.get())=="":
        print("Digite algo no campo Sexo")
    else:    
        itemSelecionado = treeViewDados.selection()[0]
        treeViewDados.item(itemSelecionado,
                        values=(str(campoDigitavelId.get()),
                                str(campoDigitavelNome.get()),
                                str(campoDigitavelIdade.get()),
                                str(campoDigitavelSexo.get())))
        contarNumeroLinhas()

botaoAlterar = Button(text="Alterar",
                        font="Arial 20",
                        command=alterarItemTreeview)

botaoAlterar.grid(row=2,column=4,columnspan=2,sticky="NSEW")

from openpyxl import load_workbook
import os

def exportarParaExcel():
    workbook = load_workbook(filename="Tratamento_Dados.xlsx")
    sheet = workbook["Vendedores"]

    for numeroLinha in treeViewDados.get_children():
        linha = treeViewDados.item(numeroLinha)["values"]
        sheet.append(linha)

    workbook.save(filename="Dados_Exportados.xlsx")

    os.startfile("Dados_Exportados.xlsx")


botaoExportar = Button(text="Exportar",
                        font="Arial 20",
                        command=exportarParaExcel)

botaoExportar.grid(row=2,column=6,columnspan=2,sticky="NSEW")

janela.mainloop()


