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

# Criar entrada no banco

name="José Cordeiro Neto"
number="11984550603"
email="zecaxcr@gmail.com"

vsql = "INSERT INTO tb_contacts(T_NAMECONTACT, T_NUMBERCONTACT, T_EMAILCONTACT) VALUES('"+name+"','"+number+"', '"+email+"')" #usando as variaveis


def insert(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit() #necessário o commit, se não não salva
        print("Registro Inserido")
    except Error as ex:
        print(ex)


insert(vcon, vsql) #comando
