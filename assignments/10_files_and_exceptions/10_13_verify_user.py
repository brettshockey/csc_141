import json

filename = 'user_info.json'

try:
    # Try to read the stored user dictionary
    with open(filename) as f:
        user = json.load(f)

except FileNotFoundError:
    # File not found → ask for user information
    name = input("What is your name? ")
    age = input("How old are you? ")
    color = input("What is your favorite color? ")

    # Build the dictionary
    user = {
        'name': name,
        'age': age,
        'favorite_color': color
    }

    # Save it to the JSON file
    with open(filename, 'w') as f:
        json.dump(user, f)

    print("\nThanks! I'll remember that information.")

else:
    # File exists → print what we remember
    print("\nI remember you!")
    print(f"Your name is {user['name']}.")
    print(f"You are {user['age']} years old.")
    print(f"Your favorite color is {user['favorite_color']}.")
