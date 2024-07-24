#2. Crie o Arquivo CSV:**

# Crie um arquivo CSV chamado `filmes.csv` com as seguintes colunas:
#     `titulo`
#     `diretor`
#     `ano`
#     `genero`
#     `preco` 
# Adicione pelo menos 5 filmes diferentes ao arquivo `filmes.csv`.

# Exemplo do Arquivo `filmes.csv`:

# csv
# titulo,diretor,ano,genero,preco
# O Poderoso Chefão,Francis Ford Coppola,1972,Drama,25.99
# O Senhor dos Anéis: A Sociedade do Anel,Peter Jackson,2001,Fantasia,30.99
# A Origem,Christopher Nolan,2010,Ficção Científica,19.99
# A Vida de Brian,Terry Gilliam,1979,Comédia,15.99
# Pulp Fiction,Quentin Tarantino,1994,Crime,22.99

import csv

filmes = [
    ['O Poderoso Chefão','Francis Ford Coppola',1972,'Drama',25.99],
    ['O Senhor dos Anéis: A Sociedade do Anel','Peter Jackson',2001,'Fantasia',30.99],
    ['A Origem','Christopher Nolan',2010,'Ficção Científica',19.99],
    ['A Vida de Brian','Terry Gilliam',1979,'Comédia',15.99],
    ['Pulp Fiction','Quentin Tarantino',1994,'Crime',22.99]
]

with open('arquivos_csv/filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'diretor', 'ano','genero','preco'])  # Escreve o cabeçalho
    escritor.writerows(filmes)  # Escreve os dados

print('Arquivo filmes.csv criado!')
