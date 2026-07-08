text = "Python 2026"
print(len(text)) #output:11

text = "Hello"
print(type(text))  # Output: str

age = 23
print("Age is " + str(age))  # Output: Age is 23


word = "Code"
for i in range(len(word)):
    print(f"Index {i} has character {word[i]}")


user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")