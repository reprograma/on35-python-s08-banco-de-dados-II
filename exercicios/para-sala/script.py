import sqlite3

# Conectando ao banco de dados (ou criar, se não existir)
conn = sqlite3.connect("exemplo.db") #data base

# Criando um cursor para executar comandos SQL.
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL
               )
               """)

#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Daiana', 36)")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Angelina', 33)")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Danieli', 33)")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Raquel', 38)")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?,?)" , ("Xainâ", 27))

# Atualizar um registo que já existe
#cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (20, "Angelina"))

#Remover um registro da tabela
#cursor.execute("DELETE FROM usuarios WHERE nome = ? ", ('Angelina',))
#cursor.execute("DELETE FROM usuarios WHERE nome = 'Daiana'")

# Remover um registro por iD
cursor.execute("DELETE FROM usuarios WHERE id IN (?)", (29,))

# Remover vários registro por iD
#cursor.execute("DELETE FROM usuarios WHERE id IN (?, ?, ?, ?, ?, ?)", (31, 32, 34, 36, 37, 39))

# Selecionar dados
cursor.execute("SELECT * FROM usuarios")

for linha in cursor.fetchall():
    print(linha)

# Ele salva as mudanças que estão sendo feitas no banco de dados de forma permanente.
# Só esta na minha máquina, quando eu dou esse comando, as alterações para o github
conn.commit()

# Boas práticas e fechamento do cursor (pois podemos trabalhar com mais de um cursor no banco de dados)
cursor.close()

# Esse comando é uma boa prática para não dar problemas.
# Podemos fazer outras solicitações e como fechamos, não irá alterar as alterações feitas no banco
conn.close()

