"""
Make a dictionary containing three major rivers and the country each 
river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs 
through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the 
dictionary.
"""

rivers = {'egypt': 'nile',
          'china': 'yangtze',
          'russia': 'volga'}

for country, river in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')
print('\n')
for river in rivers.values():
    print(river.title())
print('\n')
for river in rivers.keys():
    print(river.title())