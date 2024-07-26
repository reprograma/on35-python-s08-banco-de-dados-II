import csv
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Executando a consulta
cursor.execute('SELECT * FROM filmes')

# Escrevendo os resultados em um novo arquivo CSV
with open('exportados_filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Escrevendo o cabeçalho
    writer.writerow(['id', 'titulo', 'diretor', 'ano', 'genero', 'preco'])
    # Escrevendo os dados
    writer.writerows(cursor.fetchall())

conn.close()