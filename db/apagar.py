import sqlite3
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))
db_path = path.join(BASE_DIR, "contatos.db")
with sqlite3.connect(db_path) as db:
    cursor = db.cursor()


    def deletar(numero):
        cursor.execute("DELETE FROM contato WHERE numero = ?", (numero,))
        db.commit()
        print('Registro excluido com sucesso.')
        db.close()
