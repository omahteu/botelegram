import sqlite3


conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE contato (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        numero VARCHAR(14) NOT NULL,
        status TEXT NOT NULL
);
""")

print('Tabela criada com sucesso.')
conn.close()
