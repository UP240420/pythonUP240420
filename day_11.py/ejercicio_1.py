#Función add_two_numbers

def add_two_numbers(a, b):
    return a + b

#Función area_of_circle

import math

def area_of_circle(radius):
    return math.pi * radius * radius

#Función add_all_nums

def add_all_nums(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        return sum(args)
    else:
        return "Todos los argumentos deben ser números."

#Función convert_celsius_to_fahrenheit

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Función check_season

def check_season(month):
    if month in [12, 1, 2]:
        return "Invierno"
    elif month in [3, 4, 5]:
        return "Primavera"
    elif month in [6, 7, 8]:
        return "Verano"
    else:
        return "Otoño"

#Función calculate_slope

def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1) if x2 != x1 else "La pendiente es indefinida"

#Función solve_quadratic_eqn

import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No hay soluciones reales"

#Función print_list

def print_list(lst):
    for item in lst:
        print(item)

#Función reverse_list

def reverse_list(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)
    return reversed_lst

#Función capitalize_list_items

def capitalize_list_items(lst):
    return [item.upper() for item in lst]

#Función add_item

def add_item(lst, item):
    lst.append(item)
    return lst

#Función remove_item

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

#Función sum_of_numbers

def sum_of_numbers(n):
    return sum(range(n+1))

#Función sum_of_odds

def sum_of_odds(n):
    return sum(i for i in range(n+1) if i % 2 != 0)

#Función sum_of_evens

def evens_and_odds(n):
    evens = sum(1 for i in range(n+1) if i % 2 == 0)
    odds = n + 1 - evens
    print(f"The number of evens are {evens}.")
    print(f"The number of odds are {odds}.")
