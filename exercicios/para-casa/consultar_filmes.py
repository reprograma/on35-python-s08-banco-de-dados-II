# **4. Consulte e Exiba os Dados:**
import sqlite3
import tabulate

#Exibir no terminal a tabela
from tabulate import tabulate
#criando a conexão 
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

#selecionando a tabela para consultar os dados
cursor.execute("SELECT * FROM filmes")
dados = cursor.fetchall()

# Imprimindo a tabela com tabulate
headers = ["id", "titulo", "diretor","ano","genero","preco"]
print(tabulate(dados, headers=headers, tablefmt="grid"))
cursor.close()
conn.close()

