# **7. Exporte os Dados para um Novo CSV:**

# * Escreva um script Python (chamado `exportar_filmes.py`) que exporte os dados da tabela `filmes` 
# para um novo arquivo CSV chamado `exportados_filmes.csv`.

import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM filmes")
dados = cursor.fetchall()

with open('exportados_filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'titulo', 'diretor', 'ano', 'genero', 'preco'])
    escritor.writerows(dados)

cursor.close()
conn.close()


# * **`cursor.execute("SELECT * FROM clientes")`**: Seleciona todos os registros da tabela "clientes".
# * **`dados = cursor.fetchall()`**: Recupera todos os registros em uma lista de tuplas.
# * **`with open(...) as csvfile`**: Abre o arquivo CSV "exportados_clientes.csv" para escrita.
# * **`escritor = csv.writer(csvfile)`**: Cria um escritor CSV para escrever dados no arquivo.
# * **`escritor.writerow(...)`**: Escreve o cabeçalho do arquivo CSV.
# * **`escritor.writerows(...)`**: Escreve os dados da tabela "clientes" no arquivo CSV.