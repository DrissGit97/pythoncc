from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print("\nFirst, we print the file without any further modification: ")
print(contents)

learned = ''
print("\nSecond, we print the file in one string: ")
lines =contents.splitlines()
learned.replace('python', 'SQL')
for line in lines:
    learned += line
print(learned)