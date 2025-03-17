#1 Get the user's age as input
edad = int(input("Enter your age: "))

# Check if the user is 18 or older
if edad >= 18:
    print("You are old enough to learn to drive.")
else:
    # Calculate how many more years are needed
    years_left = 18 - edad
    print(f"You need {years_left} more years to learn to drive.")

# Get user input for ages
my_age = int(input("Enter your age: "))  # User's age
your_age = int(input("Enter my age: "))  # Your age

#2 Compare the ages
if my_age > your_age:
    # If the user is older
    age_diff = my_age - your_age
    if age_diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_diff} years older than me.")
elif my_age < your_age:
    # If the user is younger
    age_diff = your_age - my_age
    if age_diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {age_diff} years older than you.")
else:
    # If both are the same age
    print("We are the same age.")

    #3 Get two numbers from the user
a = float(input("Enter number one: "))  # First number
b = float(input("Enter number two: "))  # Second number

# Compare the two numbers and output the result
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

