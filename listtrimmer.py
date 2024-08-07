the_list = input("Enter the list: ")
for i in range(2,len(the_list),8):
    print(the_list[i:i+4])
the_better_list = the_list.strip()
the_best_list = ""
for i in range(len(the_list)):
    print (the_list[i])
    user_input = input("Does this word belong in the list (y/n): ")
    if user_input == "y":
        the_best_list = the_best_list + the_list[i] + " "
print("Here is the trimmed list:")
print(the_best_list.split())