"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730439833"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

random: int = randint(1, 4)
print("Your fortune cookie says...")
if random == 1:
    print("Today will be your day to shine, beautiful!")
else:
    if random == 2:
        print("You might trip and fall today, but you can pick yourself back up :)")
    else:
        if random == 3:
            print("Do not listen to any tall handsome strangers...")
        else:
            if random == 4:
                print("You will receive a pleasent surprise!")
print("Now, go spread positive vibes!")
