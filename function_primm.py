"""
Main.

Created by: Theo
Date: 24 June 2024
"""
def add():
    answer = number_1 + number_2
    print (str(number_1) + " + " + str(number_2) + " = " + str(answer))
def subtract():
    answer = number_1 - number_2
    print (str(number_1) + " - " + str(number_2) + " = " + str(answer))


number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))


calc_type = input("Type add or subtract: ")
calc_type = calc_type.lower()

if calc_type == "add":
    add()
elif calc_type == "subtract":
    subtract()
