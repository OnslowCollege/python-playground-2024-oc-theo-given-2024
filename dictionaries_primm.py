""".-."""
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
students_data = {
    "Alice": {"age": 17, "grades": [132, 99, 85]},
    "Bob": {"age": 18, "grades": [92, 32, 95]},
    "Theo": {"age": 16, "grades": [86, 79, 96]},
}


library = {
    
}