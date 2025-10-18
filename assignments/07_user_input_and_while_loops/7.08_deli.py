"""
Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop 
through the list of sandwich orders and print a message for each order, 
such as I made your tuna sandwich. As each sandwich is made, move it to 
the list of finished sandwiches. After all the sandwiches have been made
, print a message listing each sandwich that was made.
"""

# Start with sandwiches that haven't been made,
# and an empty list to hold finished sandwiches.
sandwich_orders = ['sandwich1',
                   'sandwich2',
                   'sandwich3',
                   'sandwich4',
                   'sandwich5'
                   ]

finished_sandwiches = []

# Make each sandwich until there are no more sandwich orders.
# Move each finished sandwich into the empty list.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f'{current_sandwich.title()} has been made.')
    finished_sandwiches.append(current_sandwich)

# Display the finished sandwiches.
print('\nThe following sandwiches have been made:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())