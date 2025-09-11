# A list of games
games = ['elden ring', 'Uncharted', 'ark', 'Last of Us', 'God of War', 'Farcry']
print(games)

# Add an item to the end of the list
games.append('Madden')
print(games)

# Insert an item into index value 8
games.insert(8, "NBA 2K")
print(games)

# Delete the list value at index 4
del games[4]
print(games)

# Delete the value from index 0
games.pop(0)
print(games)

# Remove a value from the list using .remove by assigning the variable to a value and calling it with the .remove function
example = 'ark'
games.remove(example)
print(games)

# Add the modified values back to the list using append
games.append('Madden')
games.append('elden ring')
games.append('ark')
print(games)

# Sort the list alphabetically, permanently
games.sort()
print(games)

# Reverse alphabetical sort the list permanently
games.reverse()
print(games)

# Print a temporarily alphabetically sorted list
print(sorted(games))

# Print how many elements are in the list
print(len(games))

# Print a statement detailing the list

print(f"I'm currently playing and wish to play about {(len(games))} games.")
uppercase_list = [x.upper() for x in games]
print(f"Here is the list in alphabetical order: \n{(sorted(uppercase_list))}.")

# Use formatted string to call len function to print the length of games
# Create a variable that iterates through each element in the list with the .upper function to convert each element to uppercase
# Use a formatted string to call the created variable within the sorted function to temporarily alphabetize the list