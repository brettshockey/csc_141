filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
            print(f"\nContents of {filename}:")
            print(contents)
    except FileNotFoundError:
        # Silent failure — no message, no crash
        pass
