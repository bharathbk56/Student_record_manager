FILENAME = "students.txt"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    dept = input("Enter department: ")
    marks = input("Enter marks: ")
    with open(FILENAME, "a") as file:
        file.write(f"{name},{roll},{dept},{marks}\n")
    print("Student added successfully.\n")
    pass

def view_students():
    try:
        with open(FILENAME, "r") as file:
            print("\n📋 --- All Student Records ---")
            for line in file:
                line = line.strip()
                if line == "" or line.count(",") != 3:
                    continue  # skip invalid/empty lines
                name, roll, dept, marks = line.split(",")
                print(f"Name: {name}, Roll: {roll}, Dept: {dept}, Marks: {marks}")
            print()
    except FileNotFoundError:
        print("No records found.\n")
        pass

def search_student():
    roll_search = input("Enter roll number to search: ")
    found = False
    with open(FILENAME, "r") as file:
        for line in file:
            name, roll, dept, marks = line.strip().split(",")
            if roll == roll_search:
                print(f"\nRecord Found:\nName: {name}, Roll: {roll}, Dept: {dept}, Marks: {marks}\n")
                found = True
                break
    if not found:
        print("Student not found.\n")
    pass

def delete_student():
    roll_delete = input("Enter roll number to delete: ")
    updated_records = []
    deleted = False

    with open(FILENAME, "r") as file:
        for line in file:
            name, roll, dept, marks = line.strip().split(",")
            if roll != roll_delete:
                updated_records.append(line)
            else:
                deleted = True

    with open(FILENAME, "w") as file:
        file.writelines(updated_records)

    if deleted:
        print("Student deleted successfully.\n")
    else:
        print("Student not found.\n")
    pass

def menu():
    while True:
        print("=== Student Record Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll No")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")
menu()