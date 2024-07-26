import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL)
""")

estudantes = [
    ('Alice', 21),
    ('Bob', 22),
    ('Charlie', 23)
]
#cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)

cursor.execute("SELECT * FROM estudantes")
#cursor.execute ("SELECT * FROM estudantes where idade == 21")
registros = cursor.fetchall()
for registro in registros:
    print(registro)

#cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Bob'))
#cursor.execute("DELETE FROM estudantes WHERE nome IN (?, ?)", ('Charlie', 'Bob'))


conn.commit()
cursor.close()
conn.close()
