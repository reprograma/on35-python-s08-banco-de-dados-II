import sqlite3

#conectando ao banco de dados (ou criar, se não existir)
conn = sqlite3.connect("videoteca.db")

#criando um cursor para executar comandos SQL
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS filmes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT NOT NULL,
               diretor TEXT NOT NULL,
               ano INTEGER NOT NULL,
               genero TEXT NOT NULL,
               preco REAL NOT NULL
               )
               """)


#As seguintes vão ser sempre as últimas linhas
#salvando as mudanças
conn.commit()
#fechando cursor
cursor.close()
#fechando conexão
conn.close()





