import funciones as fn

archivo_csv = 'frases.csv'
lista_libros = fn.lee_archivo_csv(archivo_csv)

def mostrar_tabla(frases):
    if not frases:
        print("No se encontraron resultados.")
        return

    encabezado = ["Frase", "Película"]
    ancho_frase = max(len(encabezado[0]), max(len(f['frase']) for f in frases))
    ancho_pelicula = max(len(encabezado[1]), max(len(f['pelicula']) for f in frases))
    linea = f"+{'-' * (ancho_frase + 2)}+{'-' * (ancho_pelicula + 2)}+"

    print(linea)
    print(f"| {'Frase'.ljust(ancho_frase)} | {'Película'.ljust(ancho_pelicula)} |")
    print(linea)
    for fila in frases:
        print(f"| {fila['frase'].ljust(ancho_frase)} | {fila['pelicula'].ljust(ancho_pelicula)} |")
    print(linea)

def buscar_frases(frases, termino):
    termino = termino.lower()
    return [f for f in frases if termino in f['frase'].lower() or termino in f['pelicula'].lower()]

if __name__ == '__main__':
    while True:
        print("\n=== Buscador Momichi ===")
        termino = input("Escribe una palabra o parte de la frase a buscar (o escribe 'salir'): ").strip()
        if termino.lower() == 'salir':
            break
        resultados = buscar_frases(lista_libros, termino)
        mostrar_tabla(resultados)






        if __name__ == '__main__':
            parser = argparse.ArgumentParser(description="Buscador de frases célebres")