"""
Now that you know how to loop through a dictionary, clean up the code 
from exercise 6.3 by replacing your series of print() calls with a loop 
that runs though the dictionary's keys and values. When you're sure 
that your loop works, add five more Python terms to your glossary. 
When you run your program again, these new words and meanings should 
automatically be included in the output."""

# I already did this. Adding five more.

words = {'dictionary': 'glossary',
         'continue': 'skip',
         'break': 'exit',
         'try': 'exception_handling',
         'lambda': 'anonymous_function',
         'index': 'list_value',
         'return': 'exit_and_return_value',
         'none': 'absence_of_value',
         'assert': 'debugging',
         'def': 'function'
         }

for word, meaning in words.items():
    print(f'{word.title()}: {meaning.title()}')