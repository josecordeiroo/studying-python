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

# Criar tabela
vsql = """CREATE TABLE tb_contacts(
            N_IDCONTACT INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NAMECONTACT VARCHAR(30),
            T_NUMBERCONTACT VARCHAR(14),
            T_EMAILCONTACT VARCHAR(30)
        );"""


def tableCreate(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        print("Tabela criada com sucesso")
    except Error as ex:
        print(ex)


tableCreate(vcon, vsql)

vcon.close()
