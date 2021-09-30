"""List utility functions."""

__author__ = "730439833"


# TODO: Implement your functions here.
def all(x: list[int], y: int) -> bool:
    """Function that determines whether the elements are the same."""
    if len(x) == 0:
        return False
    
    i: int = 0
    while i < len(x):
        if x[i] != y:
            return False
        i += 1
    return True


def is_equal(x: list[int], y: list[int]) -> bool:
    """Determine if the lists are equal."""
    if len(x) != len(y):
        return False
    
    i: int = 1
    while i < len(x):
        if x[i] != y[i]:
            return False
        i += 1
    return True


def max(x: list[int]) -> int:
    """Return maximum value in list."""
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        maximum: int = x[0]
        i: int = 0
        while i < len(x):
            if x[i] > maximum:
                maximum = x[i]
            i += 1
    return maximum