from tkinter import*
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from scipy.optimize import linprog
import csv
import os
import datetime



def arvore(animal):
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
    sql = "SELECT mae_tag, pai_tag FROM animais WHERE tag = %s"
    valor = (animal, )
    cursor.execute(sql, valor)
    resultado = cursor.fetchall()
    #print("animal = " + str(animal))
    #print("parentes = " + str(resultado))
    #print("mae = " + str(resultado[0][0]))
    #print("pai = " + str(resultado[0][1]))

    
    if resultado[0][0] != 0:
        arvore(resultado[0][0])
    if resultado[0][1] != 0:
        arvore(resultado[0][1])
    if resultado[0][0] == 0 and resultado[0][1] == 0:
        parentes.append(animal)
        return 
    print("return " + str(animal) + "\n")
    parentes.append(animal)


global parentes           
parentes = []  

arvore(20)
print(parentes)
