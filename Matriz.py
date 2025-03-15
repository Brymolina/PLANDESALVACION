def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición si encuentra el valor
    return None  # Retorna None si el valor no está en la matriz


# Definimos la matriz 3x3 con valores predefinidos
matriz = [
    [4, 8, 3],
    [6, 1, 9],
    [2, 5, 7]
]

# Valor a buscar en la matriz
valor_buscado = 5

# Buscar el valor en la matriz
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar resultado
print("Matriz:")
for fila in matriz:
    print(fila)

if posicion:
    print(f"\nEl número {valor_buscado} se encuentra en la posición {posicion}.")
else:
    print(f"\nEl número {valor_buscado} no está en la matriz.")

# ordenacion de arreglo multidimensional

    def bubble_sort(fila):
        n = len(fila)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if fila[j] > fila[j + 1]:
                    fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio de elementos


    # Definimos la matriz 3x3 con valores predefinidos
    matriz = [
        [9, 5, 3],
        [6, 8, 1],  # Esta fila se ordenará
        [7, 2, 4]
    ]

    # Mostrar la matriz original
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    # Fila que se ordenará (índice 1)
    fila_ordenar = 1

    # Ordenar la fila elegida
    bubble_sort(matriz[fila_ordenar])

    # Mostrar la matriz con la fila ordenada
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)