"""Takes a list and puts all entries in double quotes."""
the_list = input("Enter the list: ")
the_list = the_list.replace("'", '"')
print("")
print("Here is the list:")
for i in range(0, len(the_list), 4095):
    print(the_list[i:i+4095])