# Escritura en archivo de texto
# Abrimos el archivo my_notes.txt en modo escritura (si no existe, se crea automáticamente)
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales
    file.write('Nota 1: Recordar repasar la teoría de cálculo para la clase de mañana.\n')
    file.write('Nota 2: Comprar víveres el fin de semana.\n')
    file.write('Nota 3: Revisar el código del proyecto de Python, esperando no estar mal.\n')

# Lectura de archivo de texto
# Abrimos el archivo en modo lectura para leer su contenido
with open('my_notes.txt', 'r') as file:
    # Leemos y mostramos el contenido línea por línea
    for line in file:
        print(line.strip())  # Usamos strip() para eliminar los saltos de línea extra

# El archivo se cierra automáticamente al salir del bloque `with` después de cada operación