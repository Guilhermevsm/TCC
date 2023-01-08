from tkinter import*
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from scipy.optimize import linprog
import csv
import os
import datetime




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



cursor.execute("""CREATE TABLE IF NOT EXISTS vendas (
        id_venda INT AUTO_INCREMENT PRIMARY KEY,
        animal_venda INT(10) NOT NULL,
        valor_venda INT(10) NOT NULL ,
        peso_venda INT(10) NOT NULL ,
        data DATE,
        comprador_enda VARCHAR(255)
        )""") 


conexao.commit()
conexao.close()


