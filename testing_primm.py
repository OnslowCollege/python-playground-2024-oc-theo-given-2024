"""a."""
valid_age: bool = False
user_input: str = ("")
age: int

def ask_for_age():
    """
    Return a Boolean that is whether the user's age is above or below 18.

    Returns: False if age is below 18 and True if it is above 18.

    """
    while not valid_age:
        user_input = input("What is your age? ")
        #Using try in case of errors.
        try:
            #Finding the user's age and seeing if it is within the boundaries
            age = int(user_input)
            if age <= 0 or age >= 122:
                print("Age incorrect.")
            else:
                #Returning either false or true depending on age
                return age >= 18
        except ValueError:
            #In case of the user not entering a number
            print("Please enter a number.")
    return None

if ask_for_age():
    print ("You may enter")
else:
    print ("Too young")