import mysql.connector


# Conecte-se ao banco de dados MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="minha-senha-secreta",
    database="petshop"
)

# Crie a tabela de login
mycursor = mydb.cursor()

__all__ = ['mycursor', 'mydb']