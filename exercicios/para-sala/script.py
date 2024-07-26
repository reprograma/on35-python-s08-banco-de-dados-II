import sqlite3

#Conectando ao banco dados (ou criar, se não existir)
conn = sqlite3.connect("exemplo.db")

#Criando um cursor para executar comandos SQL
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL
               )
               """)

#inserir dados
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Daiana', 36)")
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Angelina', 33)")
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Camila", 36))

#Atualizar um registro que ja existe
# cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (20, "Angelina"))

#Remover um registro da tabela
# cursor.execute("DELETE FROM usuarios WHERE nome = '?'", ('Daiana',))
# cursor.execute("DELETE FROM usuarios WHERE nome = 'Angelina'")

#Deletar Varios registro por id
# cursor.execute("DELETE FROM usuarios WHERE id IN (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (6, 7, 8, 9, 10, 11, 12, 13, 14, 15)) 

#Selecionando varios dados
cursor.execute("SELECT *FROM usuarios")

for linha in cursor.fetchall():
    print(linha)

# Salvando as mudanças
conn.commit()
#Fechando cursor
cursor.close()
#Fechando conexão
conn.close()
