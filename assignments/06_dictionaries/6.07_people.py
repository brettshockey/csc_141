"""
Start with the program you wrote for exercise 6.1. Make two new 
dictionaries representing different people, and store all three 
dictionaries in a list called people. Loop through your list of people. 
As you loop through the list, print everything you know about each 
person.
"""

# Code from 6.1:

# weeknd = {'first_name': 'abel',
#           'last_name': 'tesfaye',
#           'age': 34,
#           'city': 'ontario'}

# print(weeknd['first_name'])
# print(weeknd['last_name'])
# print(weeknd['age'])
# print(weeknd['city'])

the_weeknd = {'first_name': 'abel',
              'last_name': 'tesfaye',
              'genre': 'r&b',
              'age': 34,
              'city': 'ontario'
              }

low_roar = {'first_name': 'ryan',
            'last_name': 'karazija',
            'genre': 'post_rock',
            'age': 40,
            'city': 'reykjavik'
            }

coheed_and_cambria = {'first_name': 'claudio',
                      'last_name': 'sanchez',
                      'genre': 'alt_rock',
                      'age': 46,
                      'city': 'suffern'
                      }           

artists = [the_weeknd,
           low_roar,
           coheed_and_cambria
           ]

for artist in artists:
    if artist == the_weeknd:
        print(artist)
    elif artist == low_roar:
        print(artist)
    else:
        print(artist)

# Well, I did what the exercise asked
# I do need more practice to figure out the syntax for nesting