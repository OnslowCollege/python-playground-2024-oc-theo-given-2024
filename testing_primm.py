user_input: str = ("")
age: int
while user_input == "":
    def ask_for_age():
        user_input = input("What is your age? ")
        #Using try in case of errors.
        try:
            #Finding the user's age and seeing if it is within the boundaries
            age = int(user_input)
            if age <= 0 or age >= 122:
                print("Age incorrect.")
                user_input = ""
                return False
            if age < 18:
                print("Too young.")
                user_input = ""
                return False
            print("You may enter")
            return True
        except ValueError:
            #In case of the user not entering a number
            print("Please enter a number.")
            user_input = ""
            return False

