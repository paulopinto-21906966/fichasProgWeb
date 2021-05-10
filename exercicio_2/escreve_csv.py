import csv

with open('pessoas.csv', 'w', newline='') as ficheiro:
    campos = ['Nome', 'Idade']
    writer = csv.DictWriter(ficheiro, fieldnames=campos)
    writer.writeheader()
    writer.writerow({'Nome': 'Luis', 'Idade': 27})
    writer.writerow({'Nome': 'Marcelo', 'Idade': 26})
    writer.writerow({'Nome': 'Ana', 'Idade': 20})
