user_input: str = input("What is your age? ")

try:
    age: int = int(user_input)
    if age <= 0 and age >= 122:
        print("Age incorrect.")
    elif age < 18:
        print("Too young.")
    else:
        print("You may enter")
except ValueError:
    print("Please enter a number.")
