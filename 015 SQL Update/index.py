import sqlite3
from sqlite3 import Error, connect

# Criar conexão

def DatabaseConnection():
    local = "D:\\OneDrive\\Developer\\SQL\\banco\\agenda.db"
    con = None
    try:
        con = sqlite3.connect(local)
    except Error as ex:
        print(ex)
    return con

vcon = DatabaseConnection()

# Criar conexão

# Deletar entrada no banco

def update(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit() #necessário o commit, se não não salva
    except Error as ex:
        print(ex)
    finally:
        print("Atualizado com sucesso")


                        #CUIDADO, se não usar o WHERE voce deleta todos os dados do banco
                        
vsql="DELETE FROM tb_contacts WHERE N_IDCONTACT=4"
update(vcon, vsql) #comando

