import sqlite3

#Connect to SQL data base
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM Filmes')
filmes = cursor.fetchall()

#show results
for filme in filmes:
    print(f"ID: {filme[0]}, Título: {filme[1]}, Diretor: {filme[2]}, Ano: {filme[3]}, Gênero: {filme[4], }")
    
    conn.close()