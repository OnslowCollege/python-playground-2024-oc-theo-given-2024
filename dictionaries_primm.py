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


# Beginning of second task

#Creating original dictionary
library = {
    "Harry Potter and the Philosopher's Stone": {
        "author": "J. K. Rowling", 
        "ISBN": 747532745},
    "The Lightning Thief": {
        "author": "Rick Riordan",
        "ISBN": 9781423121701},
}



#Setting up values for while loops
end = False
user_isbn = 0

#Uses 'while not end' so that it ends specifically when I want it to
while not end:
    #Displaying options before asking for user input.
    print("Please enter a number.")
    print("1: Display all info")
    print("2: Display the info of a book of your choice.")
    print("3: Add a book to the library.")
    print("4: Exit the program.")
    user_input = input()
    if user_input == "1":
        #Goes through each dictionary entry and outputs all the info of each.
        for name, info in library.items():
            #Empty print statements used for easier readability
            print("")
            print(f"Title: {name}")
            print(f"Author: {info['author']}")
            print(f"ISBN: {info['ISBN']}")
            print("")
    elif user_input == "2":
        user_input = input("Input the title of a book: ")
        #Checks each dictionary entry for the title entered and prints the info of any that have it  # noqa: E501
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
        #While loop is used to prevent an error occurring.
        while user_isbn == 0:
            try:
                user_isbn = int(input("Please input the ISBN: "))
            except ValueError:
                print("Invalid Input.")
        #Adding new dictionary entry
        library[user_title] = {"author": user_author, "ISBN": user_isbn}
        #Prints the dictionary entry to show the user it has been made
        print("")
        print(f"Title: {user_title}")
        print(f"Author: {user_author}")
        print(f"ISBN: {user_isbn}")
        print("")
        user_isbn = 0
    elif user_input == "4":
        #Ends the program
        end = True
    else:
        #If anything other than one of the options is entered, it will print this  # noqa: E501
        print("Invalid Option")