user_input: str = ("")
age: int
def ask_for_age():
    # Setting code to an empty string so the while loop starts
    while user_input == "":
        user_input = input("What is your age? ")
        #Using try in case of errors.
        try:
            #Finding the user's age and seeing if it is within the boundaries
            age = int(user_input)
            if age <= 0 or age >= 122:
                print("Age incorrect.")
                user_input = ""
            elif age < 18:
                print("Too young.")
                user_input = ""
            else:
                print("You may enter")
        except ValueError:
            #In case of the user not entering a number
            print("Please enter a number.")
            user_input = ""

