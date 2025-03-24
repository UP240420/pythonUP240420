#Funciones de estadísticas para listas

def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0

#Función is_prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Función check_unique_elements

def check_unique_elements(lst):
    return len(lst) == len(set(lst))

#Función check_same_type

def check_same_type(lst):
    return all(isinstance(x, type(lst[0])) for x in lst)

#Función is_valid_variable

def is_valid_variable(variable):
    import keyword
    if not variable.isidentifier() or keyword.iskeyword(variable):
        return False
    return True

#Función most_spoken_languages

def most_spoken_languages():
    # Esta es una lista simulada de idiomas y su número de hablantes
    languages = {
        "Mandarin": 918000000,
        "Spanish": 460000000,
        "English": 377000000,
        "Hindi": 310000000,
        "Arabic": 310000000,
        "Bengali": 230000000,
        "Portuguese": 220000000,
        "Russian": 150000000,
        "Japanese": 125000000,
        "Punjabi": 120000000,
    }
    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:10]

#Función most_populated_countries

def most_populated_countries():
    countries = {
        "China": 1393409038,
        "India": 1366417754,
        "USA": 329500000,
        "Indonesia": 267670000,
        "Pakistan": 233500000,
        "Brazil": 211000000,
        "Nigeria": 206000000,
        "Bangladesh": 163000000,
        "Russia": 145900000,
        "Mexico": 127500000,
    }
    sorted_countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)
    return sorted_countries[:10]
