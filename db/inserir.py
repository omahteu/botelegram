import sqlite3

conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()


def salvar(numero, status):
    cursor.execute(f"INSERT INTO clientes (numero, status) VALUES ({numero}, {status})")

    conn.commit()
    conn.close()

    print('Dados inseridos com sucesso.')
