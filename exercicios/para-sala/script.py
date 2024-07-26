import sqlite3

#Conectando ao bd (ou criar, se não existir)
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
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Daiana', 36)")
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Angelina', 33)")
cursor.execute("INSERT into usuarios (nome, idade) VALUES (?,?)", ("Camila", 36))

#atualizar um registro
cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?",(20, 'Angelina'))

#remover um registro da tabela
cursor.execute("DELETE FROM usuarios WHERE nome = ?", ('Daiana',))

#deletar varios registros por id
cursor.execute("DELETE FROM usuarios WHERE id IN (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

#Selecionar dados
cursor.execute("SELECT * FROM usuarios")

for linha in cursor.fetchall():
    print(linha)

#Salvar as mudanças
conn.commit()
#Fechando conexão
conn.close()