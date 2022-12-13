from tkinter import*
import mysql.connector
from mysql.connector import Error
import csv

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
    print(e)

cursor.execute("CREATE VIEW despesas AS SELECT fornecedores.nome, estoque.item, transacao.valor_unitario, transacao.quantidade, transacao.valor_unitario*transacao.quantidade FROM fornecedores, estoque, transacao WHERE transacao.f_id=fornecedores.cnpj AND transacao.e_id=estoque.id")
#cursor.execute("SHOW TABLES")
#print(cursor.fetchall())

conexao.commit()
conexao.close()