import csv

filmes = [
    [ "Um Lugar Chamado Notting Hill", "Roger Michell", 1999, "Romance", 12.99],
    [ "Esposa de Mentirinha", "Dennis Dugan", 2011, "Comédia", 10.99],
    [ "Procurando Nemo", "Andrew Stanton", 2003, "Animação", 14.99],
    [ "Divertida Mente", "Pete Docter", 2015, "Animação, Comédia", 16.99],
    [ "Carol", "Todd Haynes", 2015, "Romance",  18.99]
]

with open('filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'diretor', 'ano', 'genero', 'preco' ])
    escritor.writerows(filmes)
