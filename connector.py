import mysql.connector

# Conexão com o banco de dados
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Coloque sua senha aqui se tiver
        database="futebol"
    )

db = conectar_bd()
cursor = db.cursor()