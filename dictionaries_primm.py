""".o."""
# Function to process student information


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
library = {
    "Harry Potter and the Philosopher's Stone": {"author": "J. K. Rowling", "ISBN": 747532745},
    "The Lightning Thief": {"author": "Rick Riordan", "ISBN": 9781423121701},
}




valid_entry = False
end = False




while not end:
    print("Please enter a number.")
    print("1: Display all info")
    print("2: Display the info of a book of your choice.")
    print("3: Add a book to the library.")
    user_input = input()
    if user_input == "1":
        for name, info in library.items():
            print(f"Title: {name}")
            print(f"Author: {info['author']}")
            print(f"ISBN: {info['ISBN']}")
        end = True
    elif user_input == "2":
        user_input = input("Input the title of a book: ")
        for name, info in library.items():
            if user_input == name:
                print(f"Title: {name}")
                print(f"Author: {info['author']}")
                print(f"ISBN: {info['ISBN']}")
        end = True
    elif user_input == "3":
        end = True
    else:
        print("Invalid Option")