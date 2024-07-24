# 7. Exporte os Dados para um Novo CSV:**

# Escreva um script Python (chamado `exportar_filmes.py`) que exporte os dados da tabela `filmes` para um novo arquivo CSV chamado `exportados_filmes.csv`.

import sqlite3
import csv

# Conectar ao banco de dados (ou criar um banco de dados)
conn = sqlite3.connect('banco_dados/videoteca.db')
cursor = conn.cursor()

sql_query = ("SELECT * FROM filmes")

cursor.execute(sql_query)
datas = cursor.fetchall() #significa buscar todos os registros que foi selecionada pelo select

with open('arquivos_csv/exportados_filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'diretor', 'ano', 'genero', 'preco'])
    escritor.writerows(datas)

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()