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
    print("Cursor criado")
except Error as e:
    print(e)

cursor.execute("""CREATE TABLE IF NOT EXISTS ingredientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ingrediente VARCHAR(255),
        magnesio DECIMAL(10,2),
        potassio DECIMAL(10,2),
        sodio DECIMAL(10,2),
        enxofre DECIMAL(10,2),
        cobalto DECIMAL(10,2),
        cobre DECIMAL(10,2),
        iodo DECIMAL(10,2),
        ferro DECIMAL(10,2),
        manganes DECIMAL(10,2),
        selenio DECIMAL(10,2),
        zinco DECIMAL(10,2),
        vitamina_a DECIMAL(10,2),
        vitamina_d DECIMAL(10,2),
        calcio DECIMAL(10,2),
        fosforo DECIMAL(10,2),
        proteina DECIMAL(10,2),
        energia DECIMAL(10,2)
        )""")

conexao.commit()
conexao.close()

print("SUCESSO")