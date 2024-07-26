import sqlite3

conn = sqlite3.connect('videoteca.bd')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        diretor TEXT,
        ano INTEGER,
        genero TEXT,
        preco REAL
    )
''')



# import csv
# filmes = [
#     ["O Poderoso Chefão", "Francis Ford Coppola", 1972, "Crime", 25.99],
#     ["O Senhor dos Anéis: A Sociedade do Anel", "Peter Jackson", 2001, "Fantasia", 30.99],
#     ["Pulp Fiction", "Quentin Tarantino", 1994, "Crime", 19.99],
#     ["O Iluminado", "Stanley Kubrick", 1980, "Terror", 15.99],
#     ["Matrix", "Lana Wachowski", 1999, "Ação", 22.99]
# ]

# with open('filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
   
#    escritor = csv.writer(csvfile)
#    escritor.writerow(['titulo', 'diretor', 'ano', 'genero', 'preco'])
#    escritor.writerows(filmes)

# with open('filmes.csv', 'r', newline='', encoding='utf-8') as csvfile:
#     leitor = csv.reader(csvfile)
#     next(leitor)
#     cursor.executemany('INSERT INTO filmes (titulo, diretor, ano, genero, preco) VALUES (?, ?, ?, ?, ?)', leitor)

#     conn.commit()
#     conn.close()



