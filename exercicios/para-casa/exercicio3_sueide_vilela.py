#Importe os Dados para o Banco de Dados:

import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

with open('filmes.csv', 'r', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    
    cabecalho = next(leitor)
    
    for linha in leitor:
        try:
            cursor.execute('''
                INSERT INTO filmes (titulo, diretor, ano, genero, preco)
                VALUES (?, ?, ?, ?, ?)
            ''', (linha[0], linha[1], int(linha[2]), linha[3], float(linha[4])))
        except ValueError as e:
            print(f"Erro ao processar a linha: {linha}. Erro: {e}")


conn.commit()
conn.close()

