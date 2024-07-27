import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

filmes = [
    ('O Poderoso Chefão','Francis Ford Coppola',1972,'Drama',25.99),
    ('O Senhor dos Anéis: A Sociedade do Anel','Peter Jackson',2001,'Fantasia',30.99),
    ('A Origem','Christopher Nolan',2010,'Ficção Científica',19.99),
    ('A Vida de Brian','Terry Gilliam',1979,'Comédia',15.99),
    ('Pulp Fiction','Quentin Tarantino',1994,'Crime',22.99)
]

# Insere vários filmes de uma vez
cursor.executemany("INSERT INTO filmes (titulo, diretor, ano, genero, preco) VALUES (?, ?, ?, ?, ?)", filmes)

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()