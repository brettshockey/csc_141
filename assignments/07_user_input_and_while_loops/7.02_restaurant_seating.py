"""
Write a program that asks the user how many people are in their dinner 
group. If the answer is more than eight, print a message saying they'll 
have to wait for a table. Otherwise, report that their table is ready.
"""

party = input('How many people are in your dinner group?')
party = int(party)

if party > 8:
    print('There will be a short wait.')
else:
    print('Your table is ready.')