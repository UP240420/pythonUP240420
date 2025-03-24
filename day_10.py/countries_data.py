# Suponiendo que el archivo 'countries_data.py' contiene datos sobre países
from countries_data import countries_data  # Importamos los datos de países

# Contamos el total de idiomas
total_idiomas = set()  # Usamos un set para evitar duplicados

for country in countries_data:
    idiomas = country.get('idiomas', [])
    total_idiomas.update(idiomas)

print("Número total de idiomas:", len(total_idiomas))
