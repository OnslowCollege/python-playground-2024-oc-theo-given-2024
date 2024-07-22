StudentData = list[list[str | int]]
SUBJECTS = ["Maths", "Science", "English"]


def display_student_data(student_data: StudentData):
    print("Student Data:")
    print(f"{'Name':<15} {'Science':<10} {'Science':<10} {'English':<10}")
    for student in student_data:
        print(f"{student[0]:<15} {student[1]:<10} {student[2]:<10} {student[3]:<10}")




def average_grades(subject_index: int, student_data: StudentData):
    total: int = 0
    for student in student_data:
        total += student[subject_index]
    return total / len(student_data)




# Sample student data (Name, Math, Science, English)
student_data: StudentData = [
    ["Alice", 85, 90, 92],
    ["Bob", 78, 88, 80],
    ["Charlie", 92, 94, 89],
]


looping: bool = True
while looping:
    print("\nOptions:")
    print("1. Display Student Data")
    print("2. Calculate Average Grades")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        display_student_data(student_data)
    elif choice == "2":
        subject = input("Enter the subject (Math, Science, or English): ").capitalize()
        if subject in SUBJECTS:
            # Gets the index of the subject to pass to the average_grades function.
            subject_index = SUBJECTS.index(subject)
            avg = average_grades(subject_index, student_data)
            print(f"The average grade in {subject} is: {avg:.2f}")
        else:
            print("Invalid subject. Please enter Math, Science, or English.")
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        looping = False
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

