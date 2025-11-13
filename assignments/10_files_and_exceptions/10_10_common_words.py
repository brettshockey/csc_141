filenames = ['text1.txt', 'text2.txt', 'text3.txt']  # your files

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Could not find {filename}.")
    else:
        word = 'the'
        count = contents.lower().count(word)
        print(f"{filename}: '{word}' appears {count} times.")

