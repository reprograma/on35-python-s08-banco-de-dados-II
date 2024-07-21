import csv
import sqlite3

#O newline evita que leia linha em brancos e o utf-8 é para linguagem brasileira com os caracteres e simbolos
with open('produtos.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        print(linha)

funcionarios = [
    [1, 'Ana', 'Financeiro'],
    [2, 'Carlos', 'TI'],
    [3, 'Beatriz', 'RH']
]

with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'nome', 'departamento'])  # Escreve o cabeçalho
    escritor.writerows(funcionarios)  # Escreve os dados

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

with open('clientes.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  # Pula o cabeçalho
    for linha in leitor:
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (linha[1], linha[2]))

cursor.execute("SELECT * FROM clientes")
dados = cursor.fetchall()

with open('exportados_clientes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'nome', 'email'])
    escritor.writerows(dados)

conn.commit()
cursor.close()
conn.close()