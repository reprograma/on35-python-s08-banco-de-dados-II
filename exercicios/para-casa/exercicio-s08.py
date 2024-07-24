# 1. Crie o Banco de Dados e a Tabela:

# Crie um banco de dados SQLite chamado videoteca.db.
# Crie uma tabela chamada filmes com as seguintes colunas:
# id (INTEGER, chave primária, autoincremento)
# titulo (TEXT)
# diretor (TEXT)
# ano (INTEGER)
# genero (TEXT)
# preco (REAL)

# import sqlite3

# conn = sqlite3.connect ("videoteca.db")
# cursor = conn.cursor()

# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS filmes (
#                  id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  titulo TEXT NOT NULL,
#                  diretor TEXT NOT NULL,
#                  ano INTEGER NOT NULL,
#                  genero TEXT NOT NULL,
#                  preco REAL NOT NULL
#                )
#            """)

# conn.commit()

# cursor.close()
# conn.close()

# 2. Crie o Arquivo CSV:

# Crie um arquivo CSV chamado filmes.csv com as seguintes colunas:
# titulo
# diretor
# ano
# genero
# preco
# Adicione pelo menos 5 filmes diferentes ao arquivo filmes.csv.

# import csv 
# filmes=[
#     [1,'O homem que mudou o jogo','Bennett Miller','2011','Esporte/Comédia', '8.00'],
#     [2,'Quebrando a banca', 'Robert Luketic', '2008', 'Crime/Ação', '7.00'],
#     [3, 'O jogo da imitação','Morten Tyldum', '2014', 'Thriller/Guerra', '5.00'],
#     [4, 'Her', 'Spike Jonze', '2013', 'Romance/Ficção científica', '4.00'],
#     [5, 'Minority Report','Steven Spielberg', '2002', 'Ação/Ficção científica', '6.00' ]
# ]

# with open ('filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     escritor=csv.writer(csvfile)
#     escritor.writerow (['id','titulo','diretor','ano','genero','preco'])
#     escritor.writerows(filmes)

#3. Importe os Dados para o Banco de Dados:

# Escreva um script Python (chamado importar_filmes.py) que leia os dados do filmes.csv 
# e os insira na tabela filmes no banco de dados videoteca.db.

# 4. Consulte e Exiba os Dados:

# Escreva um script Python (chamado consultar_filmes.py) 
# que selecione e exiba todos os registros da tabela filmes.

# 5. Atualize os Dados:

# Escreva um script Python (chamado atualizar_filme.py) que 
# atualize o preço de um filme específico (por exemplo, 
# aumente o preço do filme com id 2).

# 6. Remova um Filme:

# Escreva um script Python (chamado remover_filme.py) que remova 
# um filme específico da tabela (por exemplo, remova o filme com id 3).

# 7. Exporte os Dados para um Novo CSV:

# Escreva um script Python (chamado exportar_filmes.py) que exporte os dados da tabela 
# filmes para um novo arquivo CSV chamado exportados_filmes.csv.


