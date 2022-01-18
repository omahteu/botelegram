import sqlite3
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))
db_path = path.join(BASE_DIR, "contatos.db")
with sqlite3.connect(db_path) as db:
    cursor = db.cursor()

    def salvar(numero, status):
        cursor.execute("""
        INSERT INTO contato (numero, status)
        VALUES (?,?)
        """, (numero, status))

        db.commit()
        db.close()

        print('Dados inseridos com sucesso.')

# salvar('+5585999831355', 'Ativado')