#Función evens_and_odds

def evens_and_odds(n):
    evens = sum(1 for i in range(n+1) if i % 2 == 0)
    odds = n + 1 - evens
    print(f"The number of evens are {evens}.")
    print(f"The number of odds are {odds}.")

#Función factorial

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

#Función is_empty

def is_empty(value):
    return len(value) == 0 if hasattr(value, '__len__') else value == ""
