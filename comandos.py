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
    print("Erro")

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

conexao.commit()
conexao.close()
