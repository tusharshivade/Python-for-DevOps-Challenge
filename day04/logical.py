# Logical Operators
a = True
b = False

print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)

# Check voting eligibility
age = 20
has_id = True
if age >= 18 and has_id:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Check divisibility
num = 15
if num % 3 == 0 and num % 5 == 0:
    print(num, "is divisible by 3 and 5")
