"""
Turn your if-else chain from exercise 5.4 into an if-elif-else chain.

If the alien is green, print a message that the player earned 5 points.

If the alien is yellow, print a message that the player earned 10.

If the alien is red, print a message that the player earned 15.

Write three versions of this program, making sure each message is
printed for the appropriate color alien.
"""

alien_color = 'yellow'
if alien_color == 'yellow':
    print('You have gained 5 points!')

alien_color = 'green'
if alien_color == 'green':
    print('You have gained 10 points!')

alien_color = 'red'
if alien_color == 'red':
    print('You have gained 15 points!')

# This will output 15 points since the last value for alien_color was 
# red.
if alien_color == 'yellow':
    print('You have earned 5 points!')
elif alien_color == 'green':
    print('You have earned 10 points!')
else:
    print('You have earned 15 points!')

# He said to write three versions so idk.

alien_color = ['yellow',
               'green', 
               'red'
               ]
for alien in alien_color:
    if alien == 'yellow':
        print('You have earned 5 points!')
    elif alien == 'green':
        print('You have earned 10 points!')
    else:
        print('You have earned 15 points!')