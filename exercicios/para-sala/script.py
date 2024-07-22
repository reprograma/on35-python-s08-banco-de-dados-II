import sqlite3

# Conectando ou criando uma conexão com banco de dados (bd), arquivo db (database)
conn = sqlite3.connect ("exemplo.db")

# criando um cursor para executar comandos SQl (mão do selecionar, selecionar a linha para rodar aqui no vs code, navegando dentro do bd, SQL)
cursor= conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL,
                 idade INTEGER NOT NULL
           )
           """)


# inserir dados
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Daiana', 36)")
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Angelina', 33)")


# salvar as mudanças, comentar
conn.commit ()

#Fechando a conexão em cada alteração
conn.close()


# continuação parte da tarde ausente

# Cria a tabela estudantes se ela não existir
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS estudantes (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER NOT NULL
# )
# """)

# Lista de estudantes para inserir
# estudantes = [
#     ("Alice", 21),
#     ('Bob', 22),
#     ('Charlie', 23)
# ]

# # Insere vários estudantes de uma vez
# cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)

# # Salva as alterações no banco de dados
# conn.commit()

# # Fecha a conexão
# cursor.close()
# conn.close()



# import sqlite3

# # Conexão com o banco de dados
# conn = sqlite3.connect('escola.db')
# cursor = conn.cursor()
# #  parte:
# # ------------------------
# # Parte 3: Consultando Dados

# import sqlite3

# # Conexão com o banco de dados
# conn = sqlite3.connect('escola.db')
# cursor = conn.cursor()

# # Seleciona todos os registros da tabela "estudantes"
# cursor.execute("SELECT * FROM estudantes")
# registros = cursor.fetchall()

# # Imprime os registros
# for registro in registros:
#     print(registro)

# # Fecha a conexão
# cursor.close()
# conn.close()
# cursor.execute("SELECT * FROM estudantes"): Executa a consulta SQL para selecionar todos os registros da tabela "estudantes".
# registros = cursor.fetchall(): Recupera todos os registros da consulta em uma lista de tuplas.
# for registro in registros:: Itera sobre os registros e imprime cada um deles.

# # Parte 4: Atualizando Dados

# import sqlite3

# # Conexão com o banco de dados
# conn = sqlite3.connect('escola.db')
# cursor = conn.cursor()

# # Atualiza a idade de Bob para 23
# cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Bob'))

# # Salva as alterações no banco de dados
# conn.commit()

# # Fecha a conexão
# cursor.close()
# conn.close()
# UPDATE estudantes SET idade = ? WHERE nome = ?: Atualiza a coluna "idade" na tabela "estudantes" para o valor ? (23) onde a coluna "nome" é igual a ? (Bob).
# Parte 5: Removendo Dados

# import sqlite3

# # Conexão com o banco de dados
# conn = sqlite3.connect('escola.db')
# cursor = conn.cursor()

# # Remove o estudante Charlie
# cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))

# # Salva as alterações no banco de dados
# conn.commit()

# # Fecha a conexão
# cursor.close()
# conn.close()
# DELETE FROM estudantes WHERE nome = ?: Remove o registro da tabela "estudantes" onde o nome é igual a ? (Charlie).