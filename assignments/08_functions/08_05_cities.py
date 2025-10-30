def describe_city(name,country):
  print(f"{name} is in {country}")
  
describe_city("Brooklyn","New York")

def describe_city(name,country='New York'):
  print(f"{name} is in {country}")
  
describe_city(name='The Bronx')

describe_city(name='New York City')

describe_city(name='Staten Island')