
# **7. Exporte os Dados para um Novo CSV:**

# * Escreva um script Python (chamado `exportar_filmes.py`) que exporte os dados da tabela `filmes` para um novo arquivo CSV chamado `exportados_filmes.csv`.

import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM filmes")
dados = cursor.fetchall()

with open('exportados.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escreve o cabeçalho no arquivo CSV
    escritor_csv.writerow(['titulo', 'diretor', 'ano', 'genero', 'preco'])
    
    # Escreve os dados no arquivo CSV
    escritor_csv.writerows(dados)

cursor.close()
conn.close()
