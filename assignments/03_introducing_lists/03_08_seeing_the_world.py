locations = ['Tokyo', 'Japan', 'dubai', 'Brazil', 'Alaska']

print(locations)
# Print temporary alphabetical sort.
print(sorted(locations))
# Show that the list isn't permanently changed.
print(locations)
# Print temporary reverse alphabetical sort.
print(sorted(locations, reverse=True))
# Show that the list isn't permanently changed.
print(locations)
# Reverse the order of the list permanently.
locations.reverse()
print(locations)
# Reverse the order of the list permanently again.
locations.reverse()
print(locations)
# Permanently sort the list in alphabetical order.
locations.sort()
print(locations)
# Permanently sort the list in reverse alphabetical order.
locations.sort(reverse=True)
print(locations)