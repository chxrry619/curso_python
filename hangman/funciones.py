"""
Funciones auxiliares del juego Ahorcado
"""

import string
import unicodedata
from random import choice

def carga_archivo_texto(archivo: str) -> list:
    """
    Carga un archivo de texto y devuelve una lista con las oraciones del archivo.
    """
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

def carga_plantillas(nombre_plantilla: str) -> dict:
    """
    Carga las plantillas del juego a partir de archivos de texto.
    """
    plantillas = {}
    for i in range(6):
        archivo = f'./hangman/plantilla/{nombre_plantilla}-{i}.txt'
        plantillas[i] = carga_archivo_texto(archivo)
    return plantillas

def despliega_plantilla(diccionario: dict, nivel: int):
    """
    Despliega una plantilla del juego.
    """
    if nivel in diccionario:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon.strip())

def obten_palabras(lista: list) -> list:
    """
    Obtiene las palabras de un texto.
    """
    texto = ' '.join(lista)  # Se toma toda la lista en lugar de partir en el índice 120
    palabras = texto.split()
    
    # Convertimos a minúsculas
    minusculas = [palabra.lower() for palabra in palabras]
    
    # Removemos signos de puntuación y caracteres especiales
    set_palabras = {palabra.strip(string.punctuation) for palabra in minusculas}
    
    # Filtramos palabras que contengan solo letras
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}
    
    # Removemos acentos
    set_palabras = {unicodedata.normalize('NFKD', palabra).encode('ascii', 'ignore').decode('ascii') for palabra in set_palabras}
    
    return list(set_palabras)

def adivina_letra(abc: dict, palabra: str, letras_adivinadas: set, turnos: int) -> int:
    """
    Adivina una letra de una palabra.
    """
    palabra_oculta = ''.join(letra if letra in letras_adivinadas else '_' for letra in palabra)

    print(f'Tienes {turnos} turnos restantes.')
    print(f'Palabra oculta: {palabra_oculta}')
    print(f'El abecedario es: {abc}')
    
    letra = input('Ingresa una letra: ').lower()
    
    if len(letra) != 1 or letra not in abc:
        print('Ingresa una letra válida.')
    else:
        if abc[letra] == "*":
            print('Ya ingresaste esa letra.')
        else:
            abc[letra] = "*"
            if letra in palabra:
                letras_adivinadas.add(letra)
            else:
                turnos -= 1  # Se descuenta turno si la letra no está en la palabra
    
    return turnos  # Retornar el número de turnos actualizado

if __name__ == '__main__':
    plantillas = carga_plantillas('plantilla')
    despliega_plantilla(plantillas, 5)
    
    lista_oraciones = carga_archivo_texto('./hangman/datos/pg155332.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    
    print(f"Total de palabras obtenidas: {len(lista_palabras)}")
    
    palabra_secreta = choice(lista_palabras)
    print(f'Palabra seleccionada (oculta en el juego): {palabra_secreta}')
    
    abcdario = {letra: letra for letra in string.ascii_lowercase}
    letras_adivinadas = set()
    turnos = 5
    
    while turnos > 0:
        turnos = adivina_letra(abcdario, palabra_secreta, letras_adivinadas, turnos)
        
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print(f"¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
            break
    else:
        print(f"Se acabaron los turnos. La palabra era: {palabra_secreta}")
