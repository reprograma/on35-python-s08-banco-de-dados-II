#import csv

#with open('produtos.csv', newline='', encoding='UTF-8') as csvfile:
#    leitor = csv.reader(csvfile)
#    for linha in leitor:
#        print(linha)

# import csv
# funcionarios = [
#     [1,'Milena','TI'],
#     [2, 'Ellen', 'Desenvolvimento'],
#     [3, 'Danda', 'Dados'],
#     [4, 'Camila', 'Prof']
# ]
# with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     escritor = csv.writer(csvfile)
#     escritor.writerow(['id', 'nome', 'departamento'])
#     escritor.writerows(funcionarios) 

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
#     next(leitor)  # Pula o cabeçalho
#     for linha in leitor:
#         cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (linha[1], linha[2]))
        
# conn.commit()
# cursor.close()
# conn.close()

# # Exportação de SQLite para CSV:
# import sqlite3
# import csv
# conn = sqlite3.connect('empresa.db')
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM clientes")
# dados = cursor.fetchall()
# with open('exportados_clientes.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     escritor = csv.writer(csvfile)
#     escritor.writerow(['id', 'nome', 'email'])    
#     escritor.writerows(dados)
# cursor.close()
# conn.close()

#IMPRIMIR TABELA NO TERMINAL
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
conn.close()

