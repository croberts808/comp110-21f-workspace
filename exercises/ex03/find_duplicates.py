"""Finding duplicate letters in a word."""

__author__ = "730439833"

word: str = input("Enter a word: ")
i: int = 0
tf: bool = False

while i < len(word):
    character: str = word[i]
    index: int = i + 1
    while index < len(word):
        if character == word[index]:
            tf = True
        index += 1
    i += 1

print("Found Duplicate: " + str(tf))
