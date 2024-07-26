import sqlite3
import csv

conn=sqlite3.connect("videoteca.db")
cursor=conn.cursor()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT NOT NULL,
               diretor TEXT NOT NULL,
               ano INTEREGER NOT NULL,
               genero TEXT NOT NULL,
               preco REAL NOT NULL)   
        """)

cursor.execute("SELECT * FROM filmes")
dados = cursor.fetchall()

#Criando arquivo CSV
with open('filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'diretor', 'ano', 'genero', 'preco'])
    escritor.writerows(dados)

#Adcionando filmes no arquivo CSV
filme = [
    [1, 'O Poderoso Chefão','Francis Ford Coppola',1972,'Drama',25.99],
    [2, 'O Senhor dos Anéis: A Sociedade do Anel','Peter Jackson',2001,'Fantasia',30.99],
    [3, 'A Origem','Christopher Nolan',2010,'Ficção Científica',19.99],
    [3, 'A Vida de Brian','Terry Gilliam',1979,'Comédia',15.99],
    [4, 'Pulp Fictio','Quentin Tarantino',1994,'Crime',22.99]   ] 

with open('filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'diretor', 'ano', 'genero', 'preco'])  # Escreve o cabeçalho
    escritor.writerows(filme) 

conn.commit()
cursor.close()
conn.close()