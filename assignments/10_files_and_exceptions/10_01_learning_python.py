from pathlib import Path
path = Path('python.txt')
contents = path.read_text()
lines = contents.splitlines()
# printing in list

for line in lines:
  print(line)

# priting entire file.
contents
