import csv

funcionarios = [
    [1, 'Ana', 'Financeiro', 'ana@gmail.com'],
    [2, 'Carlos', 'TI', 'carlos@gmail.com'],
    [3, 'Thais', 'RH', 'thais@gmail.com'],
    [3, 'Joao', 'RH', 'joao@gmail.com']
]

with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'nome', 'departamento', 'email'])  # Escreve o cabeçalho
    escritor.writerows(funcionarios)  # Escreve muitos dados