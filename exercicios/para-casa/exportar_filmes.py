# 7. Exporte os Dados para um Novo CSV:

# Escreva um script Python (chamado exportar_filmes.py) que exporte os dados da tabela filmes para um novo arquivo CSV chamado exportados_filmes.csv.
# Exemplo do Arquivo filmes.csv:

import csv
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

dados = ("SELECT * FROM filmes")

cursor.execute(dados)
dados = cursor.fetchall() #busca todos os registros do arquivo selecionado

#criaando e escrevendo o arquivo CSV.
with open('exportados_filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id','titulo', 'diretor', 'ano', 'genero', 'preco'])
    escritor.writerows(dados)

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()