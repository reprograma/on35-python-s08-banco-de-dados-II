import sqlite3
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    diretor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    genero TEXT NOT NULL,
    preco REAL NOT NULL
)
''')

conn.commit()
conn.close()

# Importe os Dados para o Banco de Dados:
import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

with open('filmes.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute('''
        INSERT INTO filmes (titulo, diretor, ano, genero, preco)
        VALUES (?, ?, ?, ?, ?)
        ''', (row['titulo'], row['diretor'], int(row['ano']), row['genero'], float(row['preco'])))

conn.commit()
conn.close()


       
#Consulte e Exiba os Dados:
import sqlite3


conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM filmes')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


# Atualize os Dados:

import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('''
UPDATE filmes
SET preco = ?
WHERE id = ?
''', (29.99, 2))

conn.commit()
conn.close()

# Remova um Filme

import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('DELETE FROM filmes WHERE id = ?', (3,))

conn.commit()
conn.close()


# Exporte os Dados para um Novo CSV
import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM filmes')
rows = cursor.fetchall()

column_names = [description[0] for description in cursor.description]

with open('exportados_filmes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(column_names)
    writer.writerows(rows) 

# Fechando a conexão
conn.close()



conn.commit()
conn.close()

