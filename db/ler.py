import sqlite3
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))
db_path = path.join(BASE_DIR, "contatos.db")
with sqlite3.connect(db_path) as db:
    cursor = db.cursor()

    def leitura():
        cursor.execute("SELECT * FROM contato")
        dados = cursor.fetchall()
        return dados

        # for linha in cursor.fetchall():
        #     print(linha)

        # db.close()
