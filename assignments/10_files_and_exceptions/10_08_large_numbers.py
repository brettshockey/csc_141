path1 = Path('cats.txt')
path2 = Path("dogs.txt")


cats = path1.read_text()
dogs = path2.read_text()

billian = cats.splitlines()
kuttay = dogs.splitlines()

# printing in list

for line in billian:
  print(line)

for line in kuttay:
  print(line)
# priting entire file.
billian
kuttay