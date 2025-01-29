import matplotlib.pyplot as plt

def Calcular_Y(x: float, m: float, b: float) -> float:
    '''
    Calcula el valor de y en una linea recta
    x: valor de x
    m: pendiente
    b: interseccion de y
    regresa el valor de y
    '''
    return m * x + b


def main():
    m = 2
    b = 3
    x = 5
    y = Calcular_Y(x, m, b)
    print(f'Para x={x}, y={y}')

    # Prueba de la función de graficación
    X = [i for i in range(-10, 11)]
    Y = [Calcular_Y(i, m, b) for i in X]
    grafica_linea(X, Y, m, b)


def test_linea():
    '''
    Prueba de funcionamiento de Calcular_Y
    '''
    y = Calcular_Y(0.0, 2.0, 3.0)
    return y


def grafica_linea(X: list, Y: list, m: float, b: float):
    '''
    Grafica una línea recta basada en los puntos X y Y.
    '''
    plt.plot(X, Y)
    plt.title(f'Linea con pendiente {m} y ordenada al origen {b}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()


    if __name__ == '__main__':
        main()
        if test_linea() == 3.0:
            print('Todo bien')
        else:
            print('Error en la prueba')
