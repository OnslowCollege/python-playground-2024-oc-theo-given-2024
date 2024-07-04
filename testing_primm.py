
user_input: str = ("")
while user_input == "":
    user_input = input("What is your age? ")
    try:
        age: int = int(user_input)
        if age <= 0 or age >= 122:
            print("Age incorrect.")
            user_input = ""
        elif age < 18:
            print("Too young.")
            user_input = ""
        else:
            print("You may enter")
    except ValueError:
        print("Please enter a number.")
        user_input = ""

