#arquivo usado para comandos sql


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
    

    cursor.execute("CREATE VIEW vacinados AS SELECT animais.tag, vacinacao.vacina_id, vacinas.nome FROM animais, vacinacao, vacinas WHERE animais.tag = vacinacao.animais_tag AND vacinacao.vacina_id = vacinas.id")


    #dando commit
    conexao.commit()

    #fechando a conexa
    conexao.close()

    print("Conexão com o banco feita com sucesso!")
except Error as e:
    aviso = ("Não foi possivel se conectar ao banco de dados \nErro: " + str(e))
    print("Conexão com o banco não foi sucedida!")