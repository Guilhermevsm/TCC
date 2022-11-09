from tkinter import*
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

root = Tk()
root.title('Casima Agrícola')
root.iconbitmap('python.ico')
root.geometry("1000x600")

#conectando ao banco
try:
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "aneis1961",
        database = "casima"
    )
    #criando o cursor
    cursor = conexao.cursor()
    
    #dando commit
    conexao.commit()

    #fechando a conexa
    conexao.close()

    print("Conexão com o banco feita com sucesso!")
except Error as e:
    aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel se conectar ao banco de dados \nErro: " + str(e))
    print("Conexão com o banco não foi sucedida!")


#-----------------------------------------------------------------------------------------

def query_database(tabela):
    return





#-----------------------------------------------------------------------------------------

def selecionar_dadosar_arvore():
    cpf_entry.delete(0, END)
    nome_entry.delete(0, END)
    telefone_entry.delete(0, END)
    endereco_entry.delete(0, END)
    salario_entry.delete(0, END)
    carteira_trabalho_entry.delete(0, END)
    cargo_entry.delete(0, END)

    selecionado = my_tree.focus()

    valor = my_tree.item(selecionado, 'values')

    cpf_entry.insert(0, valor[0])
    nome_entry.insert(0, valor[1])
    telefone_entry.insert(0, valor[2])
    endereco_entry.insert(0, valor[3])
    salario_entry.insert(0, valor[4])
    carteira_trabalho_entry.insert(0, valor[5])
    cargo_entry.insert(0, valor[6])

#-----------------------------------------------------------------------------------------

#criando o frame para funcionarios
def janela_funcionarios():
    root.geometry("1150x500")
    
    #adicionando estilo
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map('Treeview', background=[('selected', "#347083")])

    global my_tree

    #criando frame da treeview
    frame_funcionarios = LabelFrame(root, text="Funcionários")
    frame_funcionarios.pack(pady=10)

    #criando o scroll da treeview
    tree_scroll = Scrollbar(frame_funcionarios)
    tree_scroll.pack(side=RIGHT, fill=Y)

    #criando a treeview
    my_tree = ttk.Treeview(frame_funcionarios, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    #configurando o scroll
    tree_scroll.config(command=my_tree.yview)

    #difinindo as colunas
    my_tree['columns'] = ("CPF", "Nome", "Telefone", "Endereço", "Salário", "Carteira Trab", "Cargo")
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("CPF", width=140, anchor=W)
    my_tree.column("Nome", width=300, anchor=W)
    my_tree.column("Telefone", width=100, anchor=CENTER)
    my_tree.column("Endereço", width=140, anchor=CENTER)
    my_tree.column("Salário", width=140, anchor=CENTER)
    my_tree.column("Carteira Trab", width=140, anchor=CENTER)
    my_tree.column("Cargo", width=140, anchor=CENTER)

    #criando as headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("CPF", text="Nome", anchor=W)
    my_tree.heading("Nome", text="Sobrenome", anchor=W)
    my_tree.heading("Telefone", text="ID", anchor=CENTER)
    my_tree.heading("Endereço", text="Endereço", anchor=CENTER)
    my_tree.heading("Salário", text="Cidade", anchor=CENTER)
    my_tree.heading("Carteira Trab", text="Estado", anchor=CENTER)
    my_tree.heading("Cargo", text="CEP", anchor=CENTER)



    #alternando as cores das linhas
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")



    #adicionando as caixas de entrada
    data_frame = LabelFrame(root, text="Funcionários")
    data_frame.pack(fill="x", expand="yes", padx=20)
    global cpf_entry
    cpf_label = Label(data_frame, text="CPF")
    cpf_label.grid(row=0, column=0, padx=10, pady=10)
    cpf_entry = Entry(data_frame)
    cpf_entry.grid(row=0, column=1, padx=10, pady=10)
    global nome_entry
    nome_label = Label(data_frame, text="Nome")
    nome_label.grid(row=0, column=2, padx=10, pady=10)
    nome_entry = Entry(data_frame)
    nome_entry.grid(row=0, column=3, padx=10, pady=10)
    global telefone_entry
    telefone_label = Label(data_frame, text="Telefone")
    telefone_label.grid(row=0, column=4, padx=10, pady=10)
    telefone_entry = Entry(data_frame)
    telefone_entry.grid(row=0, column=5, padx=10, pady=10)
    global endereco_entry
    endereco_label = Label(data_frame, text="Endereço")
    endereco_label.grid(row=1, column=0, padx=10, pady=10)
    endereco_entry = Entry(data_frame)
    endereco_entry.grid(row=1, column=1, padx=10, pady=10)
    global salario_entry
    salario_label = Label(data_frame, text="Salário")
    salario_label.grid(row=1, column=2, padx=10, pady=10)
    salario_entry = Entry(data_frame)
    salario_entry.grid(row=1, column=3, padx=10, pady=10)
    global carteira_trabalho_entry
    carteira_trabalho_label = Label(data_frame, text="Carteira Trab")
    carteira_trabalho_label.grid(row=1, column=4, padx=10, pady=10)
    carteira_trabalho_entry = Entry(data_frame)
    carteira_trabalho_entry.grid(row=1, column=5, padx=10, pady=10)
    global cargo_entry
    cargo_label = Label(data_frame, text="Cargo")
    cargo_label.grid(row=1, column=6, padx=10, pady=10)
    cargo_entry = Entry(data_frame)
    cargo_entry.grid(row=1, column=7, padx=10, pady=10)
    

    #adicionando botões
    button_frame = LabelFrame(root, text="Ações")
    button_frame.pack(fill="x", expand="yes", padx=20)

    update_button = Button(button_frame, text="Atualizar")
    update_button.grid(row=0 , column=0 , padx=10, pady=10)

    add_button = Button(button_frame, text="Adicionar")
    add_button.grid(row=0 , column=1 , padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remover")
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)


    clear_box_button = Button(button_frame, text="Limpar")
    clear_box_button.grid(row=0 , column=7 , padx=10, pady=10)

    #bind th treeview
    my_tree.bind("<ButtonRelease-1>", selecionar_dadosar_arvore)






#-----------------------------------------------------------------------------------------

#janela inicial
menu_principal = Menu(root)
root.config(menu=menu_principal)

#criando os itens do menu
menu_banco = Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Banco", menu=menu_banco)
menu_banco.add_command(label="Funcionários", command=janela_funcionarios)
menu_banco.add_command(label="Animais")
menu_banco.add_command(label="Vacinas")
menu_banco.add_command(label="Vacinação")
menu_banco.add_command(label="Estoque")
menu_banco.add_command(label="Problemas Gestação")
menu_banco.add_command(label="Gestações")
menu_banco.add_command(label="Fornecedores")
menu_banco.add_command(label="Transações")


menu_racao = Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ração", menu=menu_racao)
menu_racao.add_command(label="Mistura Ração")
menu_racao.add_separator()
menu_racao.add_command(label="Sair", command=root.quit)


root.mainloop()