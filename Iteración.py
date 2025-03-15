# Definir los datos
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Crear una matriz 3D manualmente con temperaturas aleatorias (entre 15 y 35 grados)
temperaturas = [
    [  # Ciudad A
        [20, 22, 21, 23, 24, 19, 25],  # Semana 1
        [18, 21, 20, 22, 23, 19, 26],  # Semana 2
        [19, 22, 21, 23, 24, 18, 25],  # Semana 3
        [20, 23, 22, 24, 25, 19, 26]   # Semana 4
    ],
    [  # Ciudad B
        [25, 27, 26, 28, 29, 24, 30],
        [24, 26, 25, 27, 28, 23, 31],
        [26, 28, 27, 29, 30, 25, 32],
        [27, 29, 28, 30, 31, 26, 33]
    ],
    [  # Ciudad C
        [30, 32, 31, 33, 34, 29, 35],
        [29, 31, 30, 32, 33, 28, 36],
        [28, 30, 29, 31, 32, 27, 34],
        [27, 29, 28, 30, 31, 26, 33]
    ]
]

# Calcular y mostrar los promedios de temperatura por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas para {ciudad}:")
    for semana in range(semanas):
        suma_temperaturas = sum(temperaturas[i][semana])
        promedio = suma_temperaturas / len(dias)  # Dividir entre 7 (días de la semana)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")