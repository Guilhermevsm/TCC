from tkinter import*
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from scipy.optimize import linprog
import csv

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

    #print("Conexão com o banco feita com sucesso!")
except Error as e:
    aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel se conectar ao banco de dados \nErro: " + str(e))
    #print("Conexão com o banco não foi sucedida!")

#-----------------------------------------------------------------------------------------

def cria_menu():
    #janela inicial
    global menu_principal
    global menu_banco
    global menu_racao
    menu_principal = Menu(root)
    root.config(menu=menu_principal)

    #criando os itens do menu
    menu_banco = Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(label="Banco", menu=menu_banco)
    menu_banco.add_command(label="Funcionários", command=janela_funcionarios)
    menu_banco.add_command(label="Animais", command=janela_animais)
    menu_banco.add_command(label="Vacinas", command=janela_vacinas)
    menu_banco.add_command(label="Vacinação", command=janela_vacinacao)
    menu_banco.add_command(label="Estoque", command=janela_estoque)
    menu_banco.add_command(label="Problemas Gestação", command=janela_problemas_gestacao)
    menu_banco.add_command(label="Gestações", command=janela_gestacao)
    menu_banco.add_command(label="Fornecedores", command=janela_fornecedores)
    menu_banco.add_command(label="Transações", command=janela_transacao)

    menu_views = Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(label="Views", menu=menu_views)
    menu_views.add_command(label="Animais Vacinados", command=janela_vacinados)
    menu_views.add_command(label="Decendentes", command=janela_filhos)

    menu_racao = Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(label="Ração", menu=menu_racao)
    menu_racao.add_command(label="Mistura Ração", command=janela_simplex)

    menu_backup = Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(label="Backup", menu=menu_backup)
    menu_backup.add_command(label="Fazer Backup", command=fazer_backup)
    menu_backup.add_command(label="Restaurar Backup")
    menu_backup.add_separator()
    menu_backup.add_command(label="Sair", command=root.quit)


#-----------------------------------------------------------------------------------------

#pegando os itens do banco de dados e colocando na arvore
def query_database(tabela):
    #print(tabela)
    for item in my_tree.get_children():
        my_tree.delete(item)
    try:
        conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "aneis1961",
            database = "casima"
        )
        #criando o cursor
        cursor = conexao.cursor()
    except Error as e:
        aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel se conectar ao banco de dados \nErro: " + str(e))
        
    global num
    if tabela == "funcionarios":   
        cursor.execute("SELECT * FROM funcionarios")
        dados = cursor.fetchall()
        #print(dados) 
        num = 0
        for itens in dados:
            if num % 2 == 0:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2], dados[num][3], dados[num][4], dados[num][5], dados[num][6]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2], dados[num][3], dados[num][4], dados[num][5], dados[num][6]), tags=('oddrow', ))
            num += 1
        
    elif tabela == "animais":   
        cursor.execute("SELECT * FROM animais")
        dados = cursor.fetchall()
        #print(dados)
        num = 0
        for itens in dados:
            if num % 2 == 0:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2], dados[num][3], dados[num][4], dados[num][5], dados[num][6]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2], dados[num][3], dados[num][4], dados[num][5], dados[num][6]), tags=('oddrow', ))
            num += 1

    elif tabela == "vacinas":   
        cursor.execute("SELECT * FROM vacinas")
        dados = cursor.fetchall()
        #print(dados)
        num = 0
        for itens in dados:
            if num % 2 == 0:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2]), tags=('oddrow', ))
            num += 1

    elif tabela == "vacinacao":   
        cursor.execute("SELECT * FROM vacinacao")
        dados = cursor.fetchall()
        #print(dados)
        num = 0
        for itens in dados:
            if num % 2 == 0:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2], dados[num][3]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2], dados[num][3]), tags=('oddrow', ))
            num += 1

    elif tabela == "estoque":   
        cursor.execute("SELECT * FROM estoque")
        dados = cursor.fetchall()
        #print(dados)
        num = 0
        for itens in dados:
            if num % 2 == 0:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2]), tags=('oddrow', ))
            num += 1

    elif tabela == "problemas_gestacao":   
        cursor.execute("SELECT * FROM problemas_gestacao")
        dados = cursor.fetchall()
        #print(dados)
        num = 0
        for itens in dados:
            if num % 2 == 0:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2]), tags=('oddrow', ))
            num += 1


    elif tabela == "gestacao":   
        cursor.execute("SELECT * FROM gestacao")
        dados = cursor.fetchall()
        #print(dados)
        num = 0
        for itens in dados:
            if num % 2 == 0:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2], dados[num][3], dados[num][4]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2], dados[num][3], dados[num][4]), tags=('oddrow', ))
            num += 1

    elif tabela == "fornecedores":   
        cursor.execute("SELECT * FROM fornecedores")
        dados = cursor.fetchall()
        #print(dados)
        num = 0
        for itens in dados:
            if num % 2 == 0:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2], dados[num][3], dados[num][4]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2], dados[num][3], dados[num][4]), tags=('oddrow', ))
            num += 1

    elif tabela == "transacao":   
        cursor.execute("SELECT * FROM transacao")
        dados = cursor.fetchall()
        #print(dados)
        num = 0
        for itens in dados:
            if num % 2 == 0:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2], dados[num][3], dados[num][4], dados[num][5]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2], dados[num][3], dados[num][4], dados[num][5]), tags=('oddrow', ))
            num += 1
    
    elif tabela == "vacinados":   
        cursor.execute("SELECT * FROM vacinados")
        dados = cursor.fetchall()
        #print(dados)
        num = 0
        for itens in dados:
            if num % 2 == 0:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][2], dados[num][3]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][2], dados[num][3]), tags=('oddrow', ))
            num += 1

    elif tabela == "animal_vacinado":
        animal = vacinados_tag_entry.get()
        
        try:
            cursor.execute("SELECT * FROM vacinados WHERE tag = %s ", (animal, ))
        except Error as e:
            aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel se conectar ao banco de dados \nErro: " + str(e))
            print("Conexão com o banco não foi sucedida!")
        dados = cursor.fetchall()

        num = 0
        for itens in dados:
            if num % 2 == 0:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][2], dados[num][3]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][2], dados[num][3]), tags=('oddrow', ))
            num += 1


    #dando commit
    conexao.commit()

    #fechando a conexa
    conexao.close()
    

#-----------------------------------------------------------------------------------------

#atualizar dados existentes
def atualizar_dados(tabela):
    response = messagebox.askyesno(title="Atualizar",  message="Confirmar Alterações?")
    if response == 1:
        
        try:
            conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "aneis1961",
            database = "casima"
        )
        except Error as e:
            aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel se conectar ao banco de dados \nErro: " + str(e))
        cursor = conexao.cursor()
        
        if tabela == "animais":
            #atualizando o banco
            sql = "UPDATE animais SET tag = %s, tipo = %s, data_nascimento = %s, peso = %s, sexo = %s, mae_tag = %s, pai_tag = %s WHERE tag = %s "

            tag = str(tag_entry.get())
            tipo = str(tipo_entry.get())
            data_nascimento = str(data_nascimento_entry.get())
            peso = str(peso_entry.get())
            sexo = str(sexo_entry.get())
            mae_tag = str(mae_tag_entry.get())
            pai_tag = str(pai_tag_entry.get())

            dados = (tag, tipo, data_nascimento, peso, sexo, mae_tag, pai_tag, tag)
            try:
                cursor.execute(sql, dados)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível salvar as alterações \nErro: " + str(e))
            #dando commit
            conexao.commit()
            #fechando a conexao
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("animais")
        
        elif tabela == "funcionarios":
            #atualizando o banco
            sql = "UPDATE funcionarios SET nome = %s, telefone = %s, endereco = %s, salario = %s, carteira_trabalho = %s, cargo = %s WHERE cpf = %s "

            cpf = str(cpf_entry.get())
            nome = str(nome_entry.get())
            telefone = str(telefone_entry.get())
            endereco = str(endereco_entry.get())
            salario = str(salario_entry.get())
            carteira_trabalho = str(carteira_trabalho_entry.get())
            cargo = str(cargo_entry.get())

            dados = (nome, telefone, endereco, salario, carteira_trabalho, cargo, cpf)
            try:
                cursor.execute(sql, dados)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível salvar as alterações \nErro: " + str(e))
            #dando commit
            conexao.commit()
            #fechando a conexao
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("funcionarios")

        elif tabela == "vacinas":
            #atualizando o banco
            sql = "UPDATE vacinas SET nome = %s, reforco = %s WHERE id = %s "

            id_vacina = str(id_vacina_entry.get())
            nome_vacina = str(nome_vacina_entry.get())
            reforco = str(reforco_entry.get())

            dados = (nome_vacina, reforco, id_vacina)
            try:
                cursor.execute(sql, dados)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível salvar as alterações \nErro: " + str(e))
            #dando commit
            conexao.commit()
            #fechando a conexao
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("vacinas")


        elif tabela == "vacinacao":
            #atualizando o banco
            sql = "UPDATE vacinacao SET vacina_id = %s, animais_tag = %s, data = %s WHERE id = %s "

            id = str(id_vacinacao_entry.get())
            vacinafk_id = str(vacinafk_id_entry.get())
            animaisfk_tag = str(animaisfk_tag_entry.get())
            data_vacinacao = str(data_vacinacao_entry.get())

            dados = (vacinafk_id, animaisfk_tag, data_vacinacao, id)
            try:
                cursor.execute(sql, dados)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível salvar as alterações \nErro: " + str(e))
            #dando commit
            conexao.commit()
            #fechando a conexao
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("vacinacao")


        elif tabela == "estoque":
            #atualizando o banco
            sql = "UPDATE estoque SET item = %s, quantidade = %s WHERE id = %s "

            id = str(id_estoque_entry.get())
            item = str(item_entry.get())
            quantidade = str(quantidade_entry.get())

            dados = (item, quantidade, id)
            try:
                cursor.execute(sql, dados)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível salvar as alterações \nErro: " + str(e))
            #dando commit
            conexao.commit()
            #fechando a conexao
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("estoque")


        elif tabela == "problemas_gestacao":
            #atualizando o banco
            sql = "UPDATE problemas_gestacao SET nome = %s, descricao = %s WHERE id = %s "

            id = str(id_prob_gest_entry.get())
            nome = str(nome_prob_gest_entry.get())
            descricao = str(descricao_prob_gest_entry.get())

            dados = (nome, descricao, id)
            try:
                cursor.execute(sql, dados)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível salvar as alterações \nErro: " + str(e))
            #dando commit
            conexao.commit()
            #fechando a conexao
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("problemas_gestacao")


        elif tabela == "gestacao":
            #atualizando o banco
            sql = "UPDATE gestacao SET a_tag = %s, pg_id = %s, descricao = %s, data = %s WHERE id = %s "

            id = str(id_gestacao_entry.get())
            a_tag = str(gestacao_tag_entry.get())
            pg_id = str(pgid_gestacao_entry.get())
            descricao = str(descricao_gestacao_entry.get())
            data = str(data_gestacao_entry.get())

            dados = (a_tag, pg_id, descricao, data, id)
            try:
                cursor.execute(sql, dados)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível salvar as alterações \nErro: " + str(e))
            #dando commit
            conexao.commit()
            #fechando a conexao
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("gestacao")

        
        elif tabela == "fornecedores":
            #atualizando o banco
            sql = "UPDATE fornecedores SET nome = %s, cidade = %s, endereco = %s, telefone = %s WHERE cnpj = %s "

            cnpj = str(cnpj_fornecedor_entry.get())
            nome = str(nome_fornecedor_entry.get())
            cidade = str(cidade_fornecedor_entry.get())
            endereco = str(endereco_fornecedor_entry.get())
            telefone = str(telefone_fornecedor_entry.get())

            dados = (nome, cidade, endereco, telefone, cnpj)
            try:
                cursor.execute(sql, dados)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível salvar as alterações \nErro: " + str(e))
            #dando commit
            conexao.commit()
            #fechando a conexao
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("forncedores")


        elif tabela == "transacao":
            #atualizando o banco
            sql = "UPDATE transacao SET f_id = %s, e_id = %s, data = %s, quantidade = %s, valor_unitario = %s WHERE id = %s "

            id = str(id_transacao_entry.get())
            f_id = str(f_id_transacao_entry.get())
            e_id = str(e_id_transacao_entry.get())
            data = str(data_transacao_entry.get())
            quantidade = str(quantidade_transacao_entry.get())
            valor_unitario = str(valor_unitario_transacao_entry.get())

            dados = (f_id, e_id, data, quantidade, valor_unitario, id)
            try:
                cursor.execute(sql, dados)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível salvar as alterações \nErro: " + str(e))
            #dando commit
            conexao.commit()
            #fechando a conexao
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("transacao")
        
        
        
           
    else:
        aviso = messagebox.showinfo(title="Update", message="Nada foi alterado")
    

#-----------------------------------------------------------------------------------------

#deletando item do banco
def remover(tabela, pk, pk_entry):
    response = messagebox.askyesno(title="Deletar",  message="Confirmar Remoção?")
    if response == 1:
        
        try:
            conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "aneis1961",
            database = "casima"
        )
        except Error as e:
            aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel se conectar ao banco de dados \nErro: " + str(e))
        
        cursor = conexao.cursor()
        
        sql = "DELETE FROM %s WHERE %s = %s"
        tabela = str(tabela)
        primary_key = str(pk)
        primary_key_value = int(pk_entry)
        dados = (tabela, primary_key, primary_key_value)
        print(dados)
        try:
            cursor.execute(sql, dados)
            #cursor.execute()
            #cursor.execute("DELETE FROM animais WHERE tag=11")
        except Error as a:
            aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel remover o item \nErro: " + str(a))
        
        #dando commit
        conexao.commit()

        #fechando a conexao
        conexao.close()
        my_tree.delete(*my_tree.get_children())
        query_database(tabela)
    

#-----------------------------------------------------------------------------------------

#adicionar dados ao banco
def adicionar_ao_banco(tabela):
    response = messagebox.askyesno(title="Adicionar",  message="Confirmar Adição?")
    if response == 1:
        try:
            conexao = mysql.connector.connect(
                host = "localhost",
                user = "root",
                passwd = "aneis1961",
                database = "casima"
            )
            #criando o cursor
            cursor = conexao.cursor()
        except Error as e:
            aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel se conectar ao banco de dados \nErro: " + str(e))
        
        if tabela == "funcionarios":
            sql = "INSERT INTO funcionarios (cpf, nome, telefone, endereco, salario, carteira_trabalho, cargo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            valores = (str(cpf_entry.get()), str(nome_entry.get()), str(telefone_entry.get()), str(endereco_entry.get()), str(salario_entry.get()), str(carteira_trabalho_entry.get()), str(cargo_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

            conexao.commit()
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("funcionarios")

        elif tabela == "animais":
            sql = "INSERT INTO animais (tag, tipo, data_nascimento, peso, sexo, mae_tag, pai_tag) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            valores = (str(tag_entry.get()), str(tipo_entry.get()), str(data_nascimento_entry.get()), str(peso_entry.get()), str(sexo_entry.get()), str(mae_tag_entry.get()), str(pai_tag_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

            conexao.commit()
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("animais")

        elif tabela == "vacinas":
            sql = "INSERT INTO vacinas (id, nome, reforco) VALUES (%s, %s, %s)"
            valores = (str(id_vacina_entry.get()), str(nome_vacina_entry.get()), str(reforco_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

            conexao.commit()
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("vacinas")

        elif tabela == "vacinacao":
            sql = "INSERT INTO vacinacao (id, vacina_id, animais_tag, data) VALUES (%s, %s, %s, %s)"
            valores = (str(id_vacinacao_entry.get()), str(vacinafk_id_entry.get()), str(animaisfk_tag_entry.get()), str(data_vacinacao_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

            conexao.commit()
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("vacinacao")

        elif tabela == "estoque":
            sql = "INSERT INTO estoque (id, item, quantidade) VALUES (%s, %s, %s)"
            valores = (str(id_estoque_entry.get()), str(item_entry.get()), str(quantidade_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

            conexao.commit()
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("estoque")

        elif tabela == "problemas_gestacao":
            sql = "INSERT INTO problemas_gestacao (id, nome, descricao) VALUES (%s, %s, %s)"
            valores = (str(id_prob_gest_entry.get()), str(nome_prob_gest_entry.get()), str(descricao_prob_gest_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

            conexao.commit()
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("problemas_gestacao")

        elif tabela == "gestacao":
            sql = "INSERT INTO gestacao (id, a_tag, pg_id, descricao, data) VALUES (%s, %s, %s, %s, %s)"
            valores = (str(id_gestacao_entry.get()), str(gestacao_tag_entry.get()), str(pgid_gestacao_entry.get()), str(descricao_gestacao_entry.get()), str(data_gestacao_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

            conexao.commit()
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("gestacao")

        elif tabela == "fornecedores":
            sql = "INSERT INTO fornecedores (cnpj, nome, cidade, endereco, telefone) VALUES (%s, %s, %s, %s, %s)"
            valores = (str(cnpj_fornecedor_entry.get()), str(nome_fornecedor_entry.get()), str(cidade_fornecedor_entry.get()), str(endereco_fornecedor_entry.get()), str(telefone_fornecedor_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

            conexao.commit()
            conexao.close()
            my_tree.delete(*my_tree.get_children())
            query_database("fornecedores")
            

        elif tabela == "transacao":
            sql = "INSERT INTO transacao (id, f_id, e_id, data, quantidade, valor_unitario) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (str(id_transacao_entry.get()), str(f_id_transacao_entry.get()), str(e_id_transacao_entry.get()), str(data_transacao_entry.get()), str(quantidade_transacao_entry.get()), str(valor_unitario_transacao_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

            my_tree.delete(*my_tree.get_children())
            conexao.commit()
            conexao.close()
            query_database("transacao")



#-----------------------------------------------------------------------------------------

#janela para fazer um backup do banco em um arquivo csv
def fazer_backup():
    try:
        conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "aneis1961",
            database = "casima"
        )
        #criando o cursor
        cursor = conexao.cursor()
    except Error as e:
        aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel se conectar ao banco de dados \nErro: " + str(e))

    tabelas = ["animais", "funcionarios", "vacinas", "vacinacao", "estoque", "problemas_gestacao", "gestacao", "fornecedores", "transacao"]
    
    for nome in tabelas:
        if nome == "animais":
            try:
                cursor.execute("SELECT * FROM animais")
            except Error as e:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
            resultado = cursor.fetchall()
            with open('backup.csv', 'a', newline='') as arquivo_backup:
                arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                arquivo_backup.writerow(nome)
                for item in resultado:
                    arquivo_backup.writerow(item)

        elif nome == "funcionarios":
            try:
                cursor.execute("SELECT * FROM funcionarios")
            except Error as e:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
            resultado = cursor.fetchall()
            with open('backup.csv', 'a', newline='') as arquivo_backup:
                arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                arquivo_backup.writerow(nome)
                for item in resultado:
                    arquivo_backup.writerow(item)

        elif nome == "vacinas":
            try:
                cursor.execute("SELECT * FROM vacinas")
            except Error as e:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
            resultado = cursor.fetchall()
            with open('backup.csv', 'a', newline='') as arquivo_backup:
                arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                arquivo_backup.writerow(nome)
                for item in resultado:
                    arquivo_backup.writerow(item)

        elif nome == "vacinacao":
            try:
                cursor.execute("SELECT * FROM vacinacao")
            except Error as e:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
            resultado = cursor.fetchall()
            with open('backup.csv', 'a', newline='') as arquivo_backup:
                arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                arquivo_backup.writerow(nome)
                for item in resultado:
                    arquivo_backup.writerow(item)

        elif nome == "estoque":
            try:
                cursor.execute("SELECT * FROM estoque")
            except Error as e:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
            resultado = cursor.fetchall()
            with open('backup.csv', 'a', newline='') as arquivo_backup:
                arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                arquivo_backup.writerow(nome)
                for item in resultado:
                    arquivo_backup.writerow(item)

        elif nome == "problemas_gestacao":
            try:
                cursor.execute("SELECT * FROM problemas_gestacao")
            except Error as e:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
            resultado = cursor.fetchall()
            with open('backup.csv', 'a', newline='') as arquivo_backup:
                arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                arquivo_backup.writerow(nome)
                for item in resultado:
                    arquivo_backup.writerow(item)

        elif nome == "gestacao":
            try:
                cursor.execute("SELECT * FROM gestacao")
            except Error as e:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
            resultado = cursor.fetchall()
            with open('backup.csv', 'a', newline='') as arquivo_backup:
                arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                arquivo_backup.writerow(nome)
                for item in resultado:
                    arquivo_backup.writerow(item)

        elif nome == "fornecedores":
            try:
                cursor.execute("SELECT * FROM fornecedores")
            except Error as e:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
            resultado = cursor.fetchall()
            with open('backup.csv', 'a', newline='') as arquivo_backup:
                arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                arquivo_backup.writerow(nome)
                for item in resultado:
                    arquivo_backup.writerow(item)

        elif nome == "transacao":
            try:
                cursor.execute("SELECT * FROM transacao")
            except Error as e:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
            resultado = cursor.fetchall()
            with open('backup.csv', 'a', newline='') as arquivo_backup:
                arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                arquivo_backup.writerow(nome)
                for item in resultado:
                    arquivo_backup.writerow(item)

    conexao.commit()
    conexao.close()
    aviso = messagebox.showinfo(title="Backup", message="Backup feito com sucesso!")



#-----------------------------------------------------------------------------------------

#criando janela do simplex
def janela_simplex():
    for widgets in root.winfo_children():
        widgets.destroy()
    cria_menu()
    root.geometry("500x300")

    #função simplex
    def simplex():
        #indices da função de MINIMIZAR
        C = [ingrediente1_entry.get(), ingrediente2_entry.get(), ingrediente3_entry.get()]
        #Au é a matriz contendo os indices da equacoes condicionais do tipo MENOR IGUAL
        Au = [
            [-3, -1, -3],
            [1, -1, 0]
        ]
        #vetor b das equações de MENOR IGUAL
        Bu = [-6, 1]
        #Ae é a matriz contendo os indices das equações condicionais do tipo IGUALDADE
        Ae = [
            [3, 2, 0]
        ]
        #Vetor b das equações de IGUALDADE
        Be = [6]
        resultado = linprog(C, A_ub=Au, b_ub=Bu, A_eq=Ae, b_eq=Be, bounds=None, method='simplex')
        #print(resultado)
        
        #fun é o valor otimizado
        # x: array são os valores de x que otimizão a função
        #nit é o numero de interções

        resposta_label = Label(frame_simplex, text="Quantidade de ingrediente 1 = " + str(resultado['x'][0]) + " Kg\nQuantidade de ingrediente 2 = " + str(resultado['x'][1]) + " Kg\nQuantidade de ingrediente 3 = " + str(resultado['x'][2]) + " Kg")
        resposta_label.grid(row=3, column=0, columnspan=4, rowspan=3)

    #criando frame do simplex
    frame_simplex = Frame(root)
    frame_simplex.pack(pady=10)

    ingrediente1_label = Label(frame_simplex, text="Ingrediente 1")
    ingrediente1_label.grid(row=0, column=0, pady=10, padx=(10,0))
    ingrediente1_entry = Entry(frame_simplex)
    ingrediente1_entry.grid(row=0, column=1, pady=10)

    ingrediente2_label = Label(frame_simplex, text="Ingrediente 2")
    ingrediente2_label.grid(row=0, column=2, pady=10, padx=(10,0))
    ingrediente2_entry = Entry(frame_simplex)
    ingrediente2_entry.grid(row=0, column=3, pady=10)

    ingrediente3_label = Label(frame_simplex, text="Ingrediente 3")
    ingrediente3_label.grid(row=1, column=0, pady=10, padx=(10,0))
    ingrediente3_entry = Entry(frame_simplex)
    ingrediente3_entry.grid(row=1, column=1, pady=10)

    ingrediente4_label = Label(frame_simplex, text="Ingrediente 4")
    ingrediente4_label.grid(row=1, column=2, pady=10, padx=(10,0))
    ingrediente4_entry = Entry(frame_simplex)
    ingrediente4_entry.grid(row=1, column=3, pady=10)

    botao_calcular = Button(frame_simplex, text="Calcular", command=simplex)
    botao_calcular.grid(row=2, column=0, pady=10, padx=10)
    
#-----------------------------------------------------------------------------------------

#criando o frame para funcionarios
def janela_funcionarios():
    for widgets in root.winfo_children():
        widgets.destroy()
    cria_menu()
    def selecionar_dados_arvore(e):
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

    root.geometry("1300x500")
    
    #adicionando estilo
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map('Treeview', background=[('selected', "#347083")])

    global my_tree

    #criando frame da treeview
    frame_funcionarios = Frame(root)
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
    my_tree.column("Endereço", width=300, anchor=CENTER)
    my_tree.column("Salário", width=140, anchor=CENTER)
    my_tree.column("Carteira Trab", width=140, anchor=CENTER)
    my_tree.column("Cargo", width=140, anchor=CENTER)

    #criando as headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("CPF", text="CPF", anchor=W)
    my_tree.heading("Nome", text="Nome", anchor=W)
    my_tree.heading("Telefone", text="Telefone", anchor=CENTER)
    my_tree.heading("Endereço", text="Endereço", anchor=CENTER)
    my_tree.heading("Salário", text="Salário", anchor=CENTER)
    my_tree.heading("Carteira Trab", text="Carteira Trab", anchor=CENTER)
    my_tree.heading("Cargo", text="Cargo", anchor=CENTER)

    #alternando as cores das linhas
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    #adicionando as caixas de entrada
    data_frame = LabelFrame(root, text="Funcionários")
    data_frame.pack(fill="x", expand="yes", padx=20)
    global cpf_entry
    cpf_label = Label(data_frame, text="CPF")
    cpf_label.grid(row=0, column=3, padx=10, pady=10)
    cpf_entry = Entry(data_frame)
    cpf_entry.grid(row=0, column=4, padx=10, pady=10)
    global nome_entry
    nome_label = Label(data_frame, text="Nome")
    nome_label.grid(row=0, column=0, padx=10, pady=10)
    nome_entry = Entry(data_frame, width=50)
    nome_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
    global telefone_entry
    telefone_label = Label(data_frame, text="Telefone")
    telefone_label.grid(row=0, column=5, padx=10, pady=10)
    telefone_entry = Entry(data_frame)
    telefone_entry.grid(row=0, column=6, padx=10, pady=10)
    global endereco_entry
    endereco_label = Label(data_frame, text="Endereço")
    endereco_label.grid(row=1, column=0, padx=10, pady=10)
    endereco_entry = Entry(data_frame, width=50)
    endereco_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
    global salario_entry
    salario_label = Label(data_frame, text="Salário")
    salario_label.grid(row=1, column=3, padx=10, pady=10)
    salario_entry = Entry(data_frame)
    salario_entry.grid(row=1, column=4, padx=10, pady=10)
    global carteira_trabalho_entry
    carteira_trabalho_label = Label(data_frame, text="Carteira Trab")
    carteira_trabalho_label.grid(row=1, column=5, padx=10, pady=10)
    carteira_trabalho_entry = Entry(data_frame)
    carteira_trabalho_entry.grid(row=1, column=6, padx=10, pady=10)
    global cargo_entry
    cargo_label = Label(data_frame, text="Cargo")
    cargo_label.grid(row=1, column=7, padx=10, pady=10)
    cargo_entry = Entry(data_frame)
    cargo_entry.grid(row=1, column=8, padx=10, pady=10)
    
    query_database("funcionarios")

    #adicionando botões
    button_frame = LabelFrame(root, text="Ações")
    button_frame.pack(fill="x", expand="yes", padx=20)

    update_button = Button(button_frame, text="Atualizar", command=lambda:adicionar_ao_banco("funcionarios"))
    update_button.grid(row=0 , column=0 , padx=10, pady=10)

    add_button = Button(button_frame, text="Adicionar", command=lambda:adicionar_ao_banco("funcionarios"))
    add_button.grid(row=0 , column=1 , padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("funcionarios","cpf", str(cpf_entry.get())))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)


    clear_box_button = Button(button_frame, text="Limpar")
    clear_box_button.grid(row=0 , column=7 , padx=10, pady=10)

    #bind th treeview
    my_tree.bind("<ButtonRelease-1>", selecionar_dados_arvore)

#-----------------------------------------------------------------------------------------

#criando a janela para tabela animais
def janela_animais():
    for widgets in root.winfo_children():
        widgets.destroy()
    cria_menu()
    def selecionar_dados_arvore(e):
        tag_entry.delete(0, END)
        tipo_entry.delete(0, END)
        data_nascimento_entry.delete(0, END)
        peso_entry.delete(0, END)
        sexo_entry.delete(0, END)
        mae_tag_entry.delete(0, END)
        pai_tag_entry.delete(0, END)

        selecionado = my_tree.focus()

        valor = my_tree.item(selecionado, 'values')

        tag_entry.insert(0, valor[0])
        tipo_entry.insert(0, valor[1])
        data_nascimento_entry.insert(0, valor[2])
        peso_entry.insert(0, valor[3])
        sexo_entry.insert(0, valor[4])
        mae_tag_entry.insert(0, valor[5])
        pai_tag_entry.insert(0, valor[6])

    root.geometry("1030x500")
    
    #adicionando estilo
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map('Treeview', background=[('selected', "#347083")])

    global my_tree

    #criando frame da treeview
    frame_animais = Frame(root)
    frame_animais.pack(pady=10)

    #criando o scroll da treeview
    tree_scroll = Scrollbar(frame_animais)
    tree_scroll.pack(side=RIGHT, fill=Y)

    #criando a treeview
    my_tree = ttk.Treeview(frame_animais, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    #configurando o scroll
    tree_scroll.config(command=my_tree.yview)

    #difinindo as colunas
    my_tree['columns'] = ("TAG", "Tipo", "Nascimento", "Peso", "Sexo", "Mãe", "Pai")
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("TAG", width=140, anchor=W)
    my_tree.column("Tipo", width=140, anchor=W)
    my_tree.column("Nascimento", width=140, anchor=CENTER)
    my_tree.column("Peso", width=140, anchor=CENTER)
    my_tree.column("Sexo", width=140, anchor=CENTER)
    my_tree.column("Mãe", width=140, anchor=CENTER)
    my_tree.column("Pai", width=140, anchor=CENTER)

    #criando as headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("TAG", text="TAG", anchor=W)
    my_tree.heading("Tipo", text="Tipo", anchor=W)
    my_tree.heading("Nascimento", text="Nascimento", anchor=CENTER)
    my_tree.heading("Peso", text="Peso", anchor=CENTER)
    my_tree.heading("Sexo", text="Sexo", anchor=CENTER)
    my_tree.heading("Mãe", text="Mãe", anchor=CENTER)
    my_tree.heading("Pai", text="Pai", anchor=CENTER)

    #alternando as cores das linhas
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    #adicionando as caixas de entrada
    data_frame = LabelFrame(root, text="Animais")
    data_frame.pack(fill="x", expand="yes", padx=20)
    global tag_entry
    tag_label = Label(data_frame, text="TAG")
    tag_label.grid(row=0, column=0, padx=10, pady=10)
    tag_entry = Entry(data_frame)
    tag_entry.grid(row=0, column=1, padx=10, pady=10)
    global tipo_entry
    tipo_label = Label(data_frame, text="Tipo")
    tipo_label.grid(row=0, column=2, padx=10, pady=10)
    tipo_entry = Entry(data_frame)
    tipo_entry.grid(row=0, column=3, padx=10, pady=10)
    global data_nascimento_entry
    data_nascimento_label = Label(data_frame, text="Data Nascimento")
    data_nascimento_label.grid(row=0, column=4, padx=10, pady=10)
    data_nascimento_entry = Entry(data_frame)
    data_nascimento_entry.grid(row=0, column=5, padx=10, pady=10)
    global peso_entry
    peso_label = Label(data_frame, text="Peso")
    peso_label.grid(row=1, column=0, padx=10, pady=10)
    peso_entry = Entry(data_frame)
    peso_entry.grid(row=1, column=1, padx=10, pady=10)
    global sexo_entry
    sexo_label = Label(data_frame, text="Sexo")
    sexo_label.grid(row=1, column=2, padx=10, pady=10)
    sexo_entry = Entry(data_frame)
    sexo_entry.grid(row=1, column=3, padx=10, pady=10)
    global mae_tag_entry
    mae_tag_label = Label(data_frame, text="Mãe")
    mae_tag_label.grid(row=1, column=4, padx=10, pady=10)
    mae_tag_entry = Entry(data_frame)
    mae_tag_entry.grid(row=1, column=5, padx=10, pady=10)
    global pai_tag_entry
    pai_tag_label = Label(data_frame, text="Pai")
    pai_tag_label.grid(row=1, column=6, padx=10, pady=10)
    pai_tag_entry = Entry(data_frame)
    pai_tag_entry.grid(row=1, column=7, padx=10, pady=10)
    
    query_database("animais")

    #adicionando botões
    button_frame = LabelFrame(root, text="Ações")
    button_frame.pack(fill="x", expand="yes", padx=20)

    update_button = Button(button_frame, text="Atualizar", command=lambda:atualizar_dados("animais"))
    update_button.grid(row=0 , column=0 , padx=10, pady=10)

    add_button = Button(button_frame, text="Adicionar", command=lambda:adicionar_ao_banco("animais"))
    add_button.grid(row=0 , column=1 , padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("animais","tag", tag_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

    clear_box_button = Button(button_frame, text="Limpar")
    clear_box_button.grid(row=0 , column=7 , padx=10, pady=10)

    #bind th treeview
    my_tree.bind("<ButtonRelease-1>", selecionar_dados_arvore)


#-----------------------------------------------------------------------------------------

#criando janela de vacinas
def janela_vacinas():
    for widgets in root.winfo_children():
        widgets.destroy()
    cria_menu()
    def selecionar_dados_arvore(e):
        id_vacina_entry.delete(0, END)
        nome_vacina_entry.delete(0, END)
        reforco_entry.delete(0, END)
        

        selecionado = my_tree.focus()

        valor = my_tree.item(selecionado, 'values')

        id_vacina_entry.insert(0, valor[0])
        nome_vacina_entry.insert(0, valor[1])
        reforco_entry.insert(0, valor[2])
        
    root.geometry("910x470")
    
    #adicionando estilo
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map('Treeview', background=[('selected', "#347083")])

    global my_tree

    #criando frame da treeview
    frame_vacinas = Frame(root)
    frame_vacinas.pack(pady=10)

    #criando o scroll da treeview
    tree_scroll = Scrollbar(frame_vacinas)
    tree_scroll.pack(side=RIGHT, fill=Y)

    #criando a treeview
    my_tree = ttk.Treeview(frame_vacinas, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    #configurando o scroll
    tree_scroll.config(command=my_tree.yview)

    #difinindo as colunas
    my_tree['columns'] = ("ID", "Nome", "Reforço")
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ID", width=80, anchor=W)
    my_tree.column("Nome", width=150, anchor=W)
    my_tree.column("Reforço", width=600, anchor=CENTER)
    
    #criando as headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ID", text="ID", anchor=W)
    my_tree.heading("Nome", text="Nome", anchor=W)
    my_tree.heading("Reforço", text="Reforço", anchor=CENTER)
    
    #alternando as cores das linhas
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    #adicionando as caixas de entrada
    data_frame = LabelFrame(root, text="Vacinas")
    data_frame.pack(fill="x", expand="yes", padx=20)
    global id_vacina_entry
    id_vacina_label = Label(data_frame, text="ID")
    id_vacina_label.grid(row=0, column=0, padx=10, pady=10)
    id_vacina_entry = Entry(data_frame)
    id_vacina_entry.grid(row=0, column=1, padx=10, pady=10)
    global nome_vacina_entry
    nome_vacina_label = Label(data_frame, text="Nome")
    nome_vacina_label.grid(row=0, column=2, padx=10, pady=10)
    nome_vacina_entry = Entry(data_frame)
    nome_vacina_entry.grid(row=0, column=3, padx=10, pady=10)
    global reforco_entry
    reforco_label = Label(data_frame, text="Reforço")
    reforco_label.grid(row=0, column=4, padx=10, pady=10)
    reforco_entry = Entry(data_frame, width=60)
    reforco_entry.grid(row=0, column=5, padx=10, pady=10, columnspan=8)
    
    query_database("vacinas")

    #adicionando botões
    button_frame = LabelFrame(root, text="Ações")
    button_frame.pack(fill="x", expand="yes", padx=20)

    update_button = Button(button_frame, text="Atualizar", command=lambda:atualizar_dados("vacinas"))
    update_button.grid(row=0 , column=0 , padx=10, pady=10)

    add_button = Button(button_frame, text="Adicionar", command=lambda:adicionar_ao_banco("vacinas"))
    add_button.grid(row=0 , column=1 , padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("vacinas","id", id_vacina_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

    clear_box_button = Button(button_frame, text="Limpar")
    clear_box_button.grid(row=0 , column=7 , padx=10, pady=10)

    #bind th treeview
    my_tree.bind("<ButtonRelease-1>", selecionar_dados_arvore)

#-----------------------------------------------------------------------------------------

#criando a janela para tabela de vacinacao
def janela_vacinacao():
    for widgets in root.winfo_children():
        widgets.destroy()
    cria_menu()
    def selecionar_dados_arvore(e):
        id_vacinacao_entry.delete(0, END)
        vacinafk_id_entry.delete(0, END)
        animaisfk_tag_entry.delete(0, END)
        data_vacinacao_entry.delete(0, END)
        

        selecionado = my_tree.focus()

        valor = my_tree.item(selecionado, 'values')

        id_vacinacao_entry.insert(0, valor[0])
        vacinafk_id_entry.insert(0, valor[1])
        animaisfk_tag_entry.insert(0, valor[2])
        data_vacinacao_entry.insert(0, valor[3])
        
    root.geometry("1000x500")
    
    #adicionando estilo
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map('Treeview', background=[('selected', "#347083")])

    global my_tree

    #criando frame da treeview
    frame_vacinacao = Frame(root)
    frame_vacinacao.pack(pady=10)

    #criando o scroll da treeview
    tree_scroll = Scrollbar(frame_vacinacao)
    tree_scroll.pack(side=RIGHT, fill=Y)

    #criando a treeview
    my_tree = ttk.Treeview(frame_vacinacao, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    #configurando o scroll
    tree_scroll.config(command=my_tree.yview)

    #difinindo as colunas
    my_tree['columns'] = ("ID", "Vacina", "Animal", "Data")
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ID", width=100, anchor=W)
    my_tree.column("Vacina", width=180, anchor=W)
    my_tree.column("Animal", width=140, anchor=CENTER)
    my_tree.column("Data", width=140, anchor=CENTER)
    
    #criando as headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ID", text="ID", anchor=W)
    my_tree.heading("Vacina", text="Vacina", anchor=W)
    my_tree.heading("Animal", text="Animal", anchor=CENTER)
    my_tree.heading("Data", text="Data", anchor=CENTER)   

    #alternando as cores das linhas
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    #adicionando as caixas de entrada
    data_frame = LabelFrame(root, text="Vacinação")
    data_frame.pack(fill="x", expand="yes", padx=20)
    global id_vacinacao_entry
    id_vacinacao_label = Label(data_frame, text="ID")
    id_vacinacao_label.grid(row=0, column=0, padx=10, pady=10)
    id_vacinacao_entry = Entry(data_frame)
    id_vacinacao_entry.grid(row=0, column=1, padx=10, pady=10)
    global vacinafk_id_entry
    vacinafk_id_label = Label(data_frame, text="Vacina")
    vacinafk_id_label.grid(row=0, column=2, padx=10, pady=10)
    vacinafk_id_entry = Entry(data_frame)
    vacinafk_id_entry.grid(row=0, column=3, padx=10, pady=10)
    global animaisfk_tag_entry
    animaisfk_tag_label = Label(data_frame, text="Animal")
    animaisfk_tag_label.grid(row=0, column=4, padx=10, pady=10)
    animaisfk_tag_entry = Entry(data_frame)
    animaisfk_tag_entry.grid(row=0, column=5, padx=10, pady=10)
    global data_vacinacao_entry
    data_vacinacao_label = Label(data_frame, text="Data")
    data_vacinacao_label.grid(row=0, column=6, padx=10, pady=10)
    data_vacinacao_entry = Entry(data_frame)
    data_vacinacao_entry.grid(row=0, column=7, padx=10, pady=10)
    
    query_database("vacinacao")

    #adicionando botões
    button_frame = LabelFrame(root, text="Ações")
    button_frame.pack(fill="x", expand="yes", padx=20)

    update_button = Button(button_frame, text="Atualizar", command=lambda:atualizar_dados("vacinacao"))
    update_button.grid(row=0 , column=0 , padx=10, pady=10)

    add_button = Button(button_frame, text="Adicionar", command=lambda:adicionar_ao_banco("vacinacao"))
    add_button.grid(row=0 , column=1 , padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("vacinacao","id", id_vacinacao_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

    clear_box_button = Button(button_frame, text="Limpar")
    clear_box_button.grid(row=0 , column=7 , padx=10, pady=10)

    #bind th treeview
    my_tree.bind("<ButtonRelease-1>", selecionar_dados_arvore)

#-----------------------------------------------------------------------------------------

#criando o frame para funcionarios
def janela_estoque():
    for widgets in root.winfo_children():
        widgets.destroy()
    cria_menu()
    def selecionar_dados_arvore(e):
        id_estoque_entry.delete(0, END)
        item_entry.delete(0, END)
        quantidade_entry.delete(0, END)
        

        selecionado = my_tree.focus()

        valor = my_tree.item(selecionado, 'values')

        id_estoque_entry.insert(0, valor[0])
        item_entry.insert(0, valor[1])
        quantidade_entry.insert(0, valor[2])
        
    root.geometry("900x500")
    
    #adicionando estilo
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map('Treeview', background=[('selected', "#347083")])

    global my_tree

    #criando frame da treeview
    frame_estoque = Frame(root)
    frame_estoque.pack(pady=10)

    #criando o scroll da treeview
    tree_scroll = Scrollbar(frame_estoque)
    tree_scroll.pack(side=RIGHT, fill=Y)

    #criando a treeview
    my_tree = ttk.Treeview(frame_estoque, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    #configurando o scroll
    tree_scroll.config(command=my_tree.yview)

    #difinindo as colunas
    my_tree['columns'] = ("ID", "Item", "Quantidade")
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ID", width=140, anchor=W)
    my_tree.column("Item", width=300, anchor=W)
    my_tree.column("Quantidade", width=100, anchor=CENTER)
    
    #criando as headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ID", text="ID", anchor=W)
    my_tree.heading("Item", text="Item", anchor=W)
    my_tree.heading("Quantidade", text="Quantidade", anchor=CENTER)
    
    #alternando as cores das linhas
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    #adicionando as caixas de entrada
    data_frame = LabelFrame(root, text="Estoque")
    data_frame.pack(fill="x", expand="yes", padx=20)
    global id_estoque_entry
    id_estoque_label = Label(data_frame, text="ID")
    id_estoque_label.grid(row=0, column=0, padx=10, pady=10)
    id_estoque_entry = Entry(data_frame)
    id_estoque_entry.grid(row=0, column=2, padx=10, pady=10)
    global item_entry
    item_label = Label(data_frame, text="Item")
    item_label.grid(row=0, column=3, padx=10, pady=10)
    item_entry = Entry(data_frame, width=50)
    item_entry.grid(row=0, column=4, padx=10, pady=10, columnspan=2)
    global quantidade_entry
    quantidade_label = Label(data_frame, text="Quantidade")
    quantidade_label.grid(row=0, column=6, padx=10, pady=10)
    quantidade_entry = Entry(data_frame)
    quantidade_entry.grid(row=0, column=7, padx=10, pady=10)
    
    query_database("estoque")

    #adicionando botões
    button_frame = LabelFrame(root, text="Ações")
    button_frame.pack(fill="x", expand="yes", padx=20)

    update_button = Button(button_frame, text="Atualizar", command=lambda:atualizar_dados("estoque"))
    update_button.grid(row=0 , column=0 , padx=10, pady=10)

    add_button = Button(button_frame, text="Adicionar", command=lambda:adicionar_ao_banco("estoque"))
    add_button.grid(row=0 , column=1 , padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("estoque","id", id_estoque_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)


    clear_box_button = Button(button_frame, text="Limpar")
    clear_box_button.grid(row=0 , column=7 , padx=10, pady=10)

    #bind th treeview
    my_tree.bind("<ButtonRelease-1>", selecionar_dados_arvore)

#-----------------------------------------------------------------------------------------

#criando a janela para problemas gestacao
def janela_problemas_gestacao():
    for widgets in root.winfo_children():
        widgets.destroy()
    cria_menu()
    def selecionar_dados_arvore(e):
        id_prob_gest_entry.delete(0, END)
        nome_prob_gest_entry.delete(0, END)
        descricao_prob_gest_entry.delete(0, END)
        

        selecionado = my_tree.focus()

        valor = my_tree.item(selecionado, 'values')

        id_prob_gest_entry.insert(0, valor[0])
        nome_prob_gest_entry.insert(0, valor[1])
        descricao_prob_gest_entry.insert(0, valor[2])
        
    root.geometry("1030x500")
    
    #adicionando estilo
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map('Treeview', background=[('selected', "#347083")])

    global my_tree

    #criando frame da treeview
    frame_prob_gest = Frame(root)
    frame_prob_gest.pack(pady=10)

    #criando o scroll da treeview
    tree_scroll = Scrollbar(frame_prob_gest)
    tree_scroll.pack(side=RIGHT, fill=Y)

    #criando a treeview
    my_tree = ttk.Treeview(frame_prob_gest, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    #configurando o scroll
    tree_scroll.config(command=my_tree.yview)

    #difinindo as colunas
    my_tree['columns'] = ("ID", "Problema", "Descrição")
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ID", width=100, anchor=W)
    my_tree.column("Problema", width=300, anchor=W)
    my_tree.column("Descrição", width=600, anchor=CENTER)
    
    #criando as headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ID", text="ID", anchor=W)
    my_tree.heading("Problema", text="Problema", anchor=W)
    my_tree.heading("Descrição", text="Descrição", anchor=CENTER)
    
    #alternando as cores das linhas
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    #adicionando as caixas de entrada
    data_frame = LabelFrame(root, text="Problemas de Gestação")
    data_frame.pack(fill="x", expand="yes", padx=20)
    global id_prob_gest_entry
    id_prob_gest_label = Label(data_frame, text="ID")
    id_prob_gest_label.grid(row=0, column=0, padx=10, pady=10)
    id_prob_gest_entry = Entry(data_frame)
    id_prob_gest_entry.grid(row=0, column=1, padx=10, pady=10)
    global nome_prob_gest_entry
    nome_prob_gest_label = Label(data_frame, text="Problema")
    nome_prob_gest_label.grid(row=0, column=2, padx=10, pady=10)
    nome_prob_gest_entry = Entry(data_frame, width=50)
    nome_prob_gest_entry.grid(row=0, column=3, padx=10, pady=10)
    global descricao_prob_gest_entry
    descricao_prob_gest_label = Label(data_frame, text="Descrição")
    descricao_prob_gest_label.grid(row=1, column=0, padx=10, pady=10)
    descricao_prob_gest_entry = Entry(data_frame, width=88)
    descricao_prob_gest_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=4, sticky=W)
    
    
    query_database("problemas_gestacao")

    #adicionando botões
    button_frame = LabelFrame(root, text="Ações")
    button_frame.pack(fill="x", expand="yes", padx=20)

    update_button = Button(button_frame, text="Atualizar", command=lambda:atualizar_dados("problemas_gestacao"))
    update_button.grid(row=0 , column=0 , padx=10, pady=10)

    add_button = Button(button_frame, text="Adicionar", command=lambda:adicionar_ao_banco("problemas_gestacao"))
    add_button.grid(row=0 , column=1 , padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("problemas_gestacao","id", id_prob_gest_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)


    clear_box_button = Button(button_frame, text="Limpar")
    clear_box_button.grid(row=0 , column=7 , padx=10, pady=10)

    #bind th treeview
    my_tree.bind("<ButtonRelease-1>", selecionar_dados_arvore)

#-----------------------------------------------------------------------------------------

#criando a janela para tabela gestação
def janela_gestacao():
    for widgets in root.winfo_children():
        widgets.destroy()
    cria_menu()
    def selecionar_dados_arvore(e):
        id_gestacao_entry.delete(0, END)
        gestacao_tag_entry.delete(0, END)
        pgid_gestacao_entry.delete(0, END)
        descricao_gestacao_entry.delete(0, END)
        data_gestacao_entry.delete(0, END)
        

        selecionado = my_tree.focus()

        valor = my_tree.item(selecionado, 'values')

        id_gestacao_entry.insert(0, valor[0])
        gestacao_tag_entry.insert(0, valor[1])
        pgid_gestacao_entry.insert(0, valor[2])
        descricao_gestacao_entry.insert(0, valor[3])
        data_gestacao_entry.insert(0, valor[4])   

    root.geometry("1030x500")
    
    #adicionando estilo
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map('Treeview', background=[('selected', "#347083")])

    global my_tree

    #criando frame da treeview
    frame_gestacao = Frame(root)
    frame_gestacao.pack(pady=10)

    #criando o scroll da treeview
    tree_scroll = Scrollbar(frame_gestacao)
    tree_scroll.pack(side=RIGHT, fill=Y)

    #criando a treeview
    my_tree = ttk.Treeview(frame_gestacao, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    #configurando o scroll
    tree_scroll.config(command=my_tree.yview)

    #difinindo as colunas
    my_tree['columns'] = ("ID", "Animal", "Problema", "Descrição", "Data")
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ID", width=100, anchor=W)
    my_tree.column("Animal", width=100, anchor=W)
    my_tree.column("Problema", width=140, anchor=CENTER)
    my_tree.column("Descrição", width=300, anchor=CENTER)
    my_tree.column("Data", width=140, anchor=CENTER)
    
    #criando as headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ID", text="ID", anchor=W)
    my_tree.heading("Animal", text="Animal", anchor=W)
    my_tree.heading("Problema", text="Problema", anchor=CENTER)
    my_tree.heading("Descrição", text="Descrição", anchor=CENTER)
    my_tree.heading("Data", text="Data", anchor=CENTER)
    
    #alternando as cores das linhas
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    #adicionando as caixas de entrada
    data_frame = LabelFrame(root, text="Gestação")
    data_frame.pack(fill="x", expand="yes", padx=20)
    global id_gestacao_entry
    id_gestacao_label = Label(data_frame, text="ID")
    id_gestacao_label.grid(row=0, column=0, padx=10, pady=10)
    id_gestacao_entry = Entry(data_frame)
    id_gestacao_entry.grid(row=0, column=1, padx=10, pady=10)
    global gestacao_tag_entry
    gestacao_tag_label = Label(data_frame, text="Animal")
    gestacao_tag_label.grid(row=0, column=2, padx=10, pady=10)
    gestacao_tag_entry = Entry(data_frame)
    gestacao_tag_entry.grid(row=0, column=3, padx=10, pady=10)
    global pgid_gestacao_entry
    pgid_gestacao_label = Label(data_frame, text="Problema")
    pgid_gestacao_label.grid(row=0, column=4, padx=10, pady=10)
    pgid_gestacao_entry = Entry(data_frame)
    pgid_gestacao_entry.grid(row=0, column=5, padx=10, pady=10)
    global descricao_gestacao_entry
    descricao_gestacao_label = Label(data_frame, text="Descrição")
    descricao_gestacao_label.grid(row=1, column=0, padx=10, pady=10)
    descricao_gestacao_entry = Entry(data_frame)
    descricao_gestacao_entry.grid(row=1, column=1, padx=10, pady=10)
    global data_gestacao_entry
    data_gestacao_label = Label(data_frame, text="Data")
    data_gestacao_label.grid(row=1, column=2, padx=10, pady=10)
    data_gestacao_entry = Entry(data_frame)
    data_gestacao_entry.grid(row=1, column=3, padx=10, pady=10)
    
    query_database("gestacao")

    #adicionando botões
    button_frame = LabelFrame(root, text="Ações")
    button_frame.pack(fill="x", expand="yes", padx=20)

    update_button = Button(button_frame, text="Atualizar", command=lambda:atualizar_dados("gestacao"))
    update_button.grid(row=0 , column=0 , padx=10, pady=10)

    add_button = Button(button_frame, text="Adicionar", command=lambda:adicionar_ao_banco("gestacao"))
    add_button.grid(row=0 , column=1 , padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("gestacao","id", id_gestacao_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

    clear_box_button = Button(button_frame, text="Limpar")
    clear_box_button.grid(row=0 , column=7 , padx=10, pady=10)

    #bind th treeview
    my_tree.bind("<ButtonRelease-1>", selecionar_dados_arvore)


#-----------------------------------------------------------------------------------------

#criando a janela para tabela fornecedores
def janela_fornecedores():
    for widgets in root.winfo_children():
        widgets.destroy()
    cria_menu()
    def selecionar_dados_arvore(e):
        cnpj_fornecedor_entry.delete(0, END)
        nome_fornecedor_entry.delete(0, END)
        cidade_fornecedor_entry.delete(0, END)
        endereco_fornecedor_entry.delete(0, END)
        telefone_fornecedor_entry.delete(0, END)
        
        selecionado = my_tree.focus()

        valor = my_tree.item(selecionado, 'values')

        cnpj_fornecedor_entry.insert(0, valor[0])
        nome_fornecedor_entry.insert(0, valor[1])
        cidade_fornecedor_entry.insert(0, valor[2])
        endereco_fornecedor_entry.insert(0, valor[3])
        telefone_fornecedor_entry.insert(0, valor[4])
        
    root.geometry("1030x500")
    
    #adicionando estilo
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map('Treeview', background=[('selected', "#347083")])

    global my_tree

    #criando frame da treeview
    frame_fornecedores = Frame(root)
    frame_fornecedores.pack(pady=10)

    #criando o scroll da treeview
    tree_scroll = Scrollbar(frame_fornecedores)
    tree_scroll.pack(side=RIGHT, fill=Y)

    #criando a treeview
    my_tree = ttk.Treeview(frame_fornecedores, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    #configurando o scroll
    tree_scroll.config(command=my_tree.yview)

    #difinindo as colunas
    my_tree['columns'] = ("CNPJ", "Nome", "Cidade", "Endereço", "Telefone")
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("CNPJ", width=140, anchor=W)
    my_tree.column("Nome", width=300, anchor=W)
    my_tree.column("Cidade", width=140, anchor=CENTER)
    my_tree.column("Endereço", width=300, anchor=CENTER)
    my_tree.column("Telefone", width=140, anchor=CENTER)
    
    #criando as headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("CNPJ", text="CNPJ", anchor=W)
    my_tree.heading("Nome", text="Nome", anchor=W)
    my_tree.heading("Cidade", text="Cidade", anchor=CENTER)
    my_tree.heading("Endereço", text="Endereço", anchor=CENTER)
    my_tree.heading("Telefone", text="Telefone", anchor=CENTER)
    
    #alternando as cores das linhas
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    #adicionando as caixas de entrada
    data_frame = LabelFrame(root, text="Animais")
    data_frame.pack(fill="x", expand="yes", padx=20)
    global cnpj_fornecedor_entry
    cnpj_fornecedor_label = Label(data_frame, text="CNPJ")
    cnpj_fornecedor_label.grid(row=0, column=0, padx=10, pady=10)
    cnpj_fornecedor_entry = Entry(data_frame)
    cnpj_fornecedor_entry.grid(row=0, column=1, padx=10, pady=10)
    global nome_fornecedor_entry
    nome_fornecedor_label = Label(data_frame, text="Nome")
    nome_fornecedor_label.grid(row=0, column=2, padx=10, pady=10)
    nome_fornecedor_entry = Entry(data_frame)
    nome_fornecedor_entry.grid(row=0, column=3, padx=10, pady=10)
    global cidade_fornecedor_entry
    cidade_fornecedor_label = Label(data_frame, text="Cidade")
    cidade_fornecedor_label.grid(row=0, column=4, padx=10, pady=10)
    cidade_fornecedor_entry = Entry(data_frame)
    cidade_fornecedor_entry.grid(row=0, column=5, padx=10, pady=10)
    global endereco_fornecedor_entry
    endereco_fornecedor_label = Label(data_frame, text="Endereço")
    endereco_fornecedor_label.grid(row=1, column=0, padx=10, pady=10)
    endereco_fornecedor_entry = Entry(data_frame, width=55)
    endereco_fornecedor_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=3)
    global telefone_fornecedor_entry
    telefone_fornecedor_label = Label(data_frame, text="Telefone")
    telefone_fornecedor_label.grid(row=1, column=4, padx=10, pady=10)
    telefone_fornecedor_entry = Entry(data_frame)
    telefone_fornecedor_entry.grid(row=1, column=5, padx=10, pady=10)
    
    query_database("fornecedores")

    #adicionando botões
    button_frame = LabelFrame(root, text="Ações")
    button_frame.pack(fill="x", expand="yes", padx=20)

    update_button = Button(button_frame, text="Atualizar", command=lambda:atualizar_dados("fornecedores"))
    update_button.grid(row=0 , column=0 , padx=10, pady=10)

    add_button = Button(button_frame, text="Adicionar", command=lambda:adicionar_ao_banco("fornecedores"))
    add_button.grid(row=0 , column=1 , padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("fornecedores","cnpj", cnpj_fornecedor_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

    clear_box_button = Button(button_frame, text="Limpar")
    clear_box_button.grid(row=0 , column=7 , padx=10, pady=10)

    #bind th treeview
    my_tree.bind("<ButtonRelease-1>", selecionar_dados_arvore)

#-----------------------------------------------------------------------------------------

#criando a janela para tabela transação
def janela_transacao():
    for widgets in root.winfo_children():
        widgets.destroy()
    cria_menu()
    def selecionar_dados_arvore(e):
        id_transacao_entry.delete(0, END)
        f_id_transacao_entry.delete(0, END)
        e_id_transacao_entry.delete(0, END)
        data_transacao_entry.delete(0, END)
        quantidade_transacao_entry.delete(0, END)
        valor_unitario_transacao_entry.delete(0, END)

        selecionado = my_tree.focus()

        valor = my_tree.item(selecionado, 'values')

        id_transacao_entry.insert(0, valor[0])
        f_id_transacao_entry.insert(0, valor[1])
        e_id_transacao_entry.insert(0, valor[2])
        data_transacao_entry.insert(0, valor[3])
        quantidade_transacao_entry.insert(0, valor[4])
        valor_unitario_transacao_entry.insert(0, valor[5])
        
    root.geometry("1030x500")
    
    #adicionando estilo
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map('Treeview', background=[('selected', "#347083")])

    global my_tree

    #criando frame da treeview
    frame_transacao = Frame(root)
    frame_transacao.pack(pady=10)

    #criando o scroll da treeview
    tree_scroll = Scrollbar(frame_transacao)
    tree_scroll.pack(side=RIGHT, fill=Y)

    #criando a treeview
    my_tree = ttk.Treeview(frame_transacao, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    #configurando o scroll
    tree_scroll.config(command=my_tree.yview)

    #difinindo as colunas
    my_tree['columns'] = ("ID", "Fornecedor", "Item", "Data", "Quantidade", "Valor Unitário")
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ID", width=140, anchor=W)
    my_tree.column("Fornecedor", width=140, anchor=W)
    my_tree.column("Item", width=140, anchor=CENTER)
    my_tree.column("Data", width=140, anchor=CENTER)
    my_tree.column("Quantidade", width=140, anchor=CENTER)
    my_tree.column("Valor Unitário", width=140, anchor=CENTER)
    
    #criando as headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ID", text="ID", anchor=W)
    my_tree.heading("Fornecedor", text="Fornecedor", anchor=W)
    my_tree.heading("Item", text="Item", anchor=CENTER)
    my_tree.heading("Data", text="Data", anchor=CENTER)
    my_tree.heading("Quantidade", text="Quantidade", anchor=CENTER)
    my_tree.heading("Valor Unitário", text="Valor Unitário", anchor=CENTER)

    #alternando as cores das linhas
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    #adicionando as caixas de entrada
    data_frame = LabelFrame(root, text="Animais")
    data_frame.pack(fill="x", expand="yes", padx=20)
    global id_transacao_entry
    id_transacao_label = Label(data_frame, text="ID")
    id_transacao_label.grid(row=0, column=0, padx=10, pady=10)
    id_transacao_entry = Entry(data_frame)
    id_transacao_entry.grid(row=0, column=1, padx=10, pady=10)
    global f_id_transacao_entry
    f_id_transacao_label = Label(data_frame, text="Fornecedor")
    f_id_transacao_label.grid(row=0, column=2, padx=10, pady=10)
    f_id_transacao_entry = Entry(data_frame)
    f_id_transacao_entry.grid(row=0, column=3, padx=10, pady=10)
    global e_id_transacao_entry
    e_id_transacao_label = Label(data_frame, text="Item")
    e_id_transacao_label.grid(row=0, column=4, padx=10, pady=10)
    e_id_transacao_entry = Entry(data_frame)
    e_id_transacao_entry.grid(row=0, column=5, padx=10, pady=10)
    global data_transacao_entry
    data_transacao_label = Label(data_frame, text="Data")
    data_transacao_label.grid(row=1, column=0, padx=10, pady=10)
    data_transacao_entry = Entry(data_frame)
    data_transacao_entry.grid(row=1, column=1, padx=10, pady=10)
    global quantidade_transacao_entry
    quantidade_transacao_label = Label(data_frame, text="Quantidade")
    quantidade_transacao_label.grid(row=1, column=2, padx=10, pady=10)
    quantidade_transacao_entry = Entry(data_frame)
    quantidade_transacao_entry.grid(row=1, column=3, padx=10, pady=10)
    global valor_unitario_transacao_entry
    valor_unitario_transacao_label = Label(data_frame, text="Valor Unitário")
    valor_unitario_transacao_label.grid(row=1, column=4, padx=10, pady=10)
    valor_unitario_transacao_entry = Entry(data_frame)
    valor_unitario_transacao_entry.grid(row=1, column=5, padx=10, pady=10)
    
    query_database("transacao")

    #adicionando botões
    button_frame = LabelFrame(root, text="Ações")
    button_frame.pack(fill="x", expand="yes", padx=20)

    update_button = Button(button_frame, text="Atualizar", command=lambda:atualizar_dados("transacao"))
    update_button.grid(row=0 , column=0 , padx=10, pady=10)

    add_button = Button(button_frame, text="Adicionar", command=lambda:adicionar_ao_banco("transacao"))
    add_button.grid(row=0 , column=1 , padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("transacao","id", id_transacao_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

    clear_box_button = Button(button_frame, text="Limpar")
    clear_box_button.grid(row=0 , column=7 , padx=10, pady=10)

    #bind th treeview
    my_tree.bind("<ButtonRelease-1>", selecionar_dados_arvore)


#-----------------------------------------------------------------------------------------

#criando a janela para a view vacinados
def janela_vacinados():
    for widgets in root.winfo_children():
        widgets.destroy()
    cria_menu()
    
    vacinados_frame = Frame(root)
    vacinados_frame.pack(padx=10, pady=10)

    root.geometry("1030x500")
    
    #adicionando estilo
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map('Treeview', background=[('selected', "#347083")])

    global my_tree

    #criando frame da treeview
    vacinados_frame = Frame(root)
    vacinados_frame.pack(pady=10)

    #criando o scroll da treeview
    tree_scroll = Scrollbar(vacinados_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    #criando a treeview
    my_tree = ttk.Treeview(vacinados_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    #configurando o scroll
    tree_scroll.config(command=my_tree.yview)

    #difinindo as colunas
    my_tree['columns'] = ("Animal", "Vacina", "Data")
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Animal", width=140, anchor=CENTER)
    my_tree.column("Vacina", width=140, anchor=CENTER)
    my_tree.column("Data", width=140, anchor=CENTER)
    
    
    #criando as headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Animal", text="Animal", anchor=CENTER)
    my_tree.heading("Vacina", text="Vacina", anchor=CENTER)
    my_tree.heading("Data", text="Data", anchor=CENTER)
    

    #alternando as cores das linhas
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    query_database("vacinados")

    #adicionando botões
    selecinonar_frame = LabelFrame(root, text="Escolher")
    selecinonar_frame.pack(fill="x", expand="yes", padx=20)
    my_label = Label(selecinonar_frame, text="Escolher Animal")
    my_label.grid(row=0, column=0, pady=10)
    global vacinados_tag_entry
    vacinados_tag_entry = Entry(selecinonar_frame)
    vacinados_tag_entry.grid(row=0, column=1, pady=10)

    #adicionando botões
    button_frame = LabelFrame(root, text="Ações")
    button_frame.pack(fill="x", expand="yes", padx=20)

    update_button = Button(button_frame, text="Selecionar", command=lambda:query_database("animal_vacinado"))
    update_button.grid(row=0 , column=0 , padx=10, pady=10)

    limpar_button = Button(button_frame, text="Restaurar Tabela", command=lambda:query_database("vacinados"))
    limpar_button.grid(row=0 , column=1 , padx=10, pady=10)
    

#-----------------------------------------------------------------------------------------

#criar janela para vizualizar os filhos de um animal
def janela_filhos():
    for widgets in root.winfo_children():
        widgets.destroy()
    cria_menu()
    root.geometry("600x500")
    def escolher_animal_mae(tipo, escolhido):
        for widgets in frame2_parentes.winfo_children():
            widgets.destroy()
        conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "aneis1961",
            database = "casima"
        )
        #criando o cursor
        cursor = conexao.cursor()
        
        if tipo == "filhos":
            sql = "SELECT * FROM animais WHERE pai_tag = %s OR mae_tag = %s"
            animal = (str(escolhido), str(escolhido))
            aux = 0
            try:
                cursor.execute(sql, animal)
            except Error as e:
                print(e)
            resultado = cursor.fetchall()
            for item in resultado:
                resultado_filhos_label = Label(frame2_parentes, text=str(item[0]))
                resultado_filhos_label.grid(row=aux, column=0, columnspan=20, pady=10)
                aux += 1
        
        elif tipo  == "tag":
            sql = "SELECT mae_tag, pai_tag FROM animais WHERE tag = %s"
            animal = (str(escolhido), )
            aux = 0
            try:
                cursor.execute(sql, animal)
            except Error as e:
                print(e)
            resultado = cursor.fetchall()
            for item in resultado:
                resultado_filhos_label = Label(frame2_parentes, text="Mãe = " + str(item[0]) + "\nPai =  " + str(item[1]) )
                resultado_filhos_label.grid(row=aux, column=0, columnspan=20, pady=10)
                aux += 1
        
        elif tipo == "materno":
            condicao = (str(escolhido))
            aux = 0
            while condicao != 0:
                sql = "SELECT mae_tag FROM animais WHERE tag = %s"
                animal = (condicao, )
                try:
                    cursor.execute(sql, animal)
                except Error as e:
                    print(e)
                resultado = cursor.fetchall()
                condicao = resultado[0][0]
                resultado_filhos_label = Label(frame2_parentes, text=str(condicao))
                resultado_filhos_label.grid(row=aux, column=1, columnspan=20, pady=10)
                aux += 1

        else:
            condicao = (str(escolhido))
            aux = 0
            while condicao != 0:
                sql = "SELECT pai_tag FROM animais WHERE tag = %s"
                animal = (condicao, )
                try:
                    cursor.execute(sql, animal)
                except Error as e:
                    print(e)
                resultado = cursor.fetchall()
                condicao = resultado[0][0]
                resultado_filhos_label = Label(frame2_parentes, text=str(condicao))
                resultado_filhos_label.grid(row=aux, column=1, columnspan=20, pady=10)
                aux += 1
        
        
        conexao.commit()
        conexao.close()
    
    frame_parentes = LabelFrame(root, text="O que você quer saber?")
    frame_parentes.pack(pady=10, padx=10, fill="x", expand="yes", side="top")
    
    animal_parente_label = Label(frame_parentes, text="Número do brinco: ")
    animal_parente_label.grid(row=0, column=1)

    animal_parente_entry = Entry(frame_parentes)
    animal_parente_entry.grid(row=1, column=1)
    
    escolha_radio = StringVar()
    escolha_radio.set("mae_tag")

    Radiobutton(frame_parentes, text="Filhos", variable=escolha_radio, value="filhos").grid(row=0,column=0, sticky=W, padx=10)
    
    Radiobutton(frame_parentes, text="Parentes", variable=escolha_radio, value="tag").grid(row=1,column=0, sticky=W, padx=10)
    
    Radiobutton(frame_parentes, text="Parentesco Materno", variable=escolha_radio, value="materno").grid(row=2,column=0, sticky=W, padx=10)

    Radiobutton(frame_parentes, text="Parentesco Paterno", variable=escolha_radio, value="paterno").grid(row=3,column=0, sticky=W, padx=10)

    botao_escolher = Button(frame_parentes, text="Pesquisar", command=lambda:escolher_animal_mae(escolha_radio.get(), animal_parente_entry.get()), padx=10)
    botao_escolher.grid(row=2, column=1)
    
    frame2_parentes = LabelFrame(root, text="Resultado")
    frame2_parentes.pack(pady=10, padx=10, fill="x", expand="yes")

#-----------------------------------------------------------------------------------------

cria_menu()
frame_incial = LabelFrame(root, text="")
frame_incial.pack(fill="x", expand="yes", padx=20)
titulo = Label(frame_incial, text="Casima Agrícola", font=("Helvetica", 40)).pack(padx=30, pady=30)

root.mainloop()