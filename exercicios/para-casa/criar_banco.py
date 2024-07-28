
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# # Cria a tabela estudantes se ela não existir
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS filmes (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     titulo TEXT,
#     diretor TEXT,
#     ano INTEGER,
#     genero TEXT,
#     preco REAL
   
# )
# """)


import csv

filmes = [
    
[1,'O Poderoso Chefão','Francis Ford Coppola',1972,'Drama',25.99],
[2,'O Senhor dos Anéis: A Sociedade do Anel','Peter Jackson',2001,'Fantasia',30.99],
[3,'A Origem','Christopher Nolan',2010,'Ficção Científica',19.99],
[4,'A Vida de Brian','Terry Gilliam',1979,'Comédia',15.99],
[5,'Pulp Fiction','Quentin Tarantino',1994,'Crime',22.99]
]

with open('filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:  
    escritor = csv.writer(csvfile)
    escritor.writerow(['id','titulo', 'diretor', 'ano', 'genero','preco'])
    escritor.writerows(filmes)


# Insere vários estudantes de uma vez
cursor.executemany("INSERT INTO filmes ('id','titulo', 'diretor', 'ano', 'genero','preco') VALUES (?, ?, ?, ?, ?, ?)", filmes)



# Salva as alterações no banco de dados
conn.commit()

# # Fecha a conexão
cursor.close()
conn.close()
