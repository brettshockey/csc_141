# A buffet-style restaurant offers only five basic foods. Think of five 
# simple foods, and store them in a tuple.
# Use a for loop to print each food the restaurant offers.
# Try to modify one of the items, and make sure that Python rejects the 
# change.
# The restaurant changes its menu, replacing two of the items with 
# different foods. Add a line that rewrites the tuple, and then use a 
# for loop to print each of the items on the revised menu.

buffet_foods = ('fried rice',
				'chicken teriyaki',
				'eggrolls',
				'wonton soup',
				'mongolian beef'
				)
print("\nOriginal buffet foods: ")
for food in buffet_foods:
	print(food.title())

# Type error, since tuples don't support reassignment: 
# buffet_foods[0] = 'white_rice'

buffet_foods = ('white rice',
				'chicken teriyaki',
				'eggrolls',
				'eggdrop soup',
				'mongolian beef'
				)
print("\nModified buffet foods: ")
for food in buffet_foods:
	print(food.title())

# Exercises 4.14 & 4.15 ask you to read through the Python 'PEP8'
# styling guidelines and go through three of the previous exercises
# and style them according to those guidelines.

# I'm only doing it for this one.
# I added rulers to mark the max comment length of 72 and code line
# length of 79.

# As a side note, I finally got rid of the ugly VSC Github status
# indicators for each file since everything wasn't synced up.

# I still need more practice with pushing, pulling, and syncing files
# using the terminal, but I got the jist of it.
	
# Overall, the code looks much neater and i'm able to have the 
# VSC terminal open to the right side of the code for code output and to 
# push updates to Github without having a seperate CMD window open.
	
# Use 'git status' to check the status of your repository vs local.
# Use 'git add <file.name> to stage the file for commit.
# Use 'git commit -m <message> to commit the change.
# Use 'git push origin main' to push the file to the main branch.
	
# I can't wait to be done with the dictionaries chapter so I can get 
# into OOP with Python!