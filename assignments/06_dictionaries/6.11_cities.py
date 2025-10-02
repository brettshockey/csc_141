"""
Make a dictionary called cities. Use the names of three cities as keys 
in your dictionary. Create a dictionary of information about each city 
and include the country that the city is in, its approximate population,
 and one fact about that city. The keys for each city's dictionary 
should be something like country, population, and fact. Print the name 
of each city and all the information you have stored about it.
"""

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

# Creating variables within the for loop makes for cleaner print 
# statements
for city, city_info in cities.items():
    print(f'\nCity: {city.title()}')
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f'\tCountry: {country.title()}')
    print(f'\tPopulation: {population}')
    print(f'\tFact: {fact}')