import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()


cursor.execute('SELECT * FROM filmes')
filmes = cursor.fetchall()

for filme in filmes:
    print(f"ID: {filme[0]}")
    print(f"Título: {filme[1]}")
    print(f"Diretor: {filme[2]}")
    print(f"Ano: {filme[3]}")
    print(f"Gênero: {filme[4]}")
    print(f"Preço: R${filme[5]:.2f}\n")

# Fechando a conexão
conn.close()
