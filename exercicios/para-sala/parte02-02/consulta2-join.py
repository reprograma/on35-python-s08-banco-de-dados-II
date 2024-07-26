# Consulta 2: Obter todos os clientes que não têm pedidos

import sqlite3

conexao = sqlite3.connect('exercicio_join.db')
cursor = conexao.cursor()

cursor.execute('''
    SELECT clientes.id, clientes.nome, clientes.email
    FROM clientes
    LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id
    WHERE pedidos.id IS NULL
''')
resultado = cursor.fetchall()
print("\nClientes sem pedidos:")
for linha in resultado:
    print(linha)

# Fechar a conexão
conexao.close()