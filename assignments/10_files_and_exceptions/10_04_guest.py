name = input("What's your name? ")

from pathlib import Path
path = Path('user.txt')

path.write_text(name)