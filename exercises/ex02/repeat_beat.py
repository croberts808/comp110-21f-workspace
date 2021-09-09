"""Repeating a beat in a loop."""

__author__ = "730439833"

# Begin your solution here...

repeat: str = input("What beat do you want to repeat? ")
number: int = int(input("How many times do you want to repeat it? "))

rap = " " + repeat
i: int = 0

if number <= 0:
    print("No beat...")
else: 
    while i < number - 1:
        repeat = repeat + rap
        i += 1
    print(repeat)
    
















    