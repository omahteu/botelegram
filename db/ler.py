import sqlite3
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))
db_path = path.join(BASE_DIR, "contatos.db")
with sqlite3.connect(db_path) as db:
    cursor = db.cursor()

    def leitura():
        try:
            cursor.execute("""
            CREATE TABLE contato (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    numero VARCHAR(14) NOT NULL,
                    status TEXT NOT NULL
            );
            """)
            cursor.execute("SELECT * FROM contato")
            dados = cursor.fetchall()
            return dados
        except sqlite3.OperationalError:
            pass
