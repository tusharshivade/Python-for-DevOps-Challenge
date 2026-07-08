def greet():
    print("Hello! Welcome to Python.")

# function Calling
greet()




#here some common example
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Tushar")



#Function with a Return Value
def add_numbers(num1, num2):
    return num1 + num2

# Saving the result to a variable
result = add_numbers(10, 15)
print(result)



#Function with Default Arguments
def introduce(name, country="India"):
    print(f"{name} is from {country}.")
introduce("John", "USA")  

introduce("Tushar")



#Function with Variable-Length Arguments
def sum_all_numbers(*args):
    total = sum(args)
    return total

print(sum_all_numbers(1, 2, 3))
print(sum_all_numbers(10, 20, 30, 40))