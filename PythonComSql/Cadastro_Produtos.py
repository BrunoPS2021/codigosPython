import pyodbc
from tkinter import *
from tkinter import ttk

def verifica_credenciais():
    conexao = pyodbc.connect("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto_Compras.db;Trusted_connection=yes;DNS=dns")

    cursor = conexao.cursor()
    cursor.execute("select * from Usuarios where Nome = ? and Senha = ?",(
        nome_usuario_entry.get(),
        senha_entry.get()
    ))    
    usuario = cursor.fetchall()

    if usuario:
        janela_principal.destroy()
        def listar_dados():
            for i in treeview.get_children():
                treeview.delete(i)

            cursor.execute("Select * from Produtos")
            valores = cursor.fetchall()

            for valor in valores:
                treeview.insert('', 'end', values=(valor[0], valor[1], valor[2], valor[3]))
        
        janela = Tk()
        janela.title("Cadastro de Produtos")
        janela.configure(bg="#f5f5f5")
        janela.attributes("-fullscreen",True)

        Label(janela,text="Nome do Produto: ", 
            font="Arial 16",bg="#f5f5f5").grid(row=0,column=2,padx=10,pady=10)
        nome_produto = Entry(janela,font=("Arial",16))
        nome_produto.grid(row=0,column=3,padx=10,pady=10)

        Label(janela,text="Descrição do Produto: ", 
            font="Arial 16",bg="#f5f5f5").grid(row=0,column=5,padx=10,pady=10)
        descricao_produto = Entry(janela,font=("Arial",16))
        descricao_produto.grid(row=0,column=6,padx=10,pady=10)

        Label(janela,text="Produtos",fg='blue', 
            font="Arial 16",
            bg="#f5f5f5").grid(row=2,column=0,columnspan=10,padx=10,pady=10)
        
        def cadastrar():
            janela_cadastrar = Toplevel(janela)
            janela_cadastrar.title("Cadastrar Produto")
            janela_cadastrar.configure(bg='#ffffff')

            largura_janela = 450
            altura_janela = 230

            largura_tela = janela_cadastrar.winfo_screenwidth()
            altura_tela = janela_cadastrar.winfo_screenheight()

            pos_x = (largura_tela // 2) - (largura_janela // 2)
            pos_y = (altura_tela // 2) - (altura_janela // 2)

            janela_cadastrar.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela,pos_x,pos_y))

            for i in range(5):
                janela_cadastrar.grid_rowconfigure(i,weight=1)

            for j in range(2):
                janela_cadastrar.grid_columnconfigure(j,weight=1)

            estilo_borda = {"borderwidth":2,"relief":"groove"}
            Label(janela_cadastrar, text='Nome do Produto: ',
                    font=("Arial",12),
                    bg="#ffffff").grid(row=0,column=0,padx=10,pady=10, sticky='w')
            nome_produto_cadastrar = Entry(janela_cadastrar,
                                font=("Arial",12),
                                **estilo_borda)
            nome_produto_cadastrar.grid(row=0,column=1,padx=10,pady=10)

            Label(janela_cadastrar, text='Descrição do Produto: ',
                    font=("Arial",12),
                    bg="#ffffff").grid(row=1,column=0,padx=10,pady=10, sticky='w')
            descricao_produto_cadastrar = Entry(janela_cadastrar,
                                font=("Arial",12),
                                **estilo_borda)
            descricao_produto_cadastrar.grid(row=1,column=1,padx=10,pady=10)

            Label(janela_cadastrar, text='Preço do Produto: ',
                        font=("Arial",12),
                        bg="#ffffff").grid(row=2,column=0,padx=10,pady=10, sticky='w')
            preco_produto_cadastrar = Entry(janela_cadastrar,
                                font=("Arial",12),
                                **estilo_borda)
            preco_produto_cadastrar.grid(row=2,column=1,padx=10,pady=10)

            def salvar_dados():
                novo_produto_cadastrar = (nome_produto_cadastrar.get(),
                descricao_produto_cadastrar.get(),
                preco_produto_cadastrar.get())

                cursor.execute("Insert into Produtos (NomeProduto,Descricao,Preco) values (?,?,?)",novo_produto_cadastrar)
                conexao.commit()

                print("Dados Cadastrados com sucesso!")

                janela_cadastrar.destroy()

                listar_dados()

            botao_salvar_dados = Button(janela_cadastrar,text="Salvar",
                            font=("Arial",12),command=salvar_dados)
            botao_salvar_dados.grid(row=3,column=0,columnspan=2,padx=10,pady=10,sticky='nsew')

            botao_cancelar_dados = Button(janela_cadastrar,text="Cancelar",
                            font=("Arial",12),command=janela_cadastrar.destroy)
            botao_cancelar_dados.grid(row=4,column=0,columnspan=2,padx=10,pady=10,sticky='nsew')

        botao_gravar = Button(janela,text='Novo',command=cadastrar,font=("Arial",26))
        botao_gravar.grid(row=4,column=0,columnspan=4,sticky='nsew',pady=5,padx=20)

        style = ttk.Style(janela)
        treeview = ttk.Treeview(janela,style="mystyle.Treeview")
        style.theme_use("default")
        style.configure("mystyle.Treeview",font=('Arial', 14))
        treeview = ttk.Treeview(janela,style="mystyle.Treeview",
                        columns=("Id","NomeProduto","Descricao","Preco"),
                        show='headings',height=20)

        treeview.heading("Id",text='ID')
        treeview.heading("NomeProduto",text='Nome do Produto')
        treeview.heading("Descricao",text='Descrição')
        treeview.heading("Preco",text='Preço')

        treeview.column("#0",width=0,stretch=NO)
        treeview.column("Id",width=100)
        treeview.column("NomeProduto",width=300)
        treeview.column("Descricao",width=500)
        treeview.column("Preco",width=200)

        treeview.grid(row=3,column=0,columnspan=10, sticky="nsew")

        listar_dados()

        def editar_dados(event):
            item_selecionado = treeview.selection()[0]

            valores_selecionados = treeview.item(item_selecionado)['values']

            print(valores_selecionados)

            janela_edicao = Toplevel(janela)
            janela_edicao.title("Editar Produto")
            janela_edicao.configure(bg='#ffffff')

            largura_janela = 450
            altura_janela = 200

            largura_tela = janela_edicao.winfo_screenwidth()
            altura_tela = janela_edicao.winfo_screenheight()

            pos_x = (largura_tela // 2) - (largura_janela // 2)
            pos_y = (altura_tela // 2) - (altura_janela // 2)

            janela_edicao.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela,pos_x,pos_y))

            for i in range(5):
                janela_edicao.grid_rowconfigure(i,weight=1)

            for j in range(2):
                janela_edicao.grid_columnconfigure(j,weight=1)

            estilo_borda = {"borderwidth":2,"relief":"groove"}
            Label(janela_edicao, text='Nome do Produto: ',
                    font=("Arial",12),
                    bg="#ffffff").grid(row=0,column=0,padx=10,pady=10, sticky='w')
            nome_produto_edicao = Entry(janela_edicao,
                                font=("Arial",16),
                                **estilo_borda,bg="#FFFFFF",
                                textvariable=StringVar(value=valores_selecionados[1]))
            nome_produto_edicao.grid(row=0,column=1,padx=10,pady=10)

            Label(janela_edicao, text='Descrição do Produto: ',
                    font=("Arial",12),
                    bg="#ffffff").grid(row=1,column=0,padx=10,pady=10, sticky='w')
            descricao_produto_edicao = Entry(janela_edicao,
                                            font=("Arial",16),
                                            **estilo_borda,bg="#FFFFFF",
                                            textvariable=StringVar(value=valores_selecionados[2]))
            descricao_produto_edicao.grid(row=1,column=1,padx=10,pady=10)

            Label(janela_edicao, text='Preço do Produto: ',
                        font=("Arial",12),
                        bg="#ffffff").grid(row=2,column=0,padx=10,pady=10, sticky='w')
            preco_produto_edicao = Entry(janela_edicao,
                                font=("Arial",16),
                                **estilo_borda,bg="#FFFFFF",
                                textvariable=StringVar(value=valores_selecionados[3]))
            preco_produto_edicao.grid(row=2,column=1,padx=10,pady=10)

            def salvar_edicao():
                novo_produto = nome_produto_edicao.get()
                nova_descricao = descricao_produto_edicao.get()
                novo_preco = preco_produto_edicao.get()

                treeview.item(item_selecionado,values=(valores_selecionados[0],novo_produto,nova_descricao,novo_preco))
    
                cursor.execute("update Produtos set NomeProduto = ? , Descricao = ?, Preco = ? where Id = ?",novo_produto,nova_descricao,novo_preco,valores_selecionados[0])
                conexao.commit()
    
                print("Dados alterados com sucesso!")
    
                janela_edicao.destroy()

                listar_dados()

            botao_salvar_edicao = Button(janela_edicao,text="Salvar",
                            bg="#008000",fg="#ffffff",
                            font=("Arial",12),command=salvar_edicao)
            botao_salvar_edicao.grid(row=4,column=0,padx=20,pady=20)

            def deletar_registro():
                selected_item = treeview.selection()[0]
                id = treeview.item(selected_item)['values'][0]
                cursor.execute("delete from Produtos where Id=?",id)
                conexao.commit()
                janela_edicao.destroy()
                listar_dados()

            botao_deletar_edicao = Button(janela_edicao,text="Deletar",
                            font=("Arial",16),bg="#ff0000",fg="#ffffff",
                            command=deletar_registro)
            botao_deletar_edicao.grid(row=4,column=1,padx=20,pady=20)

        treeview.bind("<Double-1>",editar_dados)

        menu_bar = Menu(janela)
        janela.configure(menu=menu_bar)
        menu_arquivo = Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)
        menu_arquivo.add_command(label="Cadastrar",command=cadastrar)
        menu_arquivo.add_command(label="Sair",command=janela.destroy)

        def limparDados():
            for i in treeview.get_children():
                treeview.delete(i)

        def filtrar_dados(nome_produto,descricao_produto):
            if not nome_produto.get() and descricao_produto.get():
                listar_dados()
                return

            sql = "Select * from Produtos"

            params = []

            if nome_produto.get():
                sql += " where NomeProduto like ?"
                params.append('%'+nome_produto.get()+'%')

            if descricao_produto.get():
                if nome_produto.get():
                    sql += " AND"
                else:
                    sql += " where"
            sql += " Descricao like ?"
            params.append('%' + descricao_produto.get() + '%')

            cursor.execute(sql,tuple(params))
            produtos = cursor.fetchall()

            limparDados()

            for dado in produtos:
                treeview.insert('','end',values=(dado[0],dado[1],dado[2],dado[3]))

        nome_produto.bind("<KeyRelease>",lambda e: filtrar_dados(nome_produto,descricao_produto))
        descricao_produto.bind("<KeyRelease>",lambda e: filtrar_dados(nome_produto,descricao_produto))

        def deletar():
            selected_item = treeview.selection()[0]
            id = treeview.item(selected_item)['values'][0]
            cursor.execute("delete from Produtos where Id=?",id)
            conexao.commit()
            listar_dados()
        
        botao_deletar = Button(janela,text='Deletar',command=deletar,font=("Arial",26))
        botao_deletar.grid(row=4,column=4,columnspan=4,sticky='nsew',pady=5,padx=20)

        janela.mainloop()

        cursor.close()
        conexao.close()

    else:
        mensagem_lbl = Label(janela_principal,text="Nome de usuário ou senha incorretos",
                            fg='red')
        mensagem_lbl.grid(row=3,column=0,columnspan=2)

janela_principal = Tk()
janela_principal.title("Tela de Login")
janela_principal.configure(bg='#f5f5f5')

largura_janela = 450
altura_janela = 300

largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()

pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)

janela_principal.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela,pos_x,pos_y))

titulo_lbl = Label(janela_principal,text='Tela de Login',
                font=("Arial",20),
                fg='blue',
                bg='#f5f5f5')
titulo_lbl.grid(row=0,column=0,columnspan=2,pady=20)

nome_usuario_lbl = Label(janela_principal,text="Nome de Usuário: ",
                        font=("Arial",14,'bold'),
                        bg='#f5f5f5')
nome_usuario_lbl.grid(row=1,column=0,sticky='e')

senha_lbl = Label(janela_principal,text="Senha: ",
                        font=("Arial",14,'bold'),
                        bg='#f5f5f5')
senha_lbl.grid(row=2,column=0,sticky='e')

nome_usuario_entry = Entry(janela_principal,font=("Arial",14))
nome_usuario_entry.grid(row=1,column=1,pady=10)

senha_entry = Entry(janela_principal,show='*',font=("Arial",14))
senha_entry.grid(row=2,column=1,pady=10)

entrar_btn = Button(janela_principal,
                    text='Entrar',font=("Arial",14),
                    command=verifica_credenciais)
entrar_btn.grid(row=4,column=0,columnspan=2,padx=20,pady=10,sticky='nsew')

sair_btn = Button(janela_principal,
                    text='Sair',font=("Arial",14),
                    command=janela_principal.destroy)
sair_btn.grid(row=5,column=0,columnspan=2,padx=20,pady=10,sticky='nsew')

for i in range(5):
    janela_principal.grid_rowconfigure(i,weight=1)

for j in range(2):
    janela_principal.grid_columnconfigure(j,weight=1)

janela_principal.mainloop()