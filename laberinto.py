def laberinto(dimension, obstaculos):
    ''' Función que construye un laberinto cuadrado de una dimensión dada con obstáculos.

    Parámetros requeridos:
        - dimension: cantidad de columnas y filas para generar una matriz cuadrada.
        - obstaculos: Es una lista de tuplas con posiciones donde hay obstáculos.

    Salida: 
        Una matriz que representa el laberinto. 
    '''

    # Creamos una lista vacía para añadir las filas del laberinto.
    laberinto = []
    # Bucle para añadir las filas del laberinto.
    for i in range(dimension):
        # Creamos una lista vacía para añadir las casillas de la fila.
        fila = []
        # Bucle para recorrer las columnas del laberinto.
        for j in range(dimension):
            # Comprobar si la tupla está en la lista de obstáculos.
            if tuple([i, j]) in obstaculos:
                fila.append('X')
            else:
                fila.append('0')
        laberinto.append(fila)
    return laberinto

def mostrar_laberinto(laberinto):
    for fila in laberinto:
        print(' '.join(fila))

def instrucciones(laberinto):
    instrucciones = []
    fil = 0
    col = 0
    dimension = len(laberinto)

    while True:
        if fil < dimension - 1 and laberinto[fil + 1][col] == '0':
            instrucciones.append('abajo')
            fil += 1
        elif col < dimension - 1 and laberinto[fil][col + 1] == '0':
            instrucciones.append('derecha')
            col += 1
        elif fil > 0 and laberinto[fil - 1][col] == '0':
            instrucciones.append('arriba')
            fil -= 1
        elif col > 0 and laberinto[fil][col - 1] == '0':
            instrucciones.append('izquierda')
            col -= 1
        else:
            break

    return instrucciones

# Tupla de posiciones de las celdas con obstáculos en el laberinto
obstaculo = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))
# Tamaño de la matriz
dimension = 5
# llamada a la función una vez establecidos los valores de obstáculos
lab = laberinto(dimension, obstaculo)

# Imprimir el laberinto
mostrar_laberinto(lab)

# Generar e imprimir las instrucciones
instrucciones = instrucciones(lab)
print("Instrucciones para seguir los ceros:")
print(', '.join(instrucciones))

# Esperamos al usuario
input("Presione enter para salir")
