# Simple Function
def greet():
    print("Hello, DevOps Engineer!")

# Function with Parameters and Return Value
def add(a, b):
    return a + b

# Function with Default Argument
def greet_user(name="Guest"):
    print("Welcome,", name)

# Function with *args and **kwargs
def show_details(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

# Executing Functions
greet()

result = add(5, 7)
print("Addition Result:", result)

greet_user("Tushar")
greet_user()

show_details("Python", "DevOps", user="Tushar", day=6)
