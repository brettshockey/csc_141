"""
Use a dictionary to store people's favorite numbers. Think of five 
names, and use them as keys in your dictionary. Think of a favorite 
number for each person, and store each as a value in your dictionary. 
Print each person's name and their favorite number. For even more fun, 
poll a few friends and get some actual data for your program."""

# Yeah, because asking people what their favorite numbers are is 
# so much fun...
favorite_numbers = {'alice': 7,
                    'bob': 12,
                    'claire': 3,
                    'david': 42,
                    'emily': 17}

# When calling items from a dictionary in a for loop you use:
# <key> <value> positionally, which you can rename. The .items() method
# makes this possible
for name, number in favorite_numbers.items():
    print (f'{name.title()}'s favorite number is {number}.')