## Exercício de Sala 🏫:

Este exercício te guia para o mundo dos bancos de dados SQLite com Python, mostrando como criar, inserir, consultar, atualizar e remover dados de uma tabela chamada "estudantes".

**Parte 1: Criando o Banco de Dados e a Tabela**

```python
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Cria a tabela estudantes se ela não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()
```

* **`import sqlite3`**: Importa a biblioteca SQLite3 para trabalhar com bancos de dados SQLite em Python.
* **`conn = sqlite3.connect('escola.db')`**: Cria uma conexão com o banco de dados SQLite chamado "escola.db". Se o banco de dados não existir, ele será criado automaticamente.
* **`cursor = conn.cursor()`**: Cria um cursor para interagir com o banco de dados.
* **`cursor.execute(...)`**: Executa comandos SQL no banco de dados.
* **`CREATE TABLE IF NOT EXISTS estudantes (...)`**: Cria a tabela "estudantes" se ela não existir. A tabela tem as colunas:
    * `id`: Um inteiro que é a chave primária (única) e autoincrementada.
    * `nome`: Um texto que não pode ser nulo.
    * `idade`: Um inteiro que não pode ser nulo.
* **`conn.commit()`**: Salva as alterações feitas no banco de dados.
* **`cursor.close()`**: Fecha o cursor.
* **`conn.close()`**: Fecha a conexão com o banco de dados.

**Parte 2: Inserindo Dados**

```python
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Lista de estudantes para inserir
estudantes = [
    ('Alice', 21),
    ('Bob', 22),
    ('Charlie', 23)
]

# Insere vários estudantes de uma vez
cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()
```

* **`cursor.executemany(...)`**: Executa um comando SQL várias vezes com diferentes valores.
* **`INSERT INTO estudantes (nome, idade) VALUES (?, ?)`**: Insere um novo registro na tabela "estudantes". Os valores `?` são substituídos pelos dados da lista `estudantes`.

**Parte 3: Consultando Dados**

```python
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Seleciona todos os registros da tabela "estudantes"
cursor.execute("SELECT * FROM estudantes")
registros = cursor.fetchall()

# Imprime os registros
for registro in registros:
    print(registro)

# Fecha a conexão
cursor.close()
conn.close()
```

* **`cursor.execute("SELECT * FROM estudantes")`**: Executa a consulta SQL para selecionar todos os registros da tabela "estudantes".
* **`registros = cursor.fetchall()`**: Recupera todos os registros da consulta em uma lista de tuplas.
* **`for registro in registros:`**: Itera sobre os registros e imprime cada um deles.

**Parte 4: Atualizando Dados**

```python
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Atualiza a idade de Bob para 23
cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Bob'))

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()
```

* **`UPDATE estudantes SET idade = ? WHERE nome = ?`**: Atualiza a coluna "idade" na tabela "estudantes" para o valor `?` (23) onde a coluna "nome" é igual a `?` (Bob).

**Parte 5: Removendo Dados**

```python
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Remove o estudante Charlie
cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()
```

* **`DELETE FROM estudantes WHERE nome = ?`**: Remove o registro da tabela "estudantes" onde o nome é igual a `?` (Charlie).

**Parte 6: Consulta com Condições**

```python
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Seleciona os estudantes com idade maior que 21
cursor.execute("SELECT * FROM estudantes WHERE idade > 21")
registros = cursor.fetchall()

# Imprime os registros
for registro in registros:
    print(registro)

# Fecha a conexão
cursor.close()
conn.close()
```

* **`SELECT * FROM estudantes WHERE idade > 21`**: Seleciona todos os registros da tabela "estudantes" onde a coluna "idade" é maior que 21.

**Exercícios com CSV e Python:**

**1. Leitura de CSV:**

```python
import csv

with open('produtos.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        print(linha)
```

* **`with open(...) as csvfile`**: Abre o arquivo CSV "produtos.csv" para leitura.
* **`leitor = csv.reader(csvfile)`**: Cria um leitor CSV para ler as linhas do arquivo.
* **`for linha in leitor:`**: Itera sobre as linhas do arquivo CSV e imprime cada linha.

**2. Escrita em CSV:**

```python
import csv

funcionarios = [
    [1, 'Ana', 'Financeiro'],
    [2, 'Carlos', 'TI'],
    [3, 'Beatriz', 'RH']
]

with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'nome', 'departamento'])  # Escreve o cabeçalho
    escritor.writerows(funcionarios)  # Escreve os dados
```

* **`with open(...) as csvfile`**: Abre o arquivo CSV "funcionarios.csv" para escrita.
* **`escritor = csv.writer(csvfile)`**: Cria um escritor CSV para escrever dados no arquivo.
* **`escritor.writerow(...)`**: Escreve uma linha no arquivo CSV.
* **`escritor.writerows(...)`**: Escreve várias linhas no arquivo CSV.

**3. Importação de CSV para SQLite:**

```python
import sqlite3
import csv

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

conn.commit()
cursor.close()
conn.close()
```

* **`with open(...) as csvfile`**: Abre o arquivo CSV "clientes.csv" para leitura.
* **`next(leitor)`**: Pula a primeira linha do arquivo CSV, que é o cabeçalho.
* **`for linha in leitor:`**: Itera sobre as linhas do arquivo CSV e insere cada linha na tabela "clientes" do banco de dados.

**4. Exportação de SQLite para CSV:**

```python
import sqlite3
import csv

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
dados = cursor.fetchall()

with open('exportados_clientes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'nome', 'email'])
    escritor.writerows(dados)

cursor.close()
conn.close()
```

* **`cursor.execute("SELECT * FROM clientes")`**: Seleciona todos os registros da tabela "clientes".
* **`dados = cursor.fetchall()`**: Recupera todos os registros em uma lista de tuplas.
* **`with open(...) as csvfile`**: Abre o arquivo CSV "exportados_clientes.csv" para escrita.
* **`escritor = csv.writer(csvfile)`**: Cria um escritor CSV para escrever dados no arquivo.
* **`escritor.writerow(...)`**: Escreve o cabeçalho do arquivo CSV.
* **`escritor.writerows(...)`**: Escreve os dados da tabela "clientes" no arquivo CSV.

**Exercício: Utilizando Joins em SQLite com Python**

**Parte 1: Criação das Tabelas e Inserção de Dados**

```python
import sqlite3

# Conectar ao banco de dados (ou criar um banco de dados)
conexao = sqlite3.connect('exercicio_join.db')
cursor = conexao.cursor()

# Criar a tabela de clientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Criar a tabela de pedidos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY,
        data TEXT NOT NULL,
        valor REAL NOT NULL,
        cliente_id INTEGER,
        FOREIGN KEY (cliente_id) REFERENCES clientes (id)
    )
''')

# Inserir dados na tabela de clientes
clientes = [
    (1, 'Ana', 'ana@example.com'),
    (2, 'Bruno', 'bruno@example.com'),
    (3, 'Carla', 'carla@example.com')
]
cursor.executemany('INSERT INTO clientes VALUES (?, ?, ?)', clientes)

# Inserir dados na tabela de pedidos
pedidos = [
    (1, '2023-07-01', 100.50, 1),
    (2, '2023-07-02', 200.75, 2),
    (3, '2023-07-03', 150.00, 1)
]
cursor.executemany('INSERT INTO pedidos VALUES (?, ?, ?, ?)', pedidos)

# Salvar (commit) as mudanças
conexao.commit()
```

**Parte 2: Consultas com Joins**

```python
# Consulta 1: Obter todos os pedidos com os dados dos clientes
cursor.execute('''
    SELECT pedidos.id, pedidos.data, pedidos.valor, clientes.nome, clientes.email
    FROM pedidos
    JOIN clientes ON pedidos.cliente_id = clientes.id
''')
resultado = cursor.fetchall()
print("Pedidos com dados dos clientes:")
for linha in resultado:
    print(linha)

# Consulta 2: Obter todos os clientes que não têm pedidos
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
```

* **`JOIN`**: Combina registros de duas ou mais tabelas com base em uma coluna relacionada entre elas.
* **`LEFT JOIN`**: Retorna todos os registros da tabela à esquerda (clientes) e os registros correspondentes da tabela à direita (pedidos). Se não houver correspondência, os resultados da tabela à direita serão NULL.

**Tarefas do Exercício:**

* Execute o código fornecido para criar o banco de dados, as tabelas e inserir os dados.
* Analise os resultados das consultas com joins:
    * A primeira consulta deve retornar todos os pedidos junto com os dados dos clientes.
    * A segunda consulta deve retornar todos os clientes que não têm pedidos associados.

**Explicação:**

* **`JOIN`**: Utilizado para combinar registros de duas ou mais tabelas com base em uma coluna relacionada entre elas.
* **`LEFT JOIN`**: Retorna todos os registros da tabela à esquerda (clientes) e os registros correspondentes da tabela à direita (pedidos). Se não houver correspondência, os resultados da tabela à direita serão NULL.

**Observação:**

* Certifique-se de ter o Python instalado e as bibliotecas necessárias (`sqlite3` e `csv`).
* Substitua os nomes dos arquivos CSV ("produtos.csv", "funcionarios.csv", "clientes.csv") pelos nomes dos seus arquivos.
* Execute os scripts em ordem para garantir que os bancos de dados e as tabelas sejam criados corretamente.


---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
