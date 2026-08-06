#List Operations

fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
print(fruits)

#insert()
fruits = ["Apple", "Banana", "Mango"]

fruits.insert(1, "Orange")

print(fruits) 

#remove() 

fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)

#pop()

fruits = ["Apple", "Banana", "Mango"]

fruits.pop(1)

print(fruits)


#Change List Element

fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)

#Find List Length
fruits = ["Apple", "Banana", "Mango"]

print(len(fruits))

# Sort List
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)

#Count Value
numbers = [10, 20, 10, 30, 10, 40]

print(numbers.count(10))


#index()
fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Mango"))
