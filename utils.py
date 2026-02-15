def save_to_file(student):
    with open("data.txt", "a") as file:
        file.write(f"{student.name},{student.marks},{student.gpa},{student.grade}\n")


def load_students():
    students = []

    try:
        with open("data.txt", "r") as file:
            for line in file:
                name, marks, gpa, grade = line.strip().split(",")
                students.append((name, int(marks), float(gpa), grade))
    except FileNotFoundError:
        pass

    return students
