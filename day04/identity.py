# Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x is z:", x is z)      # True (same memory reference)
print("x is y:", x is y)      # False (different objects in memory)
print("x == y:", x == y)      # True (equal values)

# Check for None
connection = None
print("connection is None:", connection is None)
