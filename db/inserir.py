import sqlite3

conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()


def salvar(numero, status):
    cursor.execute("""
    INSERT INTO contato (numero, status)
    VALUES (?,?)
    """, (numero, status))

    conn.commit()
    conn.close()

    print('Dados inseridos com sucesso.')
