"""
Modify your program from exercise 6.2 so each person can have more than 
one favorite number. Then print each person's name along with their 
favorite numbers.
"""
favorite_numbers = {'Brett': [7, 14],
                    'Keyan': [12, 24],
                    'Mikale': [3, 6],
                    'Lazar': [42, 5],
                    'Zion': [17, 4]
                    }

# When calling items from a dictionary in a for loop you use:
# <key> <value> positionally, which you can rename. The .items() method
# makes this possible
for name, number in favorite_numbers.items():
    print(f'{name.title()}\'s favorite numbers are {number}.')

# When storing multiple values for a key you basically put them in a 
# list.