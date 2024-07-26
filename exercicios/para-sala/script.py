import sqlite3

#Conectando ao bd (ou criar, se não existir)
conn = sqlite3.connect("exemplo.db")

#Cruar um cursos para executar comandos - igual quando selecionamos e damos o raio
cursor = conn.cursor()

#execute o comando do sql
cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL
               )
                """)

#Inserir dados 
#cursor.execute("INSERT INTO usuarios(nome,idade) VALUES ('Daiana',36)")
#cursor.execute("INSERT INTO usuarios(nome,idade) VALUES ('Angelina',33)")
#cursor.execute("INSERT INTO usuarios(nome,idade) VALUES ('Fernanda',36)")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Camila", 36))

#Alterando usuário existente
#cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (20, "Angelina"))

#Remover um registro da tabela
#cursor.execute("DELETE FROM usuarios WHERE nome = ? ", ('Daiana',))
#cursor.execute("DELETE FROM usuarios WHERE nome = 'Daiana'")

#Excluindo usuário existente
#cursor.execute("DELETE FROM usuarios WHERE id = ?",(8,))

#Selecionando os dados 
cursor.execute("SELECT * FROM usuarios")

for linha in cursor.fetchall():
    print(linha)


#salvando as mudanças
conn.commit()

#Fechando cursor
cursor.close()

#Fechando as conexões
conn.close()
