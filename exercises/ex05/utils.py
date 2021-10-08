"""List utility functions part 2."""

__author__ = "730439833"

# Define your functions below


def only_evens(a: list[int]) -> list[int]:
    """Function that returns only the evens in a list."""
    b: list[int] = []
    i: int = 0
    while i < len(a):
        if a[i] % 2 == 0:
            b.append(a[i])
        i += 1
    return b


def sub(a: list[int], start: int, end: int) -> list[int]:
    """Function that returns a subset of the list we gave it."""
    empty: list[int] = []
    if len(a) == 0 or start > len(a) or end <= 0:
        return empty
    if start < 0:
        start = 0
    if end > len(a):
        end = len(a)
    i: int = start
    sub: list[int] = []
    while i < end:
        sub.append(a[i])
        i += 1
    return sub


def concat(a: list[int], b: list[int]) -> list[int]:
    """A function that concatenates two lists."""
    new: list[int] = []
    i: int = 0
    j: int = 0
    while i < len(a):
        new.append(a[i])
        i += 1
    while j < len(b):
        new.append(b[j])
        j += 1
    return new