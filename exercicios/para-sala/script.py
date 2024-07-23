import sqlite3

#Conectando ao banco dados ( ou criar, se não existir)
conn = sqlite3.connect("exemplo.db") #variavel de conexão

#Criando um cursor para executar comandos SQL(Selecionar o local)
cursor = conn.cursor() #variavél

# 3 aspas duplas quando for usar mais de uma linha
cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT NOT NULL,
                  idade INTEGER NOT NULL
               )
               """)

#inserir dados 
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES('Daiana', 36)")
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES('Angelina', 33)")
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)",("Camila", 36)) # para usar as ""duplas

# Atulizar um registro que já existe 

# cursor.execute("UPDATE usuarios SET idade = ? WHERE nome =?",(20,"Angelina"))
#Deletar varios registro por id
#cursor.execute("DELETE FROM usuarios WHERE id IN (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

#Remover um registro da tabela
# cursor.execute("DELETE FROM usuarios WHERE nome = ?",('Camila',))
#cursor.execute("DELETE FROM usuarios WHERE nome = 'Camila'")

#Selecionando dados
cursor.execute("SELECT * From usuarios")
for linha in cursor.fetchall():
    print(linha)

#Salvar as mudanças 
conn.commit()
#fechando o cursor
cursor.close()
#Fechando a conexão
conn.close()
