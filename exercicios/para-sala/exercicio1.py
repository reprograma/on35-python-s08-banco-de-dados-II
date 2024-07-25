import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('banco_dados/escola.db')
cursor = conn.cursor()

# Cria a tabela estudantes se ela não existir
sql_query = ("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

cursor.execute(sql_query)

# Lista de estudantes para inserir
estudantes = [
#     ('Alice', 21),
#     ('Bob', 22),
     ('Charlie', 23),
     ('Jamile',29),
     ('Bel',30)
 ]

# Insere vários estudantes de uma vez
insert_datas = ("INSERT INTO estudantes (nome, idade) VALUES (?, ?)")

cursor.executemany(insert_datas, estudantes)

# Seleciona todos os registros da tabela "estudantes"
sql_query = ("SELECT * FROM estudantes")

cursor.execute(sql_query)

registros = cursor.fetchall()

# Imprime os registros
for registro in registros:
    print(registro)

# Atualiza a idade de Bob para 23
update_datas = ("UPDATE estudantes SET idade = ? WHERE nome = ?")
cursor.execute(update_datas, (26, 'Bob'))

# Remove o estudante Charlie
delete_datas = ("DELETE FROM estudantes WHERE nome = ?")
cursor.execute(delete_datas, ('Charlie',))

# Seleciona os estudantes com idade maior que 21
sql_query = ("SELECT * FROM estudantes WHERE idade > 21 ORDER BY idade")
cursor.execute(sql_query)
registros = cursor.fetchall() #significa buscar todos os registros que foi selecionada pelo select

# Imprime os registros
for registro in registros:
    print(registro)


# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()
