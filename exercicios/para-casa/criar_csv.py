#Crie o Arquivo CSV:

import csv

filmes = [
    ['As Vantagens de Ser Invisível','Stephen Chbosky',2012,'Drama',23.99],
    ['O Hobbit','Peter Jackson',2012,'Fantasia',19.99],
    ['Azul é a Cor Mais Quente','Abdellatif Kechiche',2013,'Drama',24.99],
    ['Her','Spike Jonze',2013,'Drama',26.99],
    ['Bacurau','Kleber Mendonça Filho',2019,'Drama',30.99]
]

with open('arquivos_csv/filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'diretor', 'ano','genero','preco'])  # Escreve o cabeçalho
    escritor.writerows(filmes)