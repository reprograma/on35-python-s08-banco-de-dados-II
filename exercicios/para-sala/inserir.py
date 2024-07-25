import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Lista de estudantes para inserir
estudantes = [
    ('Alice', 21),
    ('Bob', 22),
    ('Charlie', 23)
]

# Insere vários estudantes de uma vez
cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()