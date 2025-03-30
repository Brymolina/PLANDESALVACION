#Crear un diccionario con información personal

informacion_personal = { "nombre": "Bryan Molina", "edad": 30, "ciudad": "Atacames", "profesion": "Ingeniero" }

#Acceder y modificar el valor de la clave "ciudad"

informacion_personal["ciudad"] = "Atacames"

#Agregar una nueva clave-valor (ya existe "profesion", pero si fuera diferente, la agregamos)

informacion_personal["empresa"] = "Choc-Bang"

#Verificar si la clave "telefono" existe, si no, agregarla

if "telefono" not in informacion_personal: informacion_personal["telefono"] = "06 2731-789"

#Eliminar la clave "edad"

del informacion_personal["edad"]

#Imprimir el diccionario final
print(informacion_personal)