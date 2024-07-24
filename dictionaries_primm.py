""".o."""
# Function to process student information
from typing import Any


def process_student_info(students: dict) -> None:
    """
    Process and display information about students.
    
    Arguments:
    ---------
        students: A dictionary containing student information with 'name'
                as the key and a dictionary as the value.

    """
    for name, info in students.items():
        if calculate_average_grade(info["grades"]) > 85:
            print(f"Student: {name}")
            print(f"Age: {info['age']}")
            print(f"Grades: {', '.join(map(str, info['grades']))}")
            print(
                f"Average Grade: {calculate_average_grade(info['grades']):.2f}"
            )
            print()


def calculate_average_grade(grades: list) -> float:
    """
    Calculate the average grade from a list of grades.
    
    Arguments:
    ---------
        grades (list): List of student grades.
    
    Returns:
    -------
        float: The average grade.

    """
    if not grades:
        return 0
    return sum(grades) / len(grades)


# Example usage
students_data = {
    "Alice": {"age": 17, "grades": [132, 99, 85]},
    "Bob": {"age": 18, "grades": [92, 32, 95]},
    "Theo": {"age": 16, "grades": [86, 79, 96]},
}

library = {
    "Harry Potter and the Philosopher's Stone": {"author": "J. K. Rowling", "ISBN": 747532745},  # noqa: E501
    "The Lightning Thief": {"author": "Rick Riordan", "ISBN": 9781423121701}
}

for name, info in students_data.items():
    print(f"Student: {name}")
    print(f"Age: {info['age']}")


valid_entry = False
end = False




while not end:
    print("Please enter a number.")
    print("1: Display all info")
    print("2: Display the info of a book of your choice.")
    print("3: Add a book to the library.")
    user_input = input()
    if user_input == "1":
        show_library(library)
        end = True
    elif user_input == "2":
        user_input = input("Input the title of a book: ")
        for title, info in library:
            print (f"Title: {title} ({info['author']})")
        end = True
    elif user_input == "3":
        end = True
    else:
        print("Invalid Option")