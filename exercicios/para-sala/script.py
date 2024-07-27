#importando a tabela
import sqlite3

# conectando ao banco de dados (bd) e também pode criar, se não existir.
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

#Inserir dados
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Daiana', 36)")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Angelina', 33)")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Camila", 36))

# Atualizar um registro que já existe
#cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (20, "Angelina"))

# Remover um registro

#cursor.execute("DELETE FROM usuarios WHERE nome = ?", ('Camila',))
#cursor.execute("DELETE FROM usuarios WHERE nome = ?", ('Daiana',))
# cursor.execute("DELETE FROM usuarios WHERE nome = ?", ('Angelina',))

#Pra deletar varios registros por IDs
#cursor.execute("DELETE FROM usuarios WHERE id IN (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

#Selecionar os dados
cursor.execute("SELECT * FROM usuarios" )

# for para imprimir linha por linha dentro de um loop
for linha in cursor.fetchall():
    print(linha)

#Salvar mudanças
conn.commit()

#Fechando cursor
cursor.close()
#Boa prática para fechar a relação com o banco de dados.
conn.close()
