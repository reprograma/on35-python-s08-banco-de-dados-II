import csv
import sqlite3

# #Abre o arquivo produtos e imprime na tela do terminal

# #O newline evita que leia linha em brancos e o utf-8 é para linguagem brasileira com os caracteres e simbolos
# with open('arquivos_csv/produtos.csv', newline='', encoding='utf-8') as csvfile:
#     leitor = csv.reader(csvfile)
#     for linha in leitor:
#         print(linha)

# #-----------------------------------------------------------

# funcionarios = [
#     [1, 'Ana', 'Financeiro'],
#     [2, 'Carlos', 'TI'],
#     [3, 'Beatriz', 'RH']
# ]

# #cria um arquivo funcionarios e escreve a lista de listas que foi definida na variavel funcionarios

# with open('arquivos_csv/funcionarios.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     escritor = csv.writer(csvfile)
#     escritor.writerow(['id', 'nome', 'departamento'])  # Escreve o cabeçalho
#     escritor.writerows(funcionarios)  # Escreve os dados

conn = sqlite3.connect('banco_dados/empresa.db')
cursor = conn.cursor()

create_table = ("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

cursor.execute(create_table)

with open('arquivos_csv/clientes.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  # Pula o cabeçalho
    for linha in leitor:
        insert_datas = "INSERT INTO clientes (nome, email) VALUES (?, ?)"
        cursor.execute(insert_datas,(linha[1], linha[2]))

sql_query = ("SELECT * FROM clientes")

cursor.execute(sql_query)
dados = cursor.fetchall() #significa buscar todos os registros que foi selecionada pelo select

with open('arquivos_csv/exportados_clientes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'nome', 'email'])
    escritor.writerows(dados)

conn.commit()
cursor.close()
conn.close()