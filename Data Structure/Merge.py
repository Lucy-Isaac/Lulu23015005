# This program collects user two list user input and joins them in a new list and removing duplicates if any.

# split(): This method is used to split the user's input into a list of strings.
# enumerate: This is built in function that allows you to oop over a list(or other iterable) and have an automatic counter/inde along the values.

def merge_lists():
        lst1 =  input("enter a list of number1 (seperated by spaces): ").split()
        lst1 = [int(x) for x in lst1]
        lst2 = input("enter a list of number2(seprated by spaces): ").split()
        lst2 = [int(x) for x in lst2]
        newlist = []
        newlist.extend(lst1)
        newlist.extend(lst2)
        dup_list = [x for i, x in enumerate(newlist) if x not in newlist[:i]]
        return dup_list

dup_list = merge_lists()
print(dup_list)
