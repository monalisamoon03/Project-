from student import Student
from utils import save_to_file, load_students


def show_statistics():
    students = load_students()

    if not students:
        print("No student data found.")
        return

    marks = [s[1] for s in students]

    print("\nClass Statistics")
    print("----------------")
    print(f"Total Students : {len(students)}")
    print(f"Average Marks  : {sum(marks) / len(marks):.2f}")
    print(f"Highest Marks : {max(marks)}")
    print(f"Lowest Marks  : {min(marks)}")


def main():
    while True:
        print("\nStudent Result Analysis System")
        print("1. Add Student")
        print("2. Show Statistics")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))

            student = Student(name, marks)
            save_to_file(student)

            print("Student data saved successfully.")

        elif choice == "2":
            show_statistics()

        elif choice == "3":
            print("Program terminated.")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
