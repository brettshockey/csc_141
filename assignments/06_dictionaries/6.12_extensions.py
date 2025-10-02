"""
We're now working with examples that are complex enough that they can be
 extended in any number of ways. Use one of the example programs from 
this chapter, and extend it by adding new keys and values, changing the 
context of the program, or improving the formatting of the output.
"""

# Using cities.py for this exercise

cities = {
    'amsterdam': {
        'country': 'netherlands',
        'population': '800,000',
        'fact': 'has more than 100km of canals'
        },

    'copenhagen': {
        'country': 'denmark',
        'population': '600,000',
        'fact': 'is recognized globally as an exemplar of best practice'
                ' global planning'
        },

    'tokyo': {
        'country': 'japan',
        'population': '14,000,000',
        'fact': 'is near the boundary of three plates'
        }
}

for city, city_info in cities.items():
    print(f'\nCity: {city.title()}')
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f'\tCountry: {country.title()}')
    print(f'\tPopulation: {population}')
    print(f'\tFact: {fact}')