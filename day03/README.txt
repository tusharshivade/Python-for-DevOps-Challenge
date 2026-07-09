# 📅 Day 03 - Operators | User Input | Conditional Statements

## 📖 Introduction

Welcome to **Day 03** of my **20 Days Python for DevOps Challenge**.

Today, I learned how Python performs calculations, accepts user input, and makes decisions using conditional statements. These concepts are the foundation of automation and are widely used in DevOps for validating inputs, monitoring servers, checking system health, and automating deployment tasks.

---

# 🎯 Learning Objectives

- Learn Python Operators
- Accept User Input
- Understand Type Conversion
- Write Conditional Statements
- Build Beginner Python Programs
- Apply Python Concepts to DevOps Automation

---

# 📚 Topics Covered

## 1. Arithmetic Operators

Used to perform mathematical operations.

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Floor Division (`//`)
- Modulus (`%`)
- Exponent (`**`)

Example:

```python
a = 20
b = 10

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

---

## 2. Comparison Operators

Used to compare two values.

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

Example:

```python
age = 20

print(age >= 18)
```

---

## 3. Logical Operators

Used to combine multiple conditions.

- `and`
- `or`
- `not`

Example:

```python
age = 22
citizen = True

if age >= 18 and citizen:
    print("Eligible to Vote")
```

---

## 4. Assignment Operators

Used to update variable values.

- `=`
- `+=`
- `-=`
- `*=`
- `/=`
- `%=`

Example:

```python
count = 10

count += 5

print(count)
```

---

## 5. Membership Operators

Check whether a value exists in a sequence.

- `in`
- `not in`

Example:

```python
text = "Python DevOps"

print("Python" in text)
```

---

## 6. Identity Operators

Compare whether two objects refer to the same memory location.

- `is`
- `is not`

Example:

```python
a = [1, 2]
b = a

print(a is b)
```

---

## 7. User Input

Accept input from the user.

Example:

```python
name = input("Enter your name: ")

print("Welcome", name)
```

---

## 8. Type Conversion

Convert one data type into another.

Example:

```python
age = int(input("Enter Age: "))
salary = float(input("Enter Salary: "))
```

---

## 9. Conditional Statements

### if Statement

```python
age = 20

if age >= 18:
    print("Eligible")
```

### if...else Statement

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

### if...elif...else Statement

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
```

---

# 💻 Programs Practiced

- Addition Calculator
- Even or Odd Number
- Positive or Negative Number
- Voting Eligibility Checker
- Greatest of Three Numbers
- Grade Calculator
- Password Validator
- Login System
- ATM Withdrawal Checker
- Electricity Bill Calculator
- Age Category Checker
- BMI Calculator
- Temperature Converter
- Salary Bonus Calculator
- Simple Calculator

---

# 🚀 DevOps Use Cases

These Python concepts are useful in DevOps for:

- Validating deployment environments
- Checking disk usage
- Monitoring server status
- Automating Linux tasks
- Reading user input for scripts
- Creating deployment utilities
- Building automation tools
- Verifying configuration values

---

# 🛠 Skills Gained

- Performing mathematical operations
- Accepting user input
- Writing conditional logic
- Comparing values
- Building decision-making programs
- Understanding Python operators
- Creating beginner automation scripts

---

# 📂 Folder Structure

```
Day03/
│── 01_addition.py
│── 02_even_odd.py
│── 03_positive_negative.py
│── 04_voting.py
│── 05_greatest.py
│── 06_grade.py
│── 07_password.py
│── 08_login.py
│── 09_atm.py
│── 10_bill.py
│── 11_age_category.py
│── 12_bmi.py
│── 13_temperature.py
│── 14_bonus.py
│── 15_calculator.py
│── README.md
```

---

# 🎯 What I Learned

Today, I learned how to use Python operators for calculations, take input from users, convert data types, and write decision-making programs using conditional statements. These concepts are essential for developing automation scripts used in Cloud and DevOps environments.

---

# 📌 Challenge Status

- ✅ Operators
- ✅ User Input
- ✅ Type Conversion
- ✅ Arithmetic Operations
- ✅ Comparison Operators
- ✅ Logical Operators
- ✅ Conditional Statements
- ✅ Practice Programs Completed

---

# 🚀 Next Goal

**Day 04:** Loops (`for`, `while`) | `break` | `continue` | Nested Loops

---

## 🌟 About This Challenge

This repository is part of my **20 Days Python for DevOps Challenge**, where I practice Python every day to improve my automation and scripting skills for a career in **Cloud Computing and DevOps Engineering**.

### Connect with Me

If you have suggestions or feedback, feel free to connect with me.

⭐ Thank you for visiting my repository!