print("Give me two numbers and I'll add them up")

first_number = input("\nFirst number: ")
second_number = input("\nSecond number: ")

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Please type a numerical value for both entries")
else:
    print(answer)