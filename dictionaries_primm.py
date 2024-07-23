# Function to process student information
def process_student_info(students: dict) -> None:
    """
    Process and display information about students.
    
    Parameters
    ----------
        students (dict): A dictionary containing student information with 'name'
                        as the key and a dictionary as the value.

    """
    for name, info in students.items():
        print(f"Student: {name}")
        print(f"Age: {info['age']}")
        print(f"Grades: {', '.join(map(str, info['grades']))}")
        print(f"Average Grade: {calculate_average_grade(info['grades']):.2f}")
        print()


def calculate_average_grade(grades: list) -> float:
    """
    Calculate the average grade from a list of grades.
    
    Parameters:
    - grades (list): List of student grades.
    
    Returns:
    - float: The average grade.
    """
    if not grades:
        return 0
    return sum(grades) / len(grades)


# Example usage
students_data = {
    'Alice': {'age': 17, 'grades': [85, 90, 78]},
    'Bob': {'age': 18, 'grades': [92, 88, 95]},
    'Charlie': {'age': 17, 'grades': [75, 80, 85]},
}


process_student_info(students_data)