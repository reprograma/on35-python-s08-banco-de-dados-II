# **1. Crie o Banco de Dados e a Tabela:**
import sqlite3
import csv

# Criando a conexão com o banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Cria a tabela filmes se ela não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        diretor TEXT NOT NULL,
        ano INTEGER,
        genero TEXT NOT NULL,
        preco REAL
)
""")
# **2. Escrita em CSV:**

# criando a lista dos filmes
filmes = [
     ['O Poderoso Chefão','Francis Ford Coppola',1972,'Drama',25.99],
     ['O Senhor dos Anéis: A Sociedade do Anel','Peter Jackson',2001,'Fantasia',30.99],
     ['A Origem','Christopher Nolan',2010,'Ficção Científica',19.99],
     ['A Vida de Brian','Terry Gilliam',1979,'Comédia',15.99],
     ['Pulp Fiction','Quentin Tarantino',1994,'Crime',22.99]
]

# escrevendo o csv
with open('filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
     escritor = csv.writer(csvfile)
     escritor.writerow(['titulo', 'diretor','ano','genero',"preco"])  # Escreve o cabeçalho
     escritor.writerows(filmes)  # Escreve os dados
  
# Fecha a conexão
cursor.close()
conn.close()


