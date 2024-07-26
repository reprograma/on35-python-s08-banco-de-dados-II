import sqlite3

#conectando ao banco (ou criar, se não existir)
conn = sqlite3.connect("exemplo.db")

#criando um cursor para executar comandos sql
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL
               )
               """)

#inserir dados
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Daiana', 36)")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUE (?, ?)", ("Camila", 36))


#atualizar um registro que já existe (SET: significa definir)
#cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (20, "Angelina"))

#remover um registro da tebela
#cursor.execute("DELETE FROM usuarios WHERE nome = 'Daiana'")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Daiana', 36)")
#Deletar Varios registro por id
#cursor.execute("DELETE FROM usuarios WHERE id IN (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

#selecionar dados
#cursor.execute("SELECT * FROM usuarios")

for linha in cursor.fetchall ():   #fetchall: buscar
    print(linha)

#lista de estudantes para inserir
    estudantes = [
    ("Alice", 21),
    ('Bob', 22),
    ('Charlie', 23)
]

# Insere vários estudantes de uma vez
cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)



#fechando cursor
cursor.close()

#Salvar as mudanças
conn.commit()
#Fechando uma conexão
conn.close()



