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



#Search all
def search(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        return c.fetchall()
    except Error as ex:
        print(ex)


vsql = "SELECT * FROM tb_contacts"
search(vcon, vsql)  # comando

response = search(vcon, vsql)

# for r in response:
#     # print(r)

# Search one 
def searchOne(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        return c.fetchall()
    except Error as ex:
        print(ex)

vsqlOne = "SELECT * FROM tb_contacts WHERE N_IDCONTACT=5"
# print(searchOne(vcon, vsqlOne))


#search by letter
def searchSpecific(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        return c.fetchall()
    except Error as ex:
        print(ex)


vsqlOne = "SELECT * FROM tb_contacts WHERE T_NAMECONTACT LIKE '%o%'" #tudo que tiver a letra o (%o => Terminam com a letra o || o% => começam com a letra o)

print(searchSpecific(vcon, vsqlOne))
