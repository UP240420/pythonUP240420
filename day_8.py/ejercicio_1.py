# Paso 1: Crear un diccionario vacío llamado 'perro'
perro = {}

# Paso 2: Agregar claves al diccionario 'perro'
perro['nombre'] = 'Buddy'
perro['color'] = 'Marrón'
perro['raza'] = 'Labrador'
perro['piernas'] = 4
perro['edad'] = 3

# Paso 3: Crear un diccionario 'estudiante' y agregar claves
estudiante = {
    'nombre': 'Juan',
    'apellido': 'Pérez',
    'género': 'Masculino',
    'edad': 20,
    'estado_civil': 'Soltero',
    'habilidades': ['Python', 'Análisis de Datos'],
    'país': 'EE.UU.',
    'ciudad': 'Nueva York',
    'dirección': '123 Calle Principal, NY'
}

# Paso 4: Obtener la longitud del diccionario 'estudiante'
longitud_estudiante = len(estudiante)
print(f"Longitud del diccionario estudiante: {longitud_estudiante}")

# Paso 5: Obtener el valor de 'habilidades' y verificar el tipo de dato
habilidades = estudiante['habilidades']
print(f"Habilidades: {habilidades}")
print(f"Tipo de dato de habilidades: {type(habilidades)}")  # Debe ser una lista

# Paso 6: Modificar las 'habilidades' agregando más habilidades
estudiante['habilidades'].append('Aprendizaje Automático')
estudiante['habilidades'].append('Desarrollo Web')

# Paso 7: Obtener las claves del diccionario como una lista
claves_estudiante = list(estudiante.keys())
print(f"Claves del diccionario estudiante: {claves_estudiante}")

# Paso 8: Obtener los valores del diccionario como una lista
valores_estudiante = list(estudiante.values())
print(f"Valores del diccionario estudiante: {valores_estudiante}")

# Paso 9: Cambiar el diccionario a una lista de tuplas usando el método items()
items_estudiante = list(estudiante.items())
print(f"Diccionario estudiante como lista de tuplas: {items_estudiante}")

# Paso 10: Eliminar uno de los elementos del diccionario (por ejemplo, 'dirección')
del estudiante['dirección']
print(f"Diccionario estudiante después de eliminar dirección: {estudiante}")

# Paso 11: Eliminar todo el diccionario 'estudiante'
del estudiante
# Si intentas imprimir estudiante aquí, dará un error porque el diccionario ha sido eliminado
# print(estudiante)  # Descomentar esta línea causará un NameError
