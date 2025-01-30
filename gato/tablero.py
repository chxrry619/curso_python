import random

def dibuja_tablero(simbolos: dict):
    '''Dibuja el tablero del juego del gato'''
    print(f'''
 {simbolos['1']} | {simbolos['2']} | {simbolos['3']}  
---------
 {simbolos['4']} | {simbolos['5']} | {simbolos['6']} 
---------
 {simbolos['7']} | {simbolos['8']} | {simbolos['9']} 
''')

def ia(simbolos: dict):
    '''Estrategia de la computadora'''
    ocupado = True
    while ocupado:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X', 'O']:
            simbolos[x] = 'O'
            ocupado = False

def usuario(simbolos: dict):
    '''Estrategia del usuario'''
    ocupado = True
    lista_numeros = [str(i) for i in range(1, 10)]
    
    while ocupado:
        x = input('Elige un número del 1 al 9: ')
        if x in lista_numeros and simbolos[x] not in ['X', 'O']:
            simbolos[x] = 'X'
            ocupado = False
        else:
            print('Movimiento inválido, intenta de nuevo.')

def hay_ganador(simbolos: dict):
    '''Verifica si hay un ganador'''
    combinaciones_ganadoras = [
        ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],  # Horizontales
        ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],  # Verticales
        ['1', '5', '9'], ['3', '5', '7']                    # Diagonales
    ]
    
    for combo in combinaciones_ganadoras:
        if simbolos[combo[0]] == simbolos[combo[1]] == simbolos[combo[2]] and simbolos[combo[0]] in ['X', 'O']:
            return simbolos[combo[0]]  # Retorna 'X' o 'O' si hay un ganador
    return None

if __name__ == '__main__':
    numeros = [str(i) for i in range(1, 10)]
    dsimbolos = {x: x for x in numeros}
    
    dibuja_tablero(dsimbolos)
    
    for turno in range(5):  # Máximo 5 turnos (porque hay 9 casillas y se turnan)
        usuario(dsimbolos)
        dibuja_tablero(dsimbolos)
        
        ganador = hay_ganador(dsimbolos)
        if ganador:
            print(f'¡{ganador} ha ganado!')
            break
        
        if len([x for x in numeros if dsimbolos[x] not in ['X', 'O']]) == 0:
            print("¡Empate!")
            break
        
        ia(dsimbolos)
        dibuja_tablero(dsimbolos)

        ganador = hay_ganador(dsimbolos)
        if ganador:
            print(f'¡{ganador} ha ganado!')
            break

    print("Juego terminado.")
