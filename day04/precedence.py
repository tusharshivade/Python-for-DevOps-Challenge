# Operator Precedence
res1 = 10 + 5 * 2
print("10 + 5 * 2 =", res1)  # Multiplication runs first: 10 + 10 = 20

res2 = (10 + 5) * 2
print("(10 + 5) * 2 =", res2)  # Parentheses run first: 15 * 2 = 30

res3 = 2 ** 3 * 2
print("2 ** 3 * 2 =", res3)  # Exponent runs first: 8 * 2 = 16
