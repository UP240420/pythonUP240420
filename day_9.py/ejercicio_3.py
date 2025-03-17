# The provided person dictionary
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Task 1: Check if the person dictionary has a 'skills' key, and if so, print out the middle skill
if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]  # Find the middle skill in the list
    print(f"The middle skill is: {middle_skill}")

# Task 2: Check if 'skills' contains 'Python' and print the result
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill.")
    else:
        print("The person doesn't have Python skill.")

# Task 3: Print the role based on the skills in the list
if 'skills' in person:
    skills = person['skills']
    
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print("He is a front end developer.")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("He is a backend developer.")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("He is a fullstack developer.")
    else:
        print("Unknown title")

# Task 4: If the person is married and lives in Finland, print the following information
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
