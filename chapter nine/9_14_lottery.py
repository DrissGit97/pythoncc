from random import choice
lottery_numbers = [
    "A", 
    "B", 
    "C", 
    "D",
    "E",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    ]

print(f"\nThe winning number is...! "
      f" {choice(lottery_numbers)} {choice(lottery_numbers)} {choice(lottery_numbers)} {choice(lottery_numbers)}")