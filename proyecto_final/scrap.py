from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
import json
import os
import time
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

INPUT_JSON = "datos/json/revistas_base.json"
OUTPUT_JSON = "datos/json/revistas_enriquecidas.json"
BASE_URL = "https://www.scimagojr.com"
# Carga los datos ya existentes (si los hay)
if os.path.exists(OUTPUT_JSON):
    with open(OUTPUT_JSON, "r", encoding="latin1") as f:
        datos_existentes = json.load(f)
else:
    datos_existentes = {}

# Carga los títulos base para verificar existencia
with open(INPUT_JSON, "r", encoding="latin1") as f:
    revistas_base = json.load(f)

def buscar_url_revista(titulo):
    query = '+'.join(titulo.split())
    url = f"{BASE_URL}/search.php?q={query}&tip=jou"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    resultados = soup.select("div.search_results a")
    for r in resultados:
        if unidecode(titulo.lower()) in unidecode(r.text.strip().lower()):
            return BASE_URL + "/" + r["href"]
    return None

def extraer_info_revista(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    data = {}

    try:
        data["sitio_web"] = soup.select_one("a[href^=http]").get("href", "")
        data["h_index"] = soup.find("div", class_="hindexnumber").text.strip()
        data["subject_area"] = soup.find("div", class_="area").text.strip()
        data["publisher"] = soup.find(text="Publisher").find_next("span").text.strip()
        data["issn"] = soup.find(text="ISSN").find_next("span").text.strip()
        data["widget"] = url.replace("/journalsearch.php?q=", "/journals.php?jid=")
        data["publication_type"] = soup.find(text="Type").find_next("span").text.strip()
    except Exception as e:
        print(f"Error extrayendo datos de {url}: {e}")
        return None

    return data

# Modo interactivo
while True:
    titulo = input("Ingresa el título de la revista (o escribe 'salir' para terminar): ").strip().lower()
    if titulo == "salir":
        break

    if titulo not in revistas_base:
        print("⚠️ Título no está en el archivo base.")
        continuar = input("¿Deseas buscarlo de todos modos? (s/n): ").strip().lower()
        if continuar != 's':
            continue

    if titulo in datos_existentes:
        print(f"✔ Ya existe información para: {titulo}")
        continue

    url = buscar_url_revista(titulo)
    if not url:
        print("❌ No se encontró la revista.")
        continue

    print(f"🌐 Extrayendo información de: {url}")
    info = extraer_info_revista(url)
    if info:
        datos_existentes[titulo] = info
        with open(OUTPUT_JSON, "w", encoding="latin1") as f:
            json.dump(datos_existentes, f, ensure_ascii=False, indent=2)
        print("✅ Guardado.")
    else:
        print("⚠️ No se pudo extraer información.")

    time.sleep(3)