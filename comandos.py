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

cursor.execute("ALTER TABLE animais ADD raca VARCHAR(255)")

cursor.execute("SELECT * FROM animais")
print(cursor.fetchall())



conexao.commit()
conexao.close()