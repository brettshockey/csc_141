import json

filename = 'favorite_number.json'

try:
    # Try to read the stored number
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    # File doesn't exist yet → ask the user and store the number
    favorite_number = input("What is your favorite number? ")

    with open(filename, 'w') as f:
        json.dump(favorite_number, f)

    print("Thanks! I'll remember that.")
else:
    # File exists → report the stored number
    print(f"I know your favorite number! It's {favorite_number}.")
