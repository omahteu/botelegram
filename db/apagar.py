import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()


def deletar(numero):
    cursor.execute("DELETE FROM contato WHERE numero = ?", (numero,))
    conn.commit()
    print('Registro excluido com sucesso.')
    conn.close()
