import sqlite3

#Conectando ao banco de dados (ou criar, se nao existir)
conn = sqlite3.connect("exemplo.db")

#Criando um cursor para executar comandos SQL
cursor = conn.cursor()

#Cria a tabela usuarios se ela não existir
cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL
                )
                """)

# inserir dados
# cursor.execute("""
#                 INSERT INTO usuarios (nome, idade) VALUES ('Daiana',36),
#                                                           ('Angelina',33)
#                """)

# inserir dados
# cursor.execute("INSERT INTO usuarios (nome,idade) VALUES (?,?)",("Angelina",33))
# cursor.execute("INSERT INTO usuarios (nome,idade) VALUES (?,?)",("Daiana",36))
# cursor.execute("INSERT INTO usuarios (nome,idade) VALUES (?,?)",("Camila",36))


# Atualizar um registro que ja existe
# cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (20,"Angelina"))

# Remover um registro da tabela
# cursor.execute("DELETE FROM usuarios WHERE nome = ?", ("Camila",)) #dessa forma, precisa colocar a virgula mesmo sem um outro parametro

# Remover um registro da tabela
# cursor.execute("DELETE FROM usuarios WHERE nome = 'Camila'")

# Remover mais de um registro da tabela
# cursor.execute("DELETE FROM usuarios WHERE id IN (?,?)",(1,2))

#Selecionando os dados
cursor.execute("SELECT * FROM usuarios")

#cursor.fetchall() significa buscar todos os registros que foi selecionada pelo select
#for percorre cada linha
for linha in cursor.fetchall(): #fetchall = buscar
    print(linha)

#Salvar as mudanças = gravar as mudanças que estamos fazendo no banco de dados
conn.commit()

#Fechando cursor = libera o espaço que estavamos usando
cursor.close()

#Fechando conexão = é uma boa prática fechar o banco de dados depois das alterações para não deixar aberto consumindo recursos
conn.close()