class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.gpa = self.calculate_gpa()
        self.grade = self.calculate_grade()

    def calculate_gpa(self):
        if self.marks >= 80:
            return 4.00
        elif self.marks >= 70:
            return 3.50
        elif self.marks >= 60:
            return 3.00
        elif self.marks >= 50:
            return 2.50
        elif self.marks >= 40:
            return 2.00
        else:
            return 0.00

    def calculate_grade(self):
        if self.marks >= 80:
            return "A+"
        elif self.marks >= 70:
            return "A"
        elif self.marks >= 60:
            return "A-"
        elif self.marks >= 50:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "F"
