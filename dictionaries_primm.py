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




end = False
user_isbn = 0

while not end:
    print("Please enter a number.")
    print("1: Display all info")
    print("2: Display the info of a book of your choice.")
    print("3: Add a book to the library.")
    print("4: Exit the program.")
    user_input = input()
    if user_input == "1":
        for name, info in library.items():
            print("")
            print(f"Title: {name}")
            print(f"Author: {info['author']}")
            print(f"ISBN: {info['ISBN']}")
            print("")
    elif user_input == "2":
        user_input = input("Input the title of a book: ")
        for name, info in library.items():
            if user_input == name:
                print("")
                print(f"Title: {name}")
                print(f"Author: {info['author']}")
                print(f"ISBN: {info['ISBN']}")
                print("")
    elif user_input == "3":
        user_title = input("Please input the title: ")
        user_author = input("Please input the author: ")
        while user_isbn == 0:
            try:
                user_isbn = int(input("Please input the ISBN: "))
            except ValueError:
                print("Invalid Input.")
        library = [user_title]
        print("")
        print(f"Title: {user_title}")
        print(f"Author: {user_author}")
        print(f"ISBN: {user_isbn}")
        print("")
        user_isbn = 0
    elif user_input == "4":
        end = True
    else:
        print("Invalid Option")