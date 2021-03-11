original_list = [1, 4, 4, 2, 3, 2, 8, 10, 8, 5]
new_list = [el for el in original_list if original_list.count(el) ==1]
print(new_list)