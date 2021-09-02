"""Examples of numeric operators."""

__author__ = "123456789"

lhs: str = input("Left-hand side: ")
rhs: str = input("Right-hand side: ")

x: int = int(lhs)
y: int = int(rhs)

print(lhs + " ** " + rhs + " is " + str(x ** y))
print(lhs + " / " + rhs + " is " + str(x / y))
print(lhs + " // " + rhs + " is " + str(x // y))
print(lhs + " % " + rhs + " is " + str(x % y))