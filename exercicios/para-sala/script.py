import sqlite3

#Conectando ao banco de dados (ou criar, se nao existir)
conn = sqlite3.connect('Exemplo.db')

#Criando um cursor para executar comandos SQL 
cursor = conn.cursor()


cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL
               )
              """)

#Inserir Dados
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Daiana', 36)")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Angelina', 33)")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Karine', 24)")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Camila", 36))

#Atualizar um registro que ja existe
#cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (20, "Angelina"))

#Deletar usuario pelo ID
##cursor.execute("DELETE FROM usuarios WHERE id = 7")

#Selecionando dados
cursor.execute("SELECT * FROM usuarios")

for linha in cursor.fetchall():
    print(linha) 

#Salvar as mudancas
conn.commit()
#Fechando cursos
cursor.close()
#Fechando conexao
conn.close()
