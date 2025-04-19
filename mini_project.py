# Grade Management System

def display_menu():
    print("\nGrade Management System")
    print("1. Add Student and Grade")
    print("2. View All Students and Grades")
    print("3. Calculate Average Grade")
    print("4. Exit")

def add_student(grades):
    name = input("Enter student name: ")
    while True:
        try:
            grade = float(input(f"Enter grade for {name}: "))
            if 0 <= grade <= 100:
                grades[name] = grade
                print(f"Grade for {name} added successfully!")
                break
            else:
                print("Grade must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def view_students(grades):
    if not grades:
        print("No students found.")
    else:
        print("\nStudents and Grades:")
        for name, grade in grades.items():
            print(f"{name}: {grade}")

def calculate_average(grades):
    if not grades:
        print("No grades available to calculate average.")
    else:
        average = sum(grades.values()) / len(grades)
        print(f"The average grade is: {average:.2f}")

def main():
    grades = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_student(grades)
        elif choice == '2':
            view_students(grades)
        elif choice == '3':
            calculate_average(grades)
        elif choice == '4':
            print("Exiting the Grade Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()