def carga_archivo_texto(archivo: str) -> list:
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones


if __name__ == '__main__':
    lista = carga_archivo_texto('./hangman/plantilla/bad-apple.txt')
    for elemento in lista:
        print(elemento)
