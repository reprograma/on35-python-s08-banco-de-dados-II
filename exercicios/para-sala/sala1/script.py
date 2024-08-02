import sqlite3

#conectando ao banco de dados (ou criar, se não existir)
conn = sqlite3.connect("exemplo.db")

#criando um cursor para executar comandos SQL
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER NOT NULL
               )
               """)

#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Héllyda', 36)")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Xainã', 27)")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Camila", 36))

#cursor.execute("UPDATE usuarios SET idade = ? WHERE NOME = ?", (20, "Angelina"))


#Remover um registro da tabela
#cursor.execute("DELETE FROM usuarios WHERE nome = '?'", ('Daiana',))
#cursor.execute("DELETE FROM usuarios WHERE nome = 'Daiana'")

#cursor.execute("DELETE FROM usuarios WHERE id IN (?, ?, ?, ?)")

cursor.execute("SELECT * FROM usuarios")

for linha in cursor.fetchall():
    print(linha)




#As seguintes vão ser sempre as últimas linhas
#salvando as mudanças
conn.commit()
#fechando cursor
cursor.close()
#fechando conexão
conn.close()