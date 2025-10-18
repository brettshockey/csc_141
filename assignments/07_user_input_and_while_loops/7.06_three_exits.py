"""
Write different versions of either exercise 7.04 or 7.05 that do each of
 the following at least once:
 
 Use a conditional test in the while statement to stop the loop.
 
 Use an active variable to control how long the loop runs.
 
 Use a break statement to exit the loop when the user enters a 'quit' 
 value.
 """
# active = True
while True:
    age = input("Please enter your age (or type 'quit' to exit): ")
# if age.lower() == 'quit':
# active = False
    if age.lower() == 'quit':
        break

    age = int(age)

    if age <= 3:
        print('Your ticket is free!')
    elif age > 3 and age < 13:
        print('Your ticket costs $10.')
    else:
        print('Your ticket costs $15.')