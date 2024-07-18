# numeric_wordlist_generator.py

import itertools

# Define the length of the numeric passwords you want to generate
password_length = 8

# Define the characters to use (0-9 for numeric passwords)
characters = '0123456789'

# Generate all combinations
combinations = itertools.product(characters, repeat=password_length)

# Write combinations to a file
with open('numeric-wordlist.txt', 'w') as f:
    for combination in combinations:
        f.write(''.join(combination) + '\n')

print(f"Generated numeric wordlist 'numeric-wordlist.txt' with {len(characters)**password_length} entries.")
