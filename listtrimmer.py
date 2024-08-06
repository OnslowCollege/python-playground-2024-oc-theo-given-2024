the_list: list[str] = list(input("Enter the list: "))
the_better_list = ""
for i in range(len(the_list)):
    print (the_list[i])
    user_input = input("Does this word belong in the list (y/n): ")
    if user_input == "y":
        the_better_list = the_better_list + the_list[i] + " "
print("Here is the trimmed list:")
print(the_better_list.split())