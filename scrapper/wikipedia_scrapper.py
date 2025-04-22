'''
Scrapper para Wikipedia
'''
import os
import argparse
import requests
from bs4 import BeautifulSoup
import json

def scrap(url: str):
    '''Obtiene página desde Internet'''
    pagina = requests.get(url, timeout=10)
    if pagina.status_code != 200:
        raise Exception(f'Error {pagina.status_code} en la página {url}')
    return pagina

def guardar_pagina(pagina, nombre_archivo: str):
    '''Guarda la página en un archivo'''
    with open(nombre_archivo, 'wb') as f:
        f.write(pagina.content)
    print(f'Página guardada en {nombre_archivo}')

def main(url: str, archivo_salida: str):
    '''Función principal'''
    if not os.path.exists(archivo_salida):
        pagina = scrap(url)
        guardar_pagina(pagina, archivo_salida)
        contenido = pagina.content
    else:
        print(f'El archivo {archivo_salida} ya existe. Leyendo de él.')
        with open(archivo_salida, 'rb') as f:
            contenido = f.read()

    soup = BeautifulSoup(contenido, 'html.parser')
    main_content = soup.find('div', class_='mw-body-content')
    if main_content:
        lis = main_content.find_all('li')
        diccionario_lis = {}
        print(f'Encontré {len(lis)} elementos <li> en la página')
        for li in lis[:5]:
            if li.a:
                print(f"{li.a.get('href')} : {li.a.text.strip()}")
                diccionario_lis[li.a.text.strip()] = li.a.get('href')
        lista = [{'pelicula': k, 'link': v} for k, v in diccionario_lis.items()]
        archivo_json = archivo_salida.replace('.html', '.json')
        with open(archivo_json, 'w', encoding='utf8') as f:
            json.dump(lista, f, ensure_ascii=False, indent=2)
        print(f'Datos guardados en {archivo_json}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrap Wikipedia page')
    parser.add_argument('--url', type=str, help='URL of the Wikipedia page to scrap')
    parser.add_argument('--output', type=str, help='Output file name')
    args = parser.parse_args()
    url = args.url if args.url else "https://es.wikipedia.org/wiki/Anexo:Pel%C3%ADculas_de_Star_Wars"
    output = args.output if args.output else "wiki.html"
    main(url, output)
