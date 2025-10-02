"""
Make a dictionary called favorite_places. Think of three names to use as
 keys in the dictionary, and store one to three favorite places for each
  person. To make this exercise a bit more interesting, ask some friends
  to name a few of their favorite places. Loop through the dictionary, 
  and print each person's name and their favorite places.
"""
#Create dictonary with multiple values per key
favorite_places = {'Brett': ['Germany', 'Switzerland', 'Colorado'],
                   'Keyan': ['China', 'Los Angeles', 'Alaska'],
                   'Mikale': ['Japan', 'Nigeria', 'Hong Kong'],
                   'Zion': ['Japan', 'Mexico', 'Brazil'],
                   'Lazar': ['Tokyo', 'Pittsburgh', 'Iceland']
                   }

# Loop through the keys, values in favorite_places with .items()
for name, place in favorite_places.items():
    print(f'\n{name.title()}\'s favorite places are:')
# Nest a for loop within the first to call created value 'place'
    for place in place:
        print(f'\n{place.title()}')