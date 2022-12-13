from tkinter import*
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from scipy.optimize import linprog
import csv
import os
import datetime

root = Tk()
root.title('Casima Agrícola')
root.iconbitmap('./python.ico')
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
except Error as e:
    aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel se conectar ao banco de dados \nErro: " + str(e))

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
    menu_racao.add_separator()
    menu_racao.add_command(label="Ingredientes", command=janela_ingredientes)

    menu_backup = Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(label="Backup", menu=menu_backup)
    sub_menu = Menu(menu_backup, tearoff=0)
    menu_backup.add_cascade(label="Fazer Backup", menu=sub_menu)
    sub_menu.add_command(label="Tudo", command=fazer_backup)

    menu_backup.add_command(label="Restaurar Backup", command=restaurar_backup)
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
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][7], dados[num][2], dados[num][3], dados[num][4], dados[num][5], dados[num][6]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][7], dados[num][2], dados[num][3], dados[num][4], dados[num][5], dados[num][6]), tags=('oddrow', ))
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

    elif tabela == "rebanho":   
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
        dados = cursor.fetchall()

        num = 0
        for itens in dados:
            if num % 2 == 0:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][2], dados[num][3]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][2], dados[num][3]), tags=('oddrow', ))
            num += 1

    elif tabela == "vacina_vacinado":
        vacina = str(vacinados_tag_entry.get())
        
        try:
            cursor.execute("SELECT * FROM vacinados WHERE nome = %s ", (vacina, ))
        except Error as e:
            aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel se conectar ao banco de dados \nErro: " + str(e))
        dados = cursor.fetchall()

        num = 0
        for itens in dados:
            if num % 2 == 0:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][2], dados[num][3]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][2], dados[num][3]), tags=('oddrow', ))
            num += 1

    elif tabela == "ingredientes":   
        cursor.execute("SELECT * FROM ingredientes")
        dados = cursor.fetchall()
        #print(dados)
        num = 0
        for itens in dados:
            if num % 2 == 0:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2], dados[num][3], dados[num][4], dados[num][5], dados[num][6], dados[num][7], dados[num][8], dados[num][9], dados[num][10], dados[num][11], dados[num][12], dados[num][13], dados[num][14], dados[num][15], dados[num][16], dados[num][17], dados[num][18]), tags=('evenrow', ))
            else:
                my_tree.insert(parent='', index='end', iid=num, text='', values=(dados[num][0], dados[num][1], dados[num][2], dados[num][3], dados[num][4], dados[num][5], dados[num][6], dados[num][7], dados[num][8], dados[num][9], dados[num][10], dados[num][11], dados[num][12], dados[num][13], dados[num][14], dados[num][15], dados[num][16], dados[num][17], dados[num][18]), tags=('oddrow', ))
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
            sql = "UPDATE animais SET tag = %s, tipo = %s, data_nascimento = %s, peso = %s, sexo = %s, mae_tag = %s, pai_tag = %s, raca = %s WHERE tag = %s "

            tag = str(tag_entry.get())
            tipo = str(tipo_entry.get())
            data_nascimento = str(data_nascimento_entry.get())
            peso = str(peso_entry.get())
            sexo = str(sexo_entry.get())
            mae_tag = str(mae_tag_entry.get())
            pai_tag = str(pai_tag_entry.get())
            raca = str(raca_entry.get())

            dados = (tag, tipo, data_nascimento, peso, sexo, mae_tag, pai_tag, raca, tag)
            try:
                cursor.execute(sql, dados)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível salvar as alterações \nErro: " + str(e))
        
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

        elif tabela == "ingredientes":
            sql = "UPDATE ingredientes SET ingrediente = %s, magnesio = %s, potassio = %s, sodio = %s, enxofre = %s, cobalto = %s, cobre = %s, iodo = %s, ferro = %s, manganes = %s, selenio = %s, zinco = %s, vitamina_a = %s, vitamina_d = %s, calcio = %s, fosforo = %s, proteina = %s, energia = %s WHERE id =  = %s"
            valores = (str(ingrediente_entry.get()), str(magnesio_entry.get()), str(potassio_entry.get()), str(sodio_entry.get()), str(enxofre_entry.get()), str(cobalto_entry.get()), str(cobre_entry.get()), str(iodo_entry.get()), str(ferro_entry.get()), str(manganes_entry.get()), str(selenio_entry.get()), str(zinco_entry.get()), str(vitamina_a_entry.get()), str(vitamina_d_entry.get()), str(calcio_entry.get()), str(fosforo_entry.get()), str(proteina_entry.get()), str(energia_entry.get()), str(id_ingredientes_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível salvar as alterações \nErro: " + str(e))
        
        #dando commit
        conexao.commit()
        #fechando a conexao
        conexao.close()
        my_tree.delete(*my_tree.get_children())
        query_database(tabela)
           
    else:
        aviso = messagebox.showinfo(title="Update", message="Nada foi alterado")
    

#-----------------------------------------------------------------------------------------

#deletando item do banco
def remover(tabela, pk_entry):
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
        dados = (str(pk_entry), )
        
        if tabela == "funcionarios":
            sql = "DELETE FROM funcionarios WHERE cpf = %s"
            try:
                cursor.execute(sql, dados)
            except Error as a:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel remover o item \nErro: " + str(a))
        
        elif tabela == "animais":
            sql = "DELETE FROM animais WHERE tag = %s"
            try:
                cursor.execute(sql, dados)
            except Error as a:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel remover o item \nErro: " + str(a))

        elif tabela == "vacinas":
            sql = "DELETE FROM vacinas WHERE id = %s"
            try:
                cursor.execute(sql, dados)
            except Error as a:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel remover o item \nErro: " + str(a))

        elif tabela == "vacinacao":
            sql = "DELETE FROM vacinacao WHERE id = %s"
            try:
                cursor.execute(sql, dados)
            except Error as a:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel remover o item \nErro: " + str(a))

        elif tabela == "estoque":
            sql = "DELETE FROM estoque WHERE id = %s"
            try:
                cursor.execute(sql, dados)
            except Error as a:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel remover o item \nErro: " + str(a))

        elif tabela == "problemas_gestacao":
            sql = "DELETE FROM problemas_gestacao WHERE id = %s"
            try:
                cursor.execute(sql, dados)
            except Error as a:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel remover o item \nErro: " + str(a))

        elif tabela == "gestacao":
            sql = "DELETE FROM gestacao WHERE id = %s"
            try:
                cursor.execute(sql, dados)
            except Error as a:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel remover o item \nErro: " + str(a))

        elif tabela == "fornecedores":
            sql = "DELETE FROM fornecedores WHERE cnpj = %s"
            try:
                cursor.execute(sql, dados)
            except Error as a:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel remover o item \nErro: " + str(a))

        elif tabela == "transacao":
            sql = "DELETE FROM transacao WHERE id = %s"
            try:
                cursor.execute(sql, dados)
            except Error as a:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel remover o item \nErro: " + str(a))

        elif tabela == "ingredientes":
            sql = "DELETE FROM ingredientes WHERE id = %s"
            try:
                cursor.execute(sql, dados)
            except Error as a:
                aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel remover o item \nErro: " + str(a))


        #dando commit
        conexao.commit()
        #fechando a conexao
        conexao.close()
        #atualizando arvore
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

        elif tabela == "animais":
            sql = "INSERT INTO animais (tag, tipo, data_nascimento, peso, sexo, mae_tag, pai_tag, raca) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            valores = (str(tag_entry.get()), str(tipo_entry.get()), str(data_nascimento_entry.get()), str(peso_entry.get()), str(sexo_entry.get()), str(mae_tag_entry.get()), str(pai_tag_entry.get()), str(raca_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

        elif tabela == "vacinas":
            sql = "INSERT INTO vacinas (id, nome, reforco) VALUES (%s, %s, %s)"
            valores = (str(id_vacina_entry.get()), str(nome_vacina_entry.get()), str(reforco_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))
            
        elif tabela == "vacinacao":
            sql = "INSERT INTO vacinacao (id, vacina_id, animais_tag, data) VALUES (%s, %s, %s, %s)"
            valores = (str(id_vacinacao_entry.get()), str(vacinafk_id_entry.get()), str(animaisfk_tag_entry.get()), str(data_vacinacao_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

        elif tabela == "estoque":
            sql = "INSERT INTO estoque (item, quantidade) VALUES (%s, %s)"
            valores = (str(item_entry.get()), str(quantidade_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

        elif tabela == "problemas_gestacao":
            sql = "INSERT INTO problemas_gestacao (id, nome, descricao) VALUES (%s, %s, %s)"
            valores = (str(id_prob_gest_entry.get()), str(nome_prob_gest_entry.get()), str(descricao_prob_gest_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

        elif tabela == "gestacao":
            sql = "INSERT INTO gestacao (id, a_tag, pg_id, descricao, data) VALUES (%s, %s, %s, %s, %s)"
            valores = (str(id_gestacao_entry.get()), str(gestacao_tag_entry.get()), str(pgid_gestacao_entry.get()), str(descricao_gestacao_entry.get()), str(data_gestacao_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

        elif tabela == "fornecedores":
            sql = "INSERT INTO fornecedores (cnpj, nome, cidade, endereco, telefone) VALUES (%s, %s, %s, %s, %s)"
            valores = (str(cnpj_fornecedor_entry.get()), str(nome_fornecedor_entry.get()), str(cidade_fornecedor_entry.get()), str(endereco_fornecedor_entry.get()), str(telefone_fornecedor_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))        

        elif tabela == "transacao":
            sql = "INSERT INTO transacao (id, f_id, e_id, data, quantidade, valor_unitario) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (str(id_transacao_entry.get()), str(f_id_transacao_entry.get()), str(e_id_transacao_entry.get()), str(data_transacao_entry.get()), str(quantidade_transacao_entry.get()), str(valor_unitario_transacao_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))

        elif tabela == "ingredientes":
            sql = "INSERT INTO ingredientes (id, ingrediente, magnesio, potassio, sodio, enxofre, cobalto, cobre, iodo, ferro, manganes, selenio, zinco, vitamina_a, vitamina_d, calcio, fosforo, proteina, energia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            valores = (str(id_ingredientes_entry.get()), str(ingrediente_entry.get()), str(magnesio_entry.get()), str(potassio_entry.get()), str(sodio_entry.get()), str(enxofre_entry.get()), str(cobalto_entry.get()), str(cobre_entry.get()), str(iodo_entry.get()), str(ferro_entry.get()), str(manganes_entry.get()), str(selenio_entry.get()), str(zinco_entry.get()), str(vitamina_a_entry.get()), str(vitamina_d_entry.get()), str(calcio_entry.get()), str(fosforo_entry.get()), str(proteina_entry.get()), str(energia_entry.get()))

            try:
                cursor.execute(sql, valores)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))
        
        elif tabela == "rebanho":
            sql = "SELECT * FROM vacinas WHERE nome = %s"
            vacina = (str(vacina_selecionada.get()), )
            try:
                cursor.execute(sql, vacina)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Erro no banco de dados! \nErro: " + str(e))
            vacina_id = cursor.fetchall()
            
            sql = "SELECT tag FROM animais WHERE tipo = %s"
            rebanho = (str(rebanho_selecionado.get()), )
            try:
                cursor.execute(sql, rebanho)
            except Error as e:
                aviso = messagebox.showerror(title="ERRO", message="Erro no banco de dados! \nErro: " + str(e))
            animais = cursor.fetchall()
            
            for animal_tag in animais:
                sql = "INSERT INTO vacinacao (vacina_id, animais_tag, data) VALUES (%s, %s, %s)"
                valores = (str(vacina_id[0][0]), str(animal_tag[0]), str(datetime.date.today()))
                try:
                    cursor.execute(sql, valores)
                except Error as e:
                    aviso = messagebox.showerror(title="ERRO", message="Não foi possível adicionar ao banco! \nErro: " + str(e))
                    return

        conexao.commit()
        conexao.close()
        
        my_tree.delete(*my_tree.get_children())
        query_database(tabela)

#-----------------------------------------------------------------------------------------

#funcao para fazer um backup do banco em varios arquivos csv
def fazer_backup():
    response = messagebox.askyesno(title="Backup",  message="Fazer Backup? Isso apagará o backup antigo")
    if response == 1:
        try:
            os.remove("backup_animais.csv")
            os.remove("backup_estoque.csv")
            os.remove("backup_fornecedores.csv")
            os.remove("backup_funcionarios.csv")
            os.remove("backup_gestacao.csv")
            os.remove("backup_problemasgest.csv")
            os.remove("backup_transacao.csv")
            os.remove("backup_vacinacao.csv")
            os.remove("backup_vacinas.csv")
        
        finally:
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
                    with open('backup_animais.csv', 'a', newline='') as arquivo_backup:
                        arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                        for item in resultado:
                            arquivo_backup.writerow(item)

                elif nome == "funcionarios":
                    try:
                        cursor.execute("SELECT * FROM funcionarios")
                    except Error as e:
                        aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
                    resultado = cursor.fetchall()
                    with open('backup_funcionarios.csv', 'a', newline='') as arquivo_backup:
                        arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                        for item in resultado:
                            arquivo_backup.writerow(item)

                elif nome == "vacinas":
                    try:
                        cursor.execute("SELECT * FROM vacinas")
                    except Error as e:
                        aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
                    resultado = cursor.fetchall()
                    with open('backup_vacinas.csv', 'a', newline='') as arquivo_backup:
                        arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                        for item in resultado:
                            arquivo_backup.writerow(item)

                elif nome == "vacinacao":
                    try:
                        cursor.execute("SELECT * FROM vacinacao")
                    except Error as e:
                        aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
                    resultado = cursor.fetchall()
                    with open('backup_vacinacao.csv', 'a', newline='') as arquivo_backup:
                        arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                        for item in resultado:
                            arquivo_backup.writerow(item)

                elif nome == "estoque":
                    try:
                        cursor.execute("SELECT * FROM estoque")
                    except Error as e:
                        aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
                    resultado = cursor.fetchall()
                    with open('backup_estoque.csv', 'a', newline='') as arquivo_backup:
                        arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                        for item in resultado:
                            arquivo_backup.writerow(item)

                elif nome == "problemas_gestacao":
                    try:
                        cursor.execute("SELECT * FROM problemas_gestacao")
                    except Error as e:
                        aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
                    resultado = cursor.fetchall()
                    with open('backup_problemasgest.csv', 'a', newline='') as arquivo_backup:
                        arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                        for item in resultado:
                            arquivo_backup.writerow(item)

                elif nome == "gestacao":
                    try:
                        cursor.execute("SELECT * FROM gestacao")
                    except Error as e:
                        aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
                    resultado = cursor.fetchall()
                    with open('backup_gestacao.csv', 'a', newline='') as arquivo_backup:
                        arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                        for item in resultado:
                            arquivo_backup.writerow(item)

                elif nome == "fornecedores":
                    try:
                        cursor.execute("SELECT * FROM fornecedores")
                    except Error as e:
                        aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
                    resultado = cursor.fetchall()
                    with open('backup_fornecedores.csv', 'a', newline='') as arquivo_backup:
                        arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                        for item in resultado:
                            arquivo_backup.writerow(item)

                elif nome == "transacao":
                    try:
                        cursor.execute("SELECT * FROM transacao")
                    except Error as e:
                        aviso = messagebox.showerror(title="Falha na Conexão", message="Não foi possivel fazer o backup \nErro: " + str(e))
                    resultado = cursor.fetchall()
                    with open('backup_transacao.csv', 'a', newline='') as arquivo_backup:
                        arquivo_backup = csv.writer(arquivo_backup, dialect='excel')
                        for item in resultado:
                            arquivo_backup.writerow(item)

            conexao.commit()
            conexao.close()
            aviso = messagebox.showinfo(title="Backup", message="Backup feito com sucesso!")
    else:
        aviso = messagebox.showinfo(title="Backup", message="Backup não realizado!")


#-----------------------------------------------------------------------------------------

#funcao para restaurar o backup
def restaurar_backup():
    response = messagebox.askyesno(title="Backup",  message="Confirmar Restauração do Backup?")
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

        sql = "INSERT INTO funcionarios (cpf, nome, telefone, endereco, salario, carteira_trabalho, cargo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        with open('backup_funcionarios.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                info = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                try:
                    cursor.execute(sql, info)
                except:
                    sql = "UPDATE funcionarios SET nome = %s, telefone = %s, endereco = %s, salario = %s, carteira_trabalho = %s, cargo = %s WHERE cpf = %s "
                    info2 = (str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[0]))
                    cursor.execute(sql, info2)
        csvfile.close()

        sql = "INSERT INTO animais (tag, tipo, data_nascimento, peso, sexo, mae_tag, pai_tag, raca) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"       
        with open('backup_animais.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                info = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                try:
                    cursor.execute(sql, info)
                except:
                    sql = "UPDATE animais SET tipo = %s, data_nascimento = %s, peso = %s, sexo = %s, mae_tag = %s, pai_tag = %s, raca = %s WHERE tag = %s "
                    info2 = (str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[0]))
                    cursor.execute(sql, info2)
        csvfile.close()

        sql = "INSERT INTO vacinas (id, nome, reforco) VALUES (%s, %s, %s)"       
        with open('backup_vacinas.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                info = (row[0], row[1], row[2])
                try:
                    cursor.execute(sql, info)
                except:
                    sql = "UPDATE vacinas SET nome = %s, reforco = %s WHERE id = %s "
                    info2 = (str(row[1]), str(row[2]), str(row[0]))
                    cursor.execute(sql, info2)
        csvfile.close()

        sql = "INSERT INTO vacinacao (id, vacina_id, animais_tag, data) VALUES (%s, %s, %s, %s)"       
        with open('backup_vacinacao.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                info = (row[0], row[1], row[2], row[3])
                try:
                    cursor.execute(sql, info)
                except:
                    sql = "UPDATE vacinacao SET vacina_id = %s, animais_tag = %s, data = %s WHERE id = %s "
                    info2 = (str(row[1]), str(row[2]), str(row[3]), str(row[0]))
                    cursor.execute(sql, info2)
        csvfile.close()

        sql = "INSERT INTO estoque (id, item, quantidade) VALUES (%s, %s, %s)"       
        with open('backup_estoque.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                info = (row[0], row[1], row[2])
                try:
                    cursor.execute(sql, info)
                except:
                    sql = "UPDATE estoque SET item = %s, quantidade = %s WHERE id = %s "
                    info2 = (str(row[1]), str(row[2]), str(row[0]))
                    cursor.execute(sql, info2)
        csvfile.close()

        sql = "INSERT INTO problemas_gestacao (id, nome, descricao) VALUES (%s, %s, %s)"       
        with open('backup_problemasgest.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                info = (row[0], row[1], row[2])
                try:
                    cursor.execute(sql, info)
                except:
                    sql = "UPDATE problemas_gestacao SET nome = %s, descricao = %s WHERE id = %s "
                    info2 = (str(row[1]), str(row[2]), str(row[0]))
                    cursor.execute(sql, info2)
        csvfile.close()

        sql = "INSERT INTO gestacao (id, a_tag, pg_id, descricao, data) VALUES (%s, %s, %s, %s, %s)"
        with open('backup_gestacao.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                info = (row[0], row[1], row[2], row[3], row[4])
                try:
                    cursor.execute(sql, info)
                except:
                    sql = "UPDATE gestacao SET a_tag = %s, pg_id = %s, descricao = %s, data = %s WHERE id = %s "
                    info2 = (str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[0]))
                    cursor.execute(sql, info2)
        csvfile.close()

        sql = "INSERT INTO fornecedores (cnpj, nome, cidade, endereco, telefone) VALUES (%s, %s, %s, %s, %s)"
        with open('backup_fornecedores.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                info = (row[0], row[1], row[2], row[3], row[4])
                try:
                    cursor.execute(sql, info)
                except:
                    sql = "UPDATE fornecedores SET nome = %s, cidade = %s, endereco = %s, telefone = %s WHERE cnpj = %s "
                    info2 = (str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[0]))
                    cursor.execute(sql, info2)
        csvfile.close()

        sql = "INSERT INTO transacao (id, f_id, e_id, data, quantidade, valor_unitario,) VALUES (%s, %s, %s, %s, %s, %s)"
        with open('backup_transacao.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                info = (row[0], row[1], row[2], row[3], row[4], row[5])
                try:
                    cursor.execute(sql, info)
                except:
                    sql = "UPDATE transacao SET f_id = %s, e_id = %s, data = %s, quantidade = %s, valor_unitario = %s WHERE id = %s "
                    info2 = (str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[0]))
                    cursor.execute(sql, info2)
        csvfile.close()

        conexao.commit()
        conexao.close()
        aviso = messagebox.showinfo(title="Backup", message="Restauração feita com sucesso!")

#-----------------------------------------------------------------------------------------

#criando janela do simplex
def janela_simplex():
    for widgets in root.winfo_children():
        widgets.destroy()
    cria_menu()
    root.geometry("800x600")

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

        resposta_label = Label(frame_final, text="Quantidade de ingrediente 1 = " + str(resultado['x'][0]) + " Kg\nQuantidade de ingrediente 2 = " + str(resultado['x'][1]) + " Kg\nQuantidade de ingrediente 3 = " + str(resultado['x'][2]) + " Kg")
        resposta_label.grid(row=1, column=1, columnspan=4, rowspan=3)



    def desabilitar_botao(ingrediente):
        if ingrediente == "soja" and ing1.get() == 1:
            ingrediente1_entry.config(state=NORMAL)
        elif ingrediente == "soja" and ing1.get() == 0:
            ingrediente1_entry.delete(0, END)
            #ingrediente1_entry.insert(0, "0")
            ingrediente1_entry.config(state=DISABLED)           

        if ingrediente == "milho" and ing2.get() == 1:
            ingrediente2_entry.config(state=NORMAL)
        elif ingrediente == "milho" and ing2.get() == 0:
            ingrediente2_entry.delete(0, END)
            #ingrediente2_entry.insert(0, "0")
            ingrediente2_entry.config(state=DISABLED)
            
        if ingrediente == "cana" and ing3.get() == 1:
            ingrediente3_entry.config(state=NORMAL)
        elif ingrediente == "cana" and ing3.get() == 0:
            ingrediente3_entry.delete(0, END)
            #ingrediente3_entry.insert(0, "0")
            ingrediente3_entry.config(state=DISABLED)
        
        if ingrediente == "algodao" and ing4.get() == 1:
            ingrediente4_entry.config(state=NORMAL)
        elif ingrediente == "algodao" and ing4.get() == 0:
            ingrediente4_entry.delete(0, END)
            #ingrediente4_entry.insert(0, "0")
            ingrediente4_entry.config(state=DISABLED)
            
        if ingrediente == "sal" and ing5.get() == 1:
            ingrediente5_entry.config(state=NORMAL)
        elif ingrediente == "sal" and ing5.get() == 0:
            ingrediente5_entry.delete(0, END)
            #ingrediente5_entry.insert(0, "0")
            ingrediente5_entry.config(state=DISABLED)
            
    #criando frame para selecionar especificaacoes
    frame_selecionar = LabelFrame(root, text="Selecionar ingredientes disponíveis")
    frame_selecionar.pack(fill="x", padx=10, pady=10)

    ing1 = IntVar()
    ing2 = IntVar()
    ing3 = IntVar()
    ing4 = IntVar()
    ing5 = IntVar()
    
    soja = Checkbutton(frame_selecionar, text="Soja", variable=ing1, command=lambda:desabilitar_botao("soja"))
    milho = Checkbutton(frame_selecionar, text="Milho", variable=ing2, command=lambda:desabilitar_botao("milho"))
    cana = Checkbutton(frame_selecionar, text="Cana", variable=ing3, command=lambda:desabilitar_botao("cana"))
    algodao = Checkbutton(frame_selecionar, text="Algodão", variable=ing4, command=lambda:desabilitar_botao("algodao"))
    sal_mineral = Checkbutton(frame_selecionar, text="Sal mineral", variable=ing5, command=lambda:desabilitar_botao("sal"))

    soja.grid(row=0, column=0, padx=4, pady=4)
    milho.grid(row=0, column=1, padx=4, pady=4)
    cana.grid(row=0, column=2, padx=4, pady=4)
    algodao.grid(row=0, column=3, padx=4, pady=4)
    sal_mineral.grid(row=0, column=4, padx=4, pady=4)
    
    #criando frame do simplex
    frame_simplex = LabelFrame(root, text="Quantidade disponível de cada ingrediente em Kg")
    frame_simplex.pack(fill="x", pady=10, padx=10)

    ingrediente1_label = Label(frame_simplex, text="Soja")
    ingrediente1_label.grid(row=0, column=0, pady=10, padx=(10,0))
    ingrediente1_entry = Entry(frame_simplex, state=DISABLED)
    ingrediente1_entry.grid(row=0, column=1, pady=10)

    ingrediente2_label = Label(frame_simplex, text="Milho")
    ingrediente2_label.grid(row=0, column=2, pady=10, padx=(10,0))
    ingrediente2_entry = Entry(frame_simplex, state=DISABLED)
    ingrediente2_entry.grid(row=0, column=3, pady=10)

    ingrediente3_label = Label(frame_simplex, text="Cana")
    ingrediente3_label.grid(row=0, column=4, pady=10, padx=(10,0))
    ingrediente3_entry = Entry(frame_simplex, state=DISABLED)
    ingrediente3_entry.grid(row=0, column=5, pady=10)

    ingrediente4_label = Label(frame_simplex, text="Algodão")
    ingrediente4_label.grid(row=1, column=0, pady=10, padx=(10,0))
    ingrediente4_entry = Entry(frame_simplex, state=DISABLED)
    ingrediente4_entry.grid(row=1, column=1, pady=10)

    ingrediente5_label = Label(frame_simplex, text="Sal Mineral")
    ingrediente5_label.grid(row=1, column=2, pady=10, padx=(10,0))
    ingrediente5_entry = Entry(frame_simplex, state=DISABLED)
    ingrediente5_entry.grid(row=1, column=3, pady=10)


    frame_final = Frame(root)
    frame_final.pack(fill="x", pady=10, padx=10)


    botao_calcular = Button(frame_final, text="Calcular", command=simplex)
    botao_calcular.grid(row=0, column=0, pady=10, padx=10)
    
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

    update_button = Button(button_frame, text="Atualizar", command=lambda:atualizar_dados("funcionarios"))
    update_button.grid(row=0 , column=0 , padx=10, pady=10)

    add_button = Button(button_frame, text="Adicionar", command=lambda:adicionar_ao_banco("funcionarios"))
    add_button.grid(row=0 , column=1 , padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("funcionarios", cpf_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

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
        raca_entry.delete(0, END)
        data_nascimento_entry.delete(0, END)
        peso_entry.delete(0, END)
        sexo_entry.delete(0, END)
        mae_tag_entry.delete(0, END)
        pai_tag_entry.delete(0, END)
       

        selecionado = my_tree.focus()

        valor = my_tree.item(selecionado, 'values')

        tag_entry.insert(0, valor[0])
        tipo_entry.insert(0, valor[1])
        raca_entry.insert(0, valor[2])
        data_nascimento_entry.insert(0, valor[3])
        peso_entry.insert(0, valor[4])
        sexo_entry.insert(0, valor[5])
        mae_tag_entry.insert(0, valor[6])
        pai_tag_entry.insert(0, valor[7])
        

    root.geometry("1200x600")
    
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
    my_tree['columns'] = ("TAG", "Tipo", "Raça", "Nascimento", "Peso", "Sexo", "Mãe", "Pai")
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("TAG", width=140, anchor=W)
    my_tree.column("Tipo", width=140, anchor=W)
    my_tree.column("Raça", width=140, anchor=CENTER)
    my_tree.column("Nascimento", width=140, anchor=CENTER)
    my_tree.column("Peso", width=140, anchor=CENTER)
    my_tree.column("Sexo", width=140, anchor=CENTER)
    my_tree.column("Mãe", width=140, anchor=CENTER)
    my_tree.column("Pai", width=140, anchor=CENTER)

    #criando as headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("TAG", text="TAG", anchor=W)
    my_tree.heading("Tipo", text="Tipo", anchor=W)
    my_tree.heading("Raça", text="Raça", anchor=CENTER)
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
    peso_label.grid(row=0, column=6, padx=10, pady=10)
    peso_entry = Entry(data_frame)
    peso_entry.grid(row=0, column=7, padx=10, pady=10)
    global sexo_entry
    sexo_label = Label(data_frame, text="Sexo")
    sexo_label.grid(row=1, column=0, padx=10, pady=10)
    sexo_entry = Entry(data_frame)
    sexo_entry.grid(row=1, column=1, padx=10, pady=10)
    global mae_tag_entry
    mae_tag_label = Label(data_frame, text="Mãe")
    mae_tag_label.grid(row=1, column=2, padx=10, pady=10)
    mae_tag_entry = Entry(data_frame)
    mae_tag_entry.grid(row=1, column=3, padx=10, pady=10)
    global pai_tag_entry
    pai_tag_label = Label(data_frame, text="Pai")
    pai_tag_label.grid(row=1, column=4, padx=10, pady=10)
    pai_tag_entry = Entry(data_frame)
    pai_tag_entry.grid(row=1, column=5, padx=10, pady=10)
    global raca_entry
    raca_label = Label(data_frame, text="Raça")
    raca_label.grid(row=1, column=6, padx=10, pady=10)
    raca_entry = Entry(data_frame)
    raca_entry.grid(row=1, column=7, padx=10, pady=10)
    
    query_database("animais")

    #adicionando botões
    button_frame = LabelFrame(root, text="Ações")
    button_frame.pack(fill="x", expand="yes", padx=20)

    update_button = Button(button_frame, text="Atualizar", command=lambda:atualizar_dados("animais"))
    update_button.grid(row=0 , column=0 , padx=10, pady=10)

    add_button = Button(button_frame, text="Adicionar", command=lambda:adicionar_ao_banco("animais"))
    add_button.grid(row=0 , column=1 , padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("animais", tag_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

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

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("vacinas", id_vacina_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

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

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("vacinacao", id_vacinacao_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

    """
    #interface para vacinar varios animais
    btn_frame = LabelFrame(root, text="Vacinar")
    btn_frame.pack(fill="x", expand="yes", padx=20)

    label1 = Label(btn_frame, text="Quais animais você quer vacinar?")
    label1.grid(row=0, column=0, padx=10)


    variable = StringVar()
    variable.set("Escolher Rebanho")
    escolher_rebanho = OptionMenu(btn_frame, variable=variable, "bovino")
    escolher_rebanho.current(0)
    escolher_rebanho.grid(row=0, column=2)

    """

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

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("estoque", id_estoque_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

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

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("problemas_gestacao", id_prob_gest_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

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

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("gestacao", id_gestacao_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

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

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("fornecedores", cnpj_fornecedor_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

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

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("transacao", id_transacao_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

    #bind th treeview
    my_tree.bind("<ButtonRelease-1>", selecionar_dados_arvore)


#-----------------------------------------------------------------------------------------

#criando a janela para a view vacinados
def janela_vacinados():
    #funcao para pegar todas vacinas adiciondas no banco
    def receber_vacinas():
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
            aviso = messagebox.showerror(title="ERRO", message="Erro na conexão com o banco! \nErro: " + str(e))
    
        cursor.execute("SELECT nome FROM vacinas")
        resultado = cursor.fetchall()
        return resultado

    #funcao para pegar todos tipos de rebanhos
    def receber_rebanho():
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
            aviso = messagebox.showerror(title="ERRO", message="Erro na conexão com o banco! \nErro: " + str(e))
    
        cursor.execute("SELECT tipo FROM animais")
        resultado = cursor.fetchall()
        resultado = list(dict.fromkeys(resultado))
        return resultado
            

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
    selecinonar_frame = LabelFrame(root, text="Vizualizar")
    selecinonar_frame.pack(fill="x", expand="yes", padx=20)
    my_label = Label(selecinonar_frame, text="Escolher Animal ou Vacina")
    my_label.grid(row=0, column=0, pady=10)
    global vacinados_tag_entry
    vacinados_tag_entry = Entry(selecinonar_frame)
    vacinados_tag_entry.grid(row=0, column=1, pady=10)

    #adicionando botões
    update_button = Button(selecinonar_frame, text="Selecionar Animal", command=lambda:query_database("animal_vacinado"))
    update_button.grid(row=1 , column=0 , padx=10, pady=10)

    update2_button = Button(selecinonar_frame, text="Selecionar Vacina", command=lambda:query_database("vacina_vacinado"))
    update2_button.grid(row=1 , column=1 , padx=10, pady=10)

    limpar_button = Button(selecinonar_frame, text="Restaurar Tabela", command=lambda:query_database("vacinados"))
    limpar_button.grid(row=1 , column=2 , padx=10, pady=10)

    frame_vacinar = LabelFrame(root, text="Vacinar Rebanho")
    frame_vacinar.pack(fill="x", expand="yes", padx=20)
    
    selecionar_vacina_label = Label(frame_vacinar, text="Selecione a vacina: ")
    selecionar_vacina_label.grid(row=0, column=0, padx=10, pady=10)
    global vacina_selecionada
    vacina_selecionada = StringVar()
    selecionar_vacina = ttk.Combobox(frame_vacinar, textvariable=vacina_selecionada)
    
    selecionar_vacina['values'] = receber_vacinas()
    selecionar_vacina['state'] = 'readonly'

    selecionar_vacina.grid(row=0, column=1, padx=10, pady=10)

    selecionar_rebanho_label = Label(frame_vacinar, text="Selecione o rebanho: ")
    selecionar_rebanho_label.grid(row=0, column=2, padx=10, pady=10)
    global rebanho_selecionado
    rebanho_selecionado = StringVar()
    selecionar_rebanho = ttk.Combobox(frame_vacinar, textvariable=rebanho_selecionado)
    
    selecionar_rebanho['values'] = receber_rebanho()
    selecionar_rebanho['state'] = 'readonly'

    selecionar_rebanho.grid(row=0, column=3, padx=10, pady=10)

    botao_vainar = Button(frame_vacinar, text="Vacinar", width=20, command=lambda:adicionar_ao_banco("rebanho"))
    botao_vainar.grid(row=0, column=4, padx=10, pady=10)

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
#janela para mostrar tabela com os ingredientes da racao e seus valores nutricionais

def janela_ingredientes():
    for widgets in root.winfo_children():
        widgets.destroy()
    cria_menu()
    def selecionar_dados_arvore(e):
        id_ingredientes_entry.delete(0, END)
        ingrediente_entry.delete(0, END)
        magnesio_entry.delete(0, END)
        potassio_entry.delete(0, END)
        sodio_entry.delete(0, END)
        enxofre_entry.delete(0, END)
        cobalto_entry.delete(0, END)
        cobre_entry.delete(0, END)
        iodo_entry.delete(0, END)
        ferro_entry.delete(0, END)
        manganes_entry.delete(0, END) 
        selenio_entry.delete(0, END) 
        zinco_entry.delete(0, END) 
        vitamina_a_entry.delete(0, END)
        vitamina_d_entry.delete(0, END)
        calcio_entry.delete(0, END) 
        fosforo_entry.delete(0, END)
        proteina_entry.delete(0, END)
        energia_entry.delete(0, END)

        selecionado = my_tree.focus()

        valor = my_tree.item(selecionado, 'values')

        id_ingredientes_entry.insert(0, valor[0])
        ingrediente_entry.insert(0, valor[1])
        magnesio_entry.insert(0, valor[2])
        potassio_entry.insert(0, valor[3])
        sodio_entry.insert(0, valor[4])
        enxofre_entry.insert(0, valor[5])
        cobalto_entry.insert(0, valor[6])
        cobre_entry.insert(0, valor[7])
        iodo_entry.insert(0, valor[8])
        ferro_entry.insert(0, valor[9])
        manganes_entry.insert(0, valor[10])
        selenio_entry.insert(0, valor[11])
        zinco_entry.insert(0, valor[12])
        vitamina_a_entry.insert(0, valor[13])
        vitamina_d_entry.insert(0, valor[14])
        calcio_entry.insert(0, valor[15])
        fosforo_entry.insert(0, valor[16])
        proteina_entry.insert(0, valor[17])
        energia_entry.insert(0, valor[18])


    root.geometry("1600x800")
    
    #adicionando estilo
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map('Treeview', background=[('selected', "#347083")])

    global my_tree

    #criando frame da treeview
    frame_ingredients = Frame(root)
    frame_ingredients.pack(pady=10)

    #criando o scroll da treeview
    tree_scroll = Scrollbar(frame_ingredients)
    tree_scroll.pack(side=RIGHT, fill=Y)

    #criando a treeview
    my_tree = ttk.Treeview(frame_ingredients, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    #configurando o scroll
    tree_scroll.config(command=my_tree.yview)

    #difinindo as colunas
    my_tree['columns'] = ("ID", "Ingrediente", "Magnésio", "Potássio", "Sódio", "Enxofre", "Cobalto", "Cobre", "Iodo", "Ferro", "Manganês", "Selênio", "Zinco", "Vitamina A", "Vitamina D", "Cálcio", "Fósforo", "Proteina", "Energia")
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ID", width=50, anchor=W)
    my_tree.column("Ingrediente", width=140, anchor=W)
    my_tree.column("Magnésio", width=80, anchor=CENTER)
    my_tree.column("Potássio", width=80, anchor=CENTER)
    my_tree.column("Sódio", width=80, anchor=CENTER)
    my_tree.column("Enxofre", width=80, anchor=CENTER)
    my_tree.column("Cobalto", width=80, anchor=CENTER)
    my_tree.column("Cobre", width=80, anchor=CENTER)
    my_tree.column("Iodo", width=80, anchor=CENTER)
    my_tree.column("Ferro", width=80, anchor=CENTER)
    my_tree.column("Manganês", width=80, anchor=CENTER)
    my_tree.column("Selênio", width=80, anchor=CENTER)
    my_tree.column("Zinco", width=80, anchor=CENTER)
    my_tree.column("Vitamina A", width=80, anchor=CENTER)
    my_tree.column("Vitamina D", width=80, anchor=CENTER)
    my_tree.column("Cálcio", width=80, anchor=CENTER)
    my_tree.column("Fósforo", width=80, anchor=CENTER)
    my_tree.column("Proteina", width=80, anchor=CENTER)
    my_tree.column("Energia", width=80, anchor=CENTER)

    #criando as headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ID", text="ID", anchor=W)
    my_tree.heading("Ingrediente", text="Ingrediente", anchor=W)
    my_tree.heading("Magnésio", text="Magnésio", anchor=CENTER)
    my_tree.heading("Potássio", text="Potássio", anchor=CENTER)
    my_tree.heading("Sódio", text="Sódio", anchor=CENTER)
    my_tree.heading("Enxofre", text="Enxofre", anchor=CENTER)
    my_tree.heading("Cobalto", text="Cobalto", anchor=CENTER)
    my_tree.heading("Cobre", text="Cobre", anchor=CENTER)
    my_tree.heading("Iodo", text="Iodo", anchor=CENTER)
    my_tree.heading("Ferro", text="Ferro", anchor=CENTER)
    my_tree.heading("Manganês", text="Manganês", anchor=CENTER)
    my_tree.heading("Selênio", text="Selênio", anchor=CENTER)
    my_tree.heading("Zinco", text="Zinco", anchor=CENTER)
    my_tree.heading("Vitamina A", text="Vitamina A", anchor=CENTER)
    my_tree.heading("Vitamina D", text="Vitamina D", anchor=CENTER)
    my_tree.heading("Cálcio", text="Cálcio", anchor=CENTER)
    my_tree.heading("Fósforo", text="Fósfore", anchor=CENTER)
    my_tree.heading("Proteina", text="Proteina", anchor=CENTER)
    my_tree.heading("Energia", text="Energia", anchor=CENTER)

    #alternando as cores das linhas
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    #adicionando as caixas de entrada
    data_frame = LabelFrame(root, text="Ingredientes")
    data_frame.pack(fill="x", expand="yes", padx=20)
    global id_ingredientes_entry
    id_ingredientes_label = Label(data_frame, text="ID")
    id_ingredientes_label.grid(row=0, column=0, padx=10, pady=10)
    id_ingredientes_entry = Entry(data_frame)
    id_ingredientes_entry.grid(row=0, column=1, padx=10, pady=10)
    global ingrediente_entry
    ingrediente_label = Label(data_frame, text="Ingrediente")
    ingrediente_label.grid(row=0, column=2, padx=10, pady=10)
    ingrediente_entry = Entry(data_frame)
    ingrediente_entry.grid(row=0, column=3, padx=10, pady=10)
    global magnesio_entry
    magnesio_label = Label(data_frame, text="Magnésio")
    magnesio_label.grid(row=0, column=4, padx=10, pady=10)
    magnesio_entry = Entry(data_frame)
    magnesio_entry.grid(row=0, column=5, padx=10, pady=10)
    global potassio_entry
    potassio_label = Label(data_frame, text="Potássio")
    potassio_label.grid(row=1, column=0, padx=10, pady=10)
    potassio_entry = Entry(data_frame)
    potassio_entry.grid(row=1, column=1, padx=10, pady=10)
    global sodio_entry
    sodio_label = Label(data_frame, text="Sódio")
    sodio_label.grid(row=1, column=2, padx=10, pady=10)
    sodio_entry = Entry(data_frame)
    sodio_entry.grid(row=1, column=3, padx=10, pady=10)
    global enxofre_entry
    enxofre_label = Label(data_frame, text="Enxofre")
    enxofre_label.grid(row=1, column=4, padx=10, pady=10)
    enxofre_entry = Entry(data_frame)
    enxofre_entry.grid(row=1, column=5, padx=10, pady=10)
    global cobalto_entry
    cobalto_label = Label(data_frame, text="Cobalto")
    cobalto_label.grid(row=1, column=6, padx=10, pady=10)
    cobalto_entry = Entry(data_frame)
    cobalto_entry.grid(row=1, column=7, padx=10, pady=10)
    global cobre_entry
    cobre_label = Label(data_frame, text="Cobre")
    cobre_label.grid(row=2, column=0, padx=10, pady=10)
    cobre_entry = Entry(data_frame)
    cobre_entry.grid(row=2, column=1, padx=10, pady=10)
    global iodo_entry
    iodo_label = Label(data_frame, text="Iodo")
    iodo_label.grid(row=2, column=2, padx=10, pady=10)
    iodo_entry = Entry(data_frame)
    iodo_entry.grid(row=2, column=3, padx=10, pady=10)
    global ferro_entry
    ferro_label = Label(data_frame, text="Ferro")
    ferro_label.grid(row=2, column=4, padx=10, pady=10)
    ferro_entry = Entry(data_frame)
    ferro_entry.grid(row=2, column=5, padx=10, pady=10)
    global manganes_entry
    manganes_label = Label(data_frame, text="Manganês")
    manganes_label.grid(row=2, column=6, padx=10, pady=10)
    manganes_entry = Entry(data_frame)
    manganes_entry.grid(row=2, column=7, padx=10, pady=10)
    global selenio_entry
    selenio_label = Label(data_frame, text="Selênio")
    selenio_label.grid(row=2, column=8, padx=10, pady=10)
    selenio_entry = Entry(data_frame)
    selenio_entry.grid(row=2, column=9, padx=10, pady=10)
    global zinco_entry
    zinco_label = Label(data_frame, text="Zinco")
    zinco_label.grid(row=3, column=0, padx=10, pady=10)
    zinco_entry = Entry(data_frame)
    zinco_entry.grid(row=3, column=1, padx=10, pady=10)
    global vitamina_a_entry
    vitamina_a_label = Label(data_frame, text="Vitamina A")
    vitamina_a_label.grid(row=3, column=2, padx=10, pady=10)
    vitamina_a_entry = Entry(data_frame)
    vitamina_a_entry.grid(row=3, column=3, padx=10, pady=10)
    global vitamina_d_entry
    vitamina_d_label = Label(data_frame, text="Vitamina A")
    vitamina_d_label.grid(row=3, column=4, padx=10, pady=10)
    vitamina_d_entry = Entry(data_frame)
    vitamina_d_entry.grid(row=3, column=5, padx=10, pady=10)
    global calcio_entry
    calcio_laabel = Label(data_frame, text="Cálcio")
    calcio_laabel.grid(row=3, column=6, padx=10, pady=10)
    calcio_entry = Entry(data_frame)
    calcio_entry.grid(row=3, column=7, padx=10, pady=10)
    global fosforo_entry
    fosforo_label = Label(data_frame, text="Fósforo")
    fosforo_label.grid(row=3, column=8, padx=10, pady=10)
    fosforo_entry = Entry(data_frame)
    fosforo_entry.grid(row=3, column=9, padx=10, pady=10)
    global proteina_entry
    proteina_label = Label(data_frame, text="Proteina")
    proteina_label.grid(row=4, column=0, padx=10, pady=10)
    proteina_entry = Entry(data_frame)
    proteina_entry.grid(row=4, column=1, padx=10, pady=10)
    global energia_entry
    energia_label = Label(data_frame, text="Energia")
    energia_label.grid(row=4, column=2, padx=10, pady=10)
    energia_entry = Entry(data_frame)
    energia_entry.grid(row=4, column=3, padx=10, pady=10)


    query_database("ingredientes")

    #adicionando botões
    button_frame = LabelFrame(root, text="Ações")
    button_frame.pack(fill="x", expand="yes", padx=20)

    update_button = Button(button_frame, text="Atualizar", command=lambda:atualizar_dados("ingredientes"))
    update_button.grid(row=0 , column=0 , padx=10, pady=10)

    add_button = Button(button_frame, text="Adicionar", command=lambda:adicionar_ao_banco("ingredientes"))
    add_button.grid(row=0 , column=1 , padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remover", command=lambda:remover("ingredientes", id_ingredientes_entry.get()))
    remove_all_button.grid(row=0 , column=2 , padx=10, pady=10)

    #bind th treeview
    my_tree.bind("<ButtonRelease-1>", selecionar_dados_arvore) 


#-----------------------------------------------------------------------------------------

cria_menu()
frame_incial = LabelFrame(root, text="")
frame_incial.pack(fill="x", expand="yes", padx=20)
titulo = Label(frame_incial, text="Casima Agrícola", font=("Helvetica", 40)).pack(padx=30, pady=30)

root.mainloop()