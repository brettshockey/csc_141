while True:
  name = input("What's your first name? Write 'q' any time to quit")
  if name == 'q':
    break
  last = input("What's your last name? Write 'q' any time to quit ")
  if last == 'q':
    break
  
path = Path('guest_book.txt')

if name !='q' and last !='q':
  path.write_text(name,last)