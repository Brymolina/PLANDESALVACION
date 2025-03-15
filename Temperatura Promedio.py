# Definir los datos de la ciudad de Atacames
ciudad = "Atacames"
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Matriz 2D: temperaturas semanales (valores en grados Celsius)
temperaturas = [
    [25, 26, 27, 28, 29, 30, 31],  # Semana 1
    [26, 27, 28, 29, 30, 31, 32],  # Semana 2
    [27, 28, 29, 30, 31, 32, 33],  # Semana 3
    [28, 29, 30, 31, 32, 33, 34]   # Semana 4
]

# Función para calcular el promedio de temperatura por semana
def calcular_promedio(temperaturas):
    promedios = []
    for semana in range(semanas):
        promedio = sum(temperaturas[semana]) / len(dias)  # Promedio de cada semana
        promedios.append(promedio)
    return promedios

# Mostrar temperaturas registradas
print(f"\nTemperaturas registradas en {ciudad} durante {semanas} semanas:")
for semana, datos in enumerate(temperaturas, start=1):
    print(f"Semana {semana}: {datos}")

# Calcular los promedios semanales
promedios_semanales = calcular_promedio(temperaturas)

# Mostrar los resultados
print(f"\nPromedio de temperaturas en {ciudad}:")
for semana, promedio in enumerate(promedios_semanales, start=1):
    print(f"Semana {semana}: {promedio:.2f}°C")

    #estuvo complicado, no se si este bien realizado