
def dibuja_tablero(simbolos: dict):
    '''Dibuja el tablero del juego del gato'''
    print(f'''
 {simbolos['1']} | {simbolos['2']} | {simbolos['3']}  
---------
 {simbolos['4']} | {simbolos['5']} | {simbolos['6']} 
---------
 {simbolos['7']} | {simbolos['8']} | {simbolos['9']} 
''')

if __name__ == '__main__':
    numeros = {str(i): str(i) for i in range(1, 10)}
    dsimbolos = {x:x for x in numeros}
    dsimbolos['5'] = 'X'
    dibuja_tablero(dsimbolos)
    dsimbolos['7'] = '0'    
    dibuja_tablero(dsimbolos)