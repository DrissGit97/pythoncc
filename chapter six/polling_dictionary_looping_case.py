favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
other_names = {
    'josh': 'sql',
    'Tiffany': 'python',
    'George' : 'ruby',
    "jen" : "python",
    'sarah' : "c",
}
print("\nInitial name list")
for name in favorite_languages.keys():
    if name in favorite_languages:
        print(f"Hey, {name.title()}, wanna take another language pool?")
    else:
        print(f"Hey, {name.title}, wanna take a language pool?")

print("\nOther name list")
for name in other_names.keys():
    if name in favorite_languages:
        print(f"Hey, {name.title()}, wanna take another language pool?")
    else:
        print(f"Hey, {name.title()}, wanna take a language pool?")