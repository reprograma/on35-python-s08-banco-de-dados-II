# Exercício 1 >> Crie o Banco de Dados e a Tabela:
# Crie um banco de dados SQLite chamado `videoteca.db`. 

# Toda vez que abrirmos um novo arquivo, teremos que dar o comando de import
import sqlite3 

# Conectando ao banco de dados (ou criar, se não existir)
conn = sqlite3.connect('videoteca.db')

# Criando um cursor para executar comandos SQL.
cursor = conn.cursor()

#Crie uma tabela chamada `filmes` com as seguintes colunas:
#   `id` (INTEGER, chave primária, autoincremento)
#   `titulo`(TEXT)
#   `diretor`(TEXT)
#   `ano` (INTEGER)
#   `genero`(TEXT)
#   `preco`(REAL)

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

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()

