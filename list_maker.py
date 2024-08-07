"""Takes a string of same length words and turns them into a list."""
word_length = int(input("Enter length of all words in the list: "))
the_list = input("Enter The list:")
print("")

the_better_list = ""
for i in range(0,len(the_list),word_length):
    the_better_list = the_better_list + the_list[i:i+word_length]
    the_better_list = the_better_list + " "
the_best_list = the_better_list.split()
print(the_best_list)
