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


def sub(a: list[int], b: int, c: int) -> list[int]:
    empty: lst[int] = []
    if len(a) == 0 or b > len(a) or c <= 0:
        return empty

    i: int = b
    sub: list[int] = []
    while b < c:
        sub.append(a[i])
        i += 1
    return sub


def concat(a: list[int], b: list[int]) -> list[int]:
    new: list[int] = []
    i: int = 0
    j: int = 0
    while i < len(a):
        new.append(a[i])
        i += 1
    while j < len(b):
        new.append(b[i])
        j += 1
    return new