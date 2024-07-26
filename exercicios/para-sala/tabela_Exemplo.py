import sqlite3

#conn- armazena a conexao do banco de dados
conn = sqlite3.connect('exemplo.db')

#apontar a informaçao que quer mexer (tipo o raio do mySQL)
cursor = conn.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL
               )
               """)
#Inserir dados
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Joao', 25)")
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?,?)", ("Thais", 20))
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?,?)", ("Maria", 28))

#atualizar dados
#cursor.execute("UPDATE usuarios SET idade = 25 WHERE nome = 'Thais'")
#cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (27, "Joao"))

#Deletar dados (diversas formas)
#cursor.execute("DELETE FROM usuarios WHERE idade IN (?, ?)", (25, 20))
#cursor.execute("DELETE FROM usuarios WHERE idade = ?", (25,))
#cursor.execute("DELETE FROM usuarios WHERE nome = ?", ("Joao",))
#cursor.execute("DELETE FROM usuarios WHERE idade <25")
#cursor.execute("DELETE FROM usuarios WHERE nome 'Thais'")



#selecionando dados
cursor.execute ("SELECT * FROM usuarios")

for linha in cursor.fetchall():#buscar todos os registros selecionados
    print (linha)

#salvar as mudanças
conn.commit()
#Fechando cursor
cursor.close()
# Fechando conexao
conn.close()

