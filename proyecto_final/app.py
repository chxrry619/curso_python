from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
import os
import csv
import json
from collections import defaultdict


# Rutas
AREAS_DIR = 'datos/csv/areas'
CATALOGOS_DIR = 'datos/csv/catalogos'
OUTPUT_JSON = 'datos/json/revistas_base.json'

# Diccionario de salida
revistas = defaultdict(lambda: {"areas": [], "catalogos": []})

# Leer archivos en la carpeta de áreas
for archivo in os.listdir(AREAS_DIR):
    if archivo.endswith('.csv'):
        area_nombre = os.path.splitext(archivo)[0].upper()
        with open(os.path.join(AREAS_DIR, archivo), newline='', encoding='latin1') as f:

            reader = csv.reader(f)
            for row in reader:
                titulo = row[0].strip().lower()
                if area_nombre not in revistas[titulo]["areas"]:
                    revistas[titulo]["areas"].append(area_nombre)

# Leer archivos en la carpeta de catálogos
for archivo in os.listdir(CATALOGOS_DIR):
    if archivo.endswith('.csv'):
        catalogo_nombre = os.path.splitext(archivo)[0].upper()
        with open(os.path.join(CATALOGOS_DIR, archivo), newline='', encoding='latin1') as f:
            reader = csv.reader(f)
            for row in reader:
                titulo = row[0].strip().lower()
                if catalogo_nombre not in revistas[titulo]["catalogos"]:
                    revistas[titulo]["catalogos"].append(catalogo_nombre)

# Guardar como JSON
os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
with open(OUTPUT_JSON, 'w', encoding='latin1') as f:
    json.dump(revistas, f, ensure_ascii=False, indent=4)

print(f"Archivo JSON generado en: {OUTPUT_JSON}")