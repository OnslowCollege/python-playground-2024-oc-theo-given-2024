"""Allows the user to remove parts of a list."""
the_list = input("Enter the list: ")
the_better_list = ""
the_best_list = ""
for i in range(2,len(the_list),8):
    the_better_list = the_better_list + the_list[i:i+4]
print(the_better_list)

for i in range(0,len(the_list),4):
    print (the_better_list[i:i+4])
    user_input = input("Does this word belong in the list (y/n): ")
    if user_input == "y":
        the_best_list = the_best_list + the_better_list[i:i+4] + " "
print("Here is the trimmed list:")
print(the_best_list.split())

"dick, fuck"