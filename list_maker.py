the_list = input("Enter The list:")
print("")
the_better_list = ""
for i in range(0,len(the_list),6):
    the_better_list = the_better_list + the_list[i:i+6]
    the_better_list = the_better_list + " "
the_best_list = the_better_list.split()
print(the_best_list)
