import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS estudantes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER NOT NULL
               )
               """)

alunos = [
    ('Alice', 21),
    ('Bob', 22),
    ('Charlie', 23)
]

# Executa vários
# cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", alunos)

# cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Bob'))

# a vírgula depois de 'Charlie' indica que tem mais registros depois
# cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))

cursor.execute("SELECT * FROM estudantes")
for linha in cursor.fetchall():
    print(linha)

cursor.execute("SELECT * FROM estudantes WHERE idade > 21")
registros = cursor.fetchall()
for registro in registros:
    print(registro)


conn.commit()

cursor.close()
conn.close()
