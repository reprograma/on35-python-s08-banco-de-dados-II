import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Cria a tabela estudantes se ela não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()