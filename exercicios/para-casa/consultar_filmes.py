import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM filmes')
filmes = cursor.fetchall()

# Imprime os registros
for filme in filmes:
   print(f'ID: {filme[0]}, Título: {filme[1]}, Diretor: {filme[2]}, Ano: {filme[3]}, Gênero: {filme[4]}, Preço: {filme[5]}')

# Fecha a conexão
conn.close()