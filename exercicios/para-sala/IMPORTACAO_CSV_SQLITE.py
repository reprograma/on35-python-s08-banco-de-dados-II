# # 3. Importação de CSV para SQLite:
# import sqlite3
# import csv
# conn = sqlite3.connect('empresa.db')
# cursor = conn.cursor()
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS clientes (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     email TEXT NOT NULL
# )
# """)    
# with open('clientes.csv', newline='', encoding='utf-8') as csvfile:
#     leitor = csv.reader(csvfile)
#     next(leitor)  # Pula a primeira linha que é o cabeçalho
#     for linha in leitor: #itera sobre as linhas
#         cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (linha[1], linha[2])) #insere dados



# Exportação de SQLite para CSV:
# IMPRIMIR TABELA NO TERMINAL
import sqlite3
from tabulate import tabulate
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM clientes")
dados = cursor.fetchall()
# Imprimindo a tabela com tabulate
headers = ["id", "nome", "email"]
print(tabulate(dados, headers=headers, tablefmt="grid"))
cursor.close()
conn.close

