"""
You don't have to limit the number of tests you create to 10. If you
want to try more comparisons, write more tests and add them to
conditional_tests.py. Have at least one True and one False result for
each of the following:
Tests for equality and inequality with strings.
Tests using the lower() method.
Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to.
Tests using the and keyword and the or keyword.
Test whether an item is or is not in a list.
"""

# Equality and inequality
cheese = 'gouda'
print(cheese == 'gouda')
print(cheese != 'gouda')
print(cheese == 'muenster')
print('\n')
# Lower() method
coffee = 'Light'
print(coffee.lower() == 'light')
print(coffee == 'light')
print('\n')
# Numerical tests
number = 7
print(number == 7)
print(number == 5)
print(number <= 10)
print(number >= 10)
print('\n')
# AND and OR - this will work in the console without printing here
age_0 = 20
age_1 = 22
(age_0 >= 21) and (age_1 >= 21)
(age_0 >= 21) or (age_1 >= 21)
# Is it in a list?
requested_toppings = ['pepperoni', 'mushrooms', 'sausage', 'onions']
'mushrooms' in requested_toppings
'pineapple'in requested_toppings

outdated_cpu = ['raptor', 'alder', 'sky', 'rocket']
cpu = 'meteor'
if cpu not in outdated_cpu:
    print(f"{cpu.title()} Lake is current as of Q2 2024.")