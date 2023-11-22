print("\nFirst program: ")
from pathlib import Path

path = Path('pi_digits.txt')

contents = path.read_text()
for line in contents.splitlines():
    print(line)

print("\nSecond program: ")
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()
print(f"{pi_string[:52]}...")
print(len(pi_string))