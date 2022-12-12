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

cursor.execute("SELECT tag FROM animais WHERE tipo = 'Bovino' ")
reusltado = cursor.fetchall()



print(reusltado)

for animal in reusltado:
    print(animal)
    print(animal[0])
    sql= "INSERT INTO vacinacao (vacina_id, animais_tag, data) VALUES (%s, %s, %s)"
    vaalores = (str(1), str(animal[0]), "2022-10-10" )
    try:
        cursor.execute(sql, vaalores)
    except Error as e:
        print(e)


conexao.commit()
conexao.close()