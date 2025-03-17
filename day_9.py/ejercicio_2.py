#1 Grade assignment based on score
score = int(input("Enter your score: "))

if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score <= 89:
    print("Grade: B")
elif 60 <= score <= 69:
    print("Grade: C")
elif 50 <= score <= 59:
    print("Grade: D")
elif 0 <= score <= 49:
    print("Grade: F")
else:
    print("Invalid score entered!")

#2 Season check based on month
month = input("Enter a month (e.g., September): ").lower()

if month in ['september', 'october', 'november']:
    print("The season is Autumn.")
elif month in ['december', 'january', 'february']:
    print("The season is Winter.")
elif month in ['march', 'april', 'may']:
    print("The season is Spring.")
elif month in ['june', 'july', 'august']:
    print("The season is Summer.")
else:
    print("Invalid month entered!")

#3 Fruit list management
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit name: ").lower()

# Check if the fruit exists in the list
if new_fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit)
    print(f"The modified fruit list: {fruits}")
