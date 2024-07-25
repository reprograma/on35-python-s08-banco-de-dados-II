import sqlite3

# Conectando ao banco de dados (ou criar, se não existir)
conn = sqlite3.connect("exemplo.db")

# Cria um cursor para executar comandos SQL no BD conectado e armazenado na variável 'conn'
cursor = conn.cursor()

# Executando um comando SQL de criar a tabela 'usuarios'
cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL
               )
                """)

# Insere dados
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Daiana', 36)")
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Angelina', 33)")
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)",
#                ("Camila", 33))  # - -> outra forma de escrever

# Atualiza um registro que já existe
# cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (20, "Angelina"))

# Remover um registro
# Jeito 1: cursor.execute("DELETE FROM usuarios WHERE nome = '?'", ('Camila',))
# Jeito 2: cursor.execute("DELETE FROM usuarios WHERE nome = 'Camila'")
# Deletar vários rgistros
# cursor.execute("DELETE FROM usuarios WHERE id IN (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
# cursor.execute("DELETE FROM usuarios WHERE id = ?", (20,) and (21,))
# cursor.execute("DELETE FROM usuarios WHERE id BETWEEN 13 AND 15")

# Selecionar dados
cursor.execute("SELECT * FROM usuarios")

for linha in cursor.fetchall():  # percorre todos os registros que foram selecionados pelo comando SELECT
    print(linha)

# Aplica as alterações no banco de dados
conn.commit()
# Fecha o cursor
cursor.close()
# Fecha a conexão com o banco de dados
conn.close()
