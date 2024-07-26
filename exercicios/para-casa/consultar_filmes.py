## Exercício de Casa 🏠 Gerenciando uma Videoteca com SQLite e CSV

#4-Consultar e Exibir os Dados
import sqlite3
from tabulate import tabulate

# Conectar ao banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Executar consulta
cursor.execute("SELECT * FROM filmes")
dados = cursor.fetchall()

# Imprimir a tabela com tabulate
headers = ["id", "titulo", "diretor", "ano", "genero", "preco"]
print(tabulate(dados, headers=headers, tablefmt="grid"))

# Fechar a conexão
cursor.close()
conn.close()
