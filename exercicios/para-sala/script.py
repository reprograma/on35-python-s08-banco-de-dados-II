import sqlite3

conn = sqlite3.connect("exemplo.db")

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT NOT NULL,
                  idade INTEGER NOT NULL
               )
               """)

cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Daiana', 36)")
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Angelina', 33)")


cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (20, "Angelina"))

cursor.execute("DELETE FROM usuarios WHERE nome = 'Daiana'")


#salva mudanças
conn.commit()

#fecha cursor
cursor.close

#fecha conexão
conn.close()
















