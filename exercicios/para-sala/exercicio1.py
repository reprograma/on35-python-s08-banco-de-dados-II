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
    ('Alice', 21),
    ('Bob', 22),
    ('Charlie', 23)
]
# Insere vários estudantes de uma vez
cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)

#Parte 3: Consultando Dados*

# Seleciona todos os registros da tabela "estudantes"
cursor.execute("SELECT * FROM estudantes")
registros = cursor.fetchall()

# Imprime os registros
for registro in registros:
    print(registro)

# cursor.execute("SELECT * FROM estudantes")`**: Executa a consulta SQL para selecionar todos os registros da tabela "estudantes".
# registros = cursor.fetchall()`**: Recupera todos os registros da consulta em uma lista de tuplas.
# for registro in registros:`**: Itera sobre os registros e imprime cada um deles.

#Parte 4: Atualizando Dados

# Atualiza a idade de Bob para 23
cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Bob'))
# `UPDATE estudantes SET idade = ? WHERE nome = ?`**: Atualiza a coluna "idade" na tabela "estudantes" para o valor `?` (23) onde a coluna "nome" é igual a `?` (Bob).

# Remove o estudante Charlie
cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))

#DELETE FROM estudantes WHERE nome = ?`**: Remove o registro da tabela "estudantes" onde o nome é igual a `?` (Charlie)

#Parte 6: Consulta com Condições
# Seleciona os estudantes com idade maior que 21
cursor.execute("SELECT * FROM estudantes WHERE idade > 21")
registros = cursor.fetchall()

# Imprime os registros
for registro in registros:
    print(registro)

#SELECT * FROM estudantes WHERE idade > 21`**: Seleciona todos os registros da tabela "estudantes" onde a coluna "idade" é maior que 21.



# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()

#parte3
# Conexão com o banco de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Seleciona todos os registros da tabela "estudantes"
cursor.execute("SELECT * FROM estudantes")
registros = cursor.fetchall()

# Imprime os registros
for registro in registros:
    print(registro)

# Fecha a conexão
cursor.close()
conn.close()


#parte 4
cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?",(23,"Bob"))                           
#parte5
# Remove o estudante Charlie
cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))

cursor.execute("DELETE FROM estudantes WHERE nome = 'Charlie'")


# Salva as alterações no banco de dados
conn.commit()
cursor.execute("DELETE FROM estudantes WHERE nome = 'Charlie'")


# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()
