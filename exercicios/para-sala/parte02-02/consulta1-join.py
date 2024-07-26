# Consulta 1: Obter todos os pedidos com os dados dos clientes
import sqlite3

conexao = sqlite3.connect('exercicio_join.db')
cursor = conexao.cursor()

cursor.execute('''
    SELECT pedidos.id, pedidos.data, pedidos.valor, clientes.nome, clientes.email
    FROM pedidos
    JOIN clientes ON pedidos.cliente_id = clientes.id
''')
resultado = cursor.fetchall()
print("Pedidos com dados dos clientes:")
for linha in resultado:
    print(linha)

# Fechar a conexão
conexao.close()