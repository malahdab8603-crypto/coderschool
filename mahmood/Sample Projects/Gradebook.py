import json

class Gradebook:
    def __init__(self):
        self.students = {}  
        self.load_data()

    def add_student(self, name):
        """Adds a new student to the gradebook."""
        if name not in self.students:
            self.students[name] = []
            print(f"Student {name} added.")
        else:
            print(f"Student {name} already exists.")

    def add_grade(self, name, subject, grade):
        """Adds a grade for a student."""
        if name in self.students:
            self.students[name].append((subject, grade))
            print(f"Added grade {grade}% for {subject} to {name}.")
        else:
            print(f"Student {name} not found. Please add them first.")

    def view_grades(self, name):
        """Displays grades for a student."""
        if name in self.students:
            if not self.students[name]:
                print(f"{name} has no grades yet.")
                return
            print(f"\nGrades for {name}:")
            for subject, grade in self.students[name]:
                print(f"{subject}: {grade}%")
            gpa = self.calculate_gpa(name)
            print(f"\n{name}'s GPA: {gpa:.2f}")
        else:
            print("Student not found.")

    def calculate_gpa(self, name):
        """Calculates and returns GPA based on percentage grades."""
        if name not in self.students or not self.students[name]:
            return 0.0

        def convert_to_gpa(grade):
            if grade >= 90:
                return 4.0
            elif grade >= 80:
                return 3.0
            elif grade >= 70:
                return 2.0
            elif grade >= 60:
                return 1.0
            else:
                return 0.0

        gpa_values = [convert_to_gpa(grade) for _, grade in self.students[name]]
        return sum(gpa_values) / len(gpa_values)  # Average GPA

    def save_data(self):
        """Saves gradebook data to file."""
        with open("grades.json", "w") as f:
            json.dump(self.students, f)
        print("Gradebook saved.")

    def load_data(self):
        """Loads gradebook data from file."""
        try:
            with open("grades.json", "r") as f:
                self.students = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = {}

def main():
    gradebook = Gradebook()

    while True:
        print("\nGradebook Menu:")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Grades & GPA")
        print("4. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            gradebook.add_student(name)

        elif choice == "2":
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            try:
                grade = float(input("Enter grade (0-100%): "))
                if 0 <= grade <= 100:
                    gradebook.add_grade(name, subject, grade)
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a numeric grade.")

        elif choice == "3":
            name = input("Enter student name: ")
            gradebook.view_grades(name)

        elif choice == "4":
            gradebook.save_data()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
