import sqlite3

# Conectando ao banco de dados (ou criar, se não existir)
conn = sqlite3.connect("exemplo.db")

# Criando um cursor para executar comandos SQL
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL
               )
               """)

# Inserir Dados
#cursor.execute("INSERT INTO usuarios (nome,idade) VALUES('Daiana',36 )")
#cursor.execute("INSERT INTO usuarios (nome,idade) VALUES('Angelina',33 )")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Camila", 36))

#Atualizar um registro que já existe
#cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (20, "Angelina"))

#Remover um registro da tabela
#cursor.execute("DELETE FROM usuarios WHERE id = 2")
#cursor.execute("DELETE FROM usuarios WHERE id = ?", (4,))
#cursor.execute("DELETE FROM usuarios WHERE nome = 'Daiana'")

# Deletar Varios registro por id
# cursor.execute("DELETE FROM usuarios WHERE id IN (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

# Selecionando dados
cursor.execute("SELECT * FROM usuarios")

for linha in cursor.fetchall():
    print(linha)

# Aplicando mudanças
conn.commit()
# Fechar cursor
cursor.close
# Fechando conexão
conn.close()


