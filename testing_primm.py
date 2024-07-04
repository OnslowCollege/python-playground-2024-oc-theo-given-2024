user_input: str = input("What is your age? ")

while:
    try:
        age: int = int(user_input)
        if age <= 0 or age >= 122:
            print("Age incorrect.")
        elif age < 18:
            print("Too young.")
        else:
            print("You may enter")
    except ValueError:
        print("Please enter a number.")

