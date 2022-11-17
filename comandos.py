from tkinter import*
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from scipy.optimize import linprog
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
valores = []

with open('backup_funcionarios.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(row)
        
        

        info = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        try:
            cursor.execute(sql, info)
        except Error as e:
            print(e)

conexao.commit()
conexao.close()
