import sqlite3
import csv
 
#conectando ao banco de dados (ou criar, se não existir)
conn = sqlite3.connect("videoteca.db")

#criando um cursor para executar comandos SQL
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    diretor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    genero TEXT NOT NULL,
    preco REAL NOT NULL
    )
""")

with open ('filmes.csv', newline= '', encoding= 'utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)
    for linha in leitor:
        if len(linha) == 5:
            cursor.execute(
                "INSERT INTO filmes (titulo, diretor, ano, genero, preco) VALUES (?, ?, ?, ?, ?)",
                (linha[0], linha[1], linha[2], linha[3], linha[4])
             )
        else:
            print(f"Linha com número incorreto de colunas: {linha}")


conn.commit()
cursor.close()
conn.close()