import csv

def lee_archivo_csv(nombre_archivo):
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)
