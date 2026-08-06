students = []

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Search Student")
    print("5. Sort Students")
    print("6. Count Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    # View Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudents:")

            for i, student in enumerate(students, start=1):
                print(i, "-", student)

    # Remove Student
    elif choice == "3":
        name = input("Enter student name to remove: ")

        if name in students:
            students.remove(name)
            print("Student removed successfully!")
        else:
            print("Student not found.")

    # Search Student
    elif choice == "4":
        name = input("Enter student name to search: ")

        if name in students:
            print("Student found!")
        else:
            print("Student not found.")

    # Sort Students
    elif choice == "5":
        students.sort()
        print("Students sorted successfully!")

    # Count Students
    elif choice == "6":
        print("Total Students:", len(students))

    # Exit
    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")