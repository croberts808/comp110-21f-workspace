"""Examples of relational operators."""

__author__ = "123456789"

lhs: str = input("Left-hand int: ")
rhs: str = input("Right-hand int: ")

print(lhs + " < " + rhs + " is " + str(int(lhs) < int(rhs)))
print(lhs + " >= " + rhs + " is " + str(int(lhs) >= int(rhs)))
print(lhs + " == " + rhs + " is " + str(int(lhs) == int(rhs)))
print(lhs + " != " + rhs + " is " + str(int(lhs) != int(rhs)))