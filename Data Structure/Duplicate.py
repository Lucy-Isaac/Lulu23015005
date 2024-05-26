def remove_element():
    num = input("Enter any values that you want :")
    unique_list = []
    unique_list.extend(num)
    dup_list = [x for i, x in enumerate(unique_list) if x not in unique_list[:i]]
    return dup_list

result = remove_element()
print(*result)
