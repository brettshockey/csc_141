"""
Make several dictionaries, where each dictionary represents a different 
pet. In each dictionary, include the kind of animal and the owner's 
name. Store these dictionaries in a list called pets. Next, loop through
 your list and as you do, print everything you know about each pet.
"""

scooby = {'animal': 'dog',
          'owner': 'shaggy'
          }

garfield = {'animal': 'cat',
            'owner': 'idfk'
            }

pets = [scooby, garfield]

for pet in pets:
    print(pet)