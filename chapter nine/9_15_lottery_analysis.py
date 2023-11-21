from random import choice

possible_numbers_letters = ["A", "B", "C", "D", "E", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
winning_ticket = []
my_ticket = ["A344"]
number_of_times = 0

while winning_ticket =! my_ticket:
    pulled_item = choice(possible_numbers_letters)
    if pulled_item not in winning_ticket:
        print(f"We pulled a... {pulled_item}")
        winning_ticket.append(pulled_item)
    if winning_ticket == my_ticket:
        print(f"This was it! It only took us {number_of_times}!")
    else:
        number_of_times += 1

print(f"\n And the final winner is... {winning_ticket}")