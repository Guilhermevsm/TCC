import mysql.connector
from mysql.connector import Error


try:
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "aneis1961",
        database = "casima"
    )
    #criando o cursor
    cursor = conexao.cursor()
    

    cursor.execute("UPDATE animais SET tipo = 'Bovino' WHERE tag = 2")


    #dando commit
    conexao.commit()

    #fechando a conexa
    conexao.close()

    print("Conexão com o banco feita com sucesso!")
except Error as e:
    aviso = ("Não foi possivel se conectar ao banco de dados \nErro: " + str(e))
    print("Conexão com o banco não foi sucedida!")