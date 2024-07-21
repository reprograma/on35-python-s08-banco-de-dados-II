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

# Lista de estudantes para inserir
estudantes = [
#     ('Alice', 21),
#     ('Bob', 22),
     ('Charlie', 23),
     ('Jamile',29),
     ('Bel',30)
 ]

# Insere vários estudantes de uma vez
cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)

# Seleciona todos os registros da tabela "estudantes"
cursor.execute("SELECT * FROM estudantes")
registros = cursor.fetchall()

# Imprime os registros
for registro in registros:
    print(registro)

# Atualiza a idade de Bob para 23
cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (26, 'Bob'))

# Remove o estudante Charlie
cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))

# Seleciona os estudantes com idade maior que 21
cursor.execute("SELECT * FROM estudantes WHERE idade > 21 ORDER BY idade")
registros = cursor.fetchall()

# Imprime os registros
for registro in registros:
    print(registro)


# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()
