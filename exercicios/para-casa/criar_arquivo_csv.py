# Exercício de Casa 🏠 Gerenciando uma Videoteca com SQLite e CSV
#2-Criar o Arquivo CSV
import csv

# Dados dos filmes
filmes = [
    {"titulo": "A Origem", "diretor": "Christopher Nolan", "ano": 2010, "genero": "Sci-Fi", "preco": 17.99},
    {"titulo": "Matrix", "diretor": "The Wachowskis", "ano": 1999, "genero": "Sci-Fi", "preco": 12.99},
    {"titulo": "Clube da Luta", "diretor": "David Fincher", "ano": 1999, "genero": "Drama", "preco": 11.99},
    {"titulo": "Forrest Gump", "diretor": "Robert Zemeckis", "ano": 1994, "genero": "Drama", "preco": 12.99},
    {"titulo": "Clube da Luta", "diretor": "David Fincher", "ano": 1999, "genero": "Drama", "preco": 11.99},
    {"titulo": "O Senhor dos Anéis: A Sociedade do Anel", "diretor": "Peter Jackson", "ano": 2001, "genero": "Fantasia", "preco": 24.99},
    {"titulo": "Star Wars: Episódio V - O Império Contra-Ataca", "diretor": "Irvin Kershner", "ano": 1980, "genero": "Sci-Fi", "preco": 15.99},
    {"titulo": "O Cavaleiro das Trevas", "diretor": "Christopher Nolan", "ano": 2008, "genero": "Ação", "preco": 18.99},
    {"titulo": "Gladiador", "diretor": "Ridley Scott", "ano": 2000, "genero": "Ação", "preco": 16.99}
]

# Criar e escrever no arquivo CSV
with open('filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ["titulo", "diretor", "ano", "genero", "preco"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for filme in filmes:
        writer.writerow(filme)

print("Arquivo filmes.csv criado com sucesso!")

