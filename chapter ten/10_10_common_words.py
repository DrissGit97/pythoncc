"""Count the number of iterations of 'flower' in a text file"""

from pathlib import Path
path = Path("botanical_magazine(gutenberg).txt")

contents = path.read_text(encoding='utf-8')

print(f"\nNumber of times the word 'flower'(case sensitive) was mentioned: {contents.count("flower")}")

print(f"\nNumber of times the word 'flower'(non-case sensitive) was mentioned: {contents.lower().count("flower")}")