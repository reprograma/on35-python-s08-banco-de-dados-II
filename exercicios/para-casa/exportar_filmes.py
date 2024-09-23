# Exercício 7 >> 7. Exporte os Dados para um Novo CSV:

# Escreva um script Python (chamado exportar_filmes.py) que exporte os dados da tabela 
# filmes para um novo arquivo CSV chamado exportados_filmes.csv.

import sqlite3
import csv

# Conectar ao banco de dados
conn = sqlite3.connect('videoteca.db')

# Criar um cursor
cursor = conn.cursor()

# Selecionar todos os registros da tabela 'filmes'
cursor.execute("SELECT * FROM filmes")
filmes = cursor.fetchall()

# Exportar os dados para um arquivo CSV
with open('exportados_filmes.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escrever o cabeçalho (nomes das colunas)
    escritor_csv.writerow([i[0] for i in cursor.description])
    
    # Escrever os dados da tabela
    escritor_csv.writerows(filmes)

# Fechar o cursor e a conexão
cursor.close()
conn.close()

print("Dados exportados para 'exportados_filmes.csv' com sucesso!")
