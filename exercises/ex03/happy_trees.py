"""Drawing forests in a loop."""

__author__ = "730439833"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Enter a number: "))
i: int = 0

if depth == 0:
    print("Depth: 0")
else:
    while i < depth:
        print(TREE)
        i += 1